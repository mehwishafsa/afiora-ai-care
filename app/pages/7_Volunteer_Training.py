import streamlit as st
import json
import os

st.set_page_config(
    page_title="Volunteer Training",
    layout="centered"
)

st.title("Volunteer Readiness Training")
st.write("This training helps volunteers assist PwD effectively.")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "app", "data", "volunteer_training.json")

try:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not data.get("modules"):
        st.warning("No training modules found")

    for module in data["modules"]:
        st.subheader(module["title"])
        st.write(module["description"])

except Exception as e:
    st.error("Error loading training content")
    st.code(str(e))
