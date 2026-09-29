import base64
import re
from pathlib import Path

import pandas as pd
import streamlit as st

ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def minute_sort_key(minute) -> int:
    """'45+2' -> 4502, '90' -> 9000. A single sortable int (base*100 +
    stoppage). Pulls digit groups out with regex rather than splitting on
    '+' specifically, so it doesn't silently fail (and fall back to the
    end-of-list default) if a table uses a slightly different format -
    e.g. a unicode prime (′) instead of a straight apostrophe, or extra
    whitespace.
    """
    if minute is None:
        return 99900
    numbers = re.findall(r"\d+", str(minute))
    if not numbers:
        return 99900
    base = int(numbers[0])
    extra = int(numbers[1]) if len(numbers) > 1 else 0
    return base * 100 + extra


def format_minute(minute) -> str:
    if minute is None:
        return ""
    text = str(minute).strip().rstrip("'′")
    return f"{text}'"


def humanize_column(col: str) -> str:
    """'gk_save_pct' -> 'Save Pct', 'shots_on_target' -> 'Shots On Target'.
    Strips a redundant 'gk_' prefix (used when the surrounding table/view
    already makes clear it's goalkeeper data) and title-cases the rest.
    """
    text = col[3:] if col.startswith("gk_") else col
    text = text.replace("_", " ").title()
    return "Player" if text == "Player Name" else text


def abbreviate_name(full_name: str) -> str:
    """'Bukayo Saka' -> 'B. Saka'. Splits on the first space only, so
    multi-word surnames ('Kevin De Bruyne' -> 'K. De Bruyne') stay intact.
    """
    if not full_name:
        return ""
    parts = full_name.strip().split(" ", 1)
    if len(parts) == 1:
        return parts[0]
    first, rest = parts
    return f"{first[0]}. {rest}"


_MIME_TYPES = {".png": "image/png", ".svg": "image/svg+xml"}


@st.cache_data(show_spinner=False)
def asset_data_uri(filename: str) -> str:
    """Base64-encode a local file from assets/ (goal.png, penalty-kick.png,
    shirt.svg, ...) so it can be dropped straight into custom HTML/markdown.
    Returns "" if the file isn't there, so callers can fall back gracefully
    instead of breaking the page.
    """
    path = ASSETS_DIR / filename
    if not path.exists():
        return ""
    mime = _MIME_TYPES.get(path.suffix.lower(), "application/octet-stream")
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"

def parse_int(value, default=None):
    """int(value), or default when value is missing or not an integer
    (query params come straight from the URL, so anything can be there)."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


# A VAR decision the review didn't confirm was overturned.
_OVERTURNED = {"goalAwarded": "Goal disallowed", "penaltyAwarded": "Penalty overturned"}


def humanize_class(value) -> str:
    """'goalAwarded' -> 'Goal awarded'."""
    words = re.sub(r"(?<!^)(?=[A-Z])", " ", str(value or "")).lower()
    return words.capitalize()


def var_label(incident_class, confirmed) -> str:
    """Live-feed VAR decision as text: 'goalAwarded' + confirmed=False ->
    'Goal disallowed'; otherwise the humanized class ('Goal awarded')."""
    if incident_class in _OVERTURNED and confirmed is not None and pd.notna(confirmed) and not bool(confirmed):
        return _OVERTURNED[incident_class]
    return humanize_class(incident_class)
