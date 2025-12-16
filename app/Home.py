import streamlit as st
import json
import os


def load_translations(lang_code):
    """Load translation file for the given language code."""
    file_path = os.path.join("app", "i18n", f"{lang_code}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Translation file not found: {file_path}")
        return {}


def t(key):
    """Get translated text for the given key."""
    translations = st.session_state.get("translations", {})
    return translations.get(key, key)


if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

if "page" not in st.session_state:
    st.session_state["page"] = t("nav_home")

st.session_state["translations"] = load_translations(st.session_state["lang"])

st.set_page_config(
    page_title=t("app_title"),
    page_icon="🏥",
    layout="wide"
)

st.title(t("app_title"))
st.subheader(t("tagline"))

st.divider()

language_options = {
    "English": "en",
    "हिन्दी": "hi"
}

selected_language = st.selectbox(
    t("choose_language"),
    options=list(language_options.keys()),
    index=0 if st.session_state["lang"] == "en" else 1
)

if language_options[selected_language] != st.session_state["lang"]:
    st.session_state["lang"] = language_options[selected_language]
    st.session_state["translations"] = load_translations(st.session_state["lang"])
    st.rerun()

with st.sidebar:
    st.header(t("nav_title"))
    
    page_options = [
        t("nav_home"),
        t("nav_hospital_finder"),
        t("nav_map_view"),
        t("nav_report_upload"),
        t("nav_scheme_advisor"),
        t("nav_volunteer_help")
    ]
    
    selected_page = st.radio(
        "",
        options=page_options,
        index=page_options.index(st.session_state["page"]) if st.session_state["page"] in page_options else 0
    )
    
    st.session_state["page"] = selected_page

st.info(t("demo_note"))