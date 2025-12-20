import streamlit as st
import json
import os

# ----------------------------
# BASE DIRECTORY
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

# ----------------------------
# TRANSLATIONS
# ----------------------------
def load_translations(lang_code):
    file_path = os.path.join(DATA_DIR, f"{lang_code}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Translation file not found: {file_path}")
        return {}

def t(key):
    translations = st.session_state.get("translations", {})
    return translations.get(key, key)

# ----------------------------
# SESSION STATE DEFAULTS
# ----------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

st.session_state["translations"] = load_translations(st.session_state["lang"])

if "page" not in st.session_state:
    st.session_state["page"] = t("nav_home")

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title=t("app_title"),
    page_icon="🏥",
    layout="wide"
)

# ----------------------------
# LEARNING HUB DATA
# ----------------------------
def load_learning_hub():
    file_path = os.path.join(DATA_DIR, "learning_hub.json")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f).get("learning_hub", [])
    except FileNotFoundError:
        st.error(f"Learning hub file not found: {file_path}")
        return []

learning_hub = load_learning_hub()

# ----------------------------
# HEADER
# ----------------------------
st.title(t("app_title"))
st.subheader(t("tagline"))
st.divider()

# ----------------------------
# LANGUAGE SELECTOR
# ----------------------------
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

# ----------------------------
# SIDEBAR NAVIGATION
# ----------------------------
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
        index=page_options.index(st.session_state["page"])
        if st.session_state["page"] in page_options else 0
    )

    st.session_state["page"] = selected_page

# ----------------------------
# INFO NOTE
# ----------------------------
st.info(t("demo_note"))

# ----------------------------
# HOME PAGE
# ----------------------------
if selected_page == t("nav_home"):
    st.header(t("nav_home"))

    for section in learning_hub:
        st.subheader(section.get("title", ""))
        st.write(section.get("short_description", ""))

        st.markdown("**Step by Step**")
        for step in section.get("step_by_step", []):
            st.write(f"- {step}")

        st.markdown("**Do's and Don'ts**")
        for item in section.get("do_and_dont", []):
            st.write(f"- {item}")

        if section.get("helpline_numbers"):
            st.markdown("**Helpline Numbers**")
            for number in section["helpline_numbers"]:
                st.write(f"- {number}")

        st.divider()
