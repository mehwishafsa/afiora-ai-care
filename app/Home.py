import streamlit as st
import json
import os


def load_translations(lang_code: str) -> dict:
    """Load translation file for the given language code."""
    file_path = os.path.join("app", "i18n", f"{lang_code}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Translation file not found: {file_path}")
        return {}


def t(key: str) -> str:
    """Get translated text for the given key."""
    translations = st.session_state.get("translations", {})
    return translations.get(key, key)


# --- Session defaults (set BEFORE using t() for anything important) ---
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

# Load translations for current lang early
st.session_state["translations"] = load_translations(st.session_state["lang"])

# Use translated default page AFTER translations are loaded
if "page" not in st.session_state:
    st.session_state["page"] = t("nav_home")


st.set_page_config(
    page_title=t("app_title"),
    page_icon="🏥",
    layout="wide",
)

st.title(t("app_title"))
st.subheader(t("tagline"))
st.divider()

# --- Language Selector (top) ---
language_options = {
    "English": "en",
    "हिन्दी": "hi",
}

selected_language = st.selectbox(
    t("choose_language"),
    options=list(language_options.keys()),
    index=0 if st.session_state["lang"] == "en" else 1,
    key="lang_select",
)

new_lang = language_options[selected_language]

# Keep current page key stable across language switches
# (Map old page label -> page key -> new label)
page_key_by_label = {
    t("nav_home"): "nav_home",
    t("nav_hospital_finder"): "nav_hospital_finder",
    t("nav_map_view"): "nav_map_view",
    t("nav_report_upload"): "nav_report_upload",
    t("nav_scheme_advisor"): "nav_scheme_advisor",
    t("nav_volunteer_help"): "nav_volunteer_help",
}

if new_lang != st.session_state["lang"]:
    # Determine current page key (best effort)
    current_label = st.session_state.get("page", t("nav_home"))
    current_key = page_key_by_label.get(current_label, "nav_home")

    # Apply language + reload translations
    st.session_state["lang"] = new_lang
    st.session_state["translations"] = load_translations(st.session_state["lang"])

    # Set page label in new language
    st.session_state["page"] = t(current_key)
    st.rerun()

# --- Sidebar Navigation ---
with st.sidebar:
    st.header(t("nav_title"))

    page_options = [
        t("nav_home"),
        t("nav_hospital_finder"),
        t("nav_map_view"),
        t("nav_report_upload"),
        t("nav_scheme_advisor"),
        t("nav_volunteer_help"),
    ]

    # Ensure current page is valid
    current_page = st.session_state.get("page", t("nav_home"))
    if current_page not in page_options:
        current_page = page_options[0]
        st.session_state["page"] = current_page

    selected_page = st.radio(
        "Navigation",                  # ✅ non-empty label
        options=page_options,
        index=page_options.index(current_page),
        label_visibility="collapsed",  # ✅ hides label but keeps accessibility
        key="nav_radio",
    )

    st.session_state["page"] = selected_page

st.info(t("demo_note"))
