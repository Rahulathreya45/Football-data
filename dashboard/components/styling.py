from pathlib import Path

import streamlit as st


def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "theme.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def fix_history_navigation():
    """Workarounds for Streamlit's multipage browser-history bugs, which made
    browser back show "No team selected"/"No match selected":

    1. switch_page/page_link with query_params push two history entries -
       the new query on the *old* path (/team?match_id=...), then the real
       one - and pages setting st.query_params push extra entries too. So
       only the first pushState after a user click/keypress creates an
       entry; follow-up pushes replace it.
    2. On back/forward Streamlit reruns the page from the URL path with the
       *previous* page's query params. The address bar is already right
       when popstate fires, so a capture-phase listener (runs before
       Streamlit's own listener on window) stops Streamlit's handler and
       reloads that URL instead.

    Registered once per browser tab."""
    st.html(
        """
        <script>
        if (!window.__footballHistoryFix) {
            window.__footballHistoryFix = true;

            let userNavPending = false;
            document.addEventListener("click", () => { userNavPending = true; }, true);
            document.addEventListener("keydown", (e) => {
                if (e.key === "Enter" || e.key === " ") userNavPending = true;
            }, true);

            const pushState = window.history.pushState.bind(window.history);
            window.history.pushState = (state, title, url) => {
                if (userNavPending) {
                    userNavPending = false;
                    return pushState(state, title, url);
                }
                return window.history.replaceState(state, title, url);
            };

            window.addEventListener("popstate", (event) => {
                event.stopImmediatePropagation();
                window.location.reload();
            }, { capture: true });
        }
        </script>
        """,
        unsafe_allow_javascript=True,
    )
