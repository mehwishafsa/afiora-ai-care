import streamlit as st
import json
from pathlib import Path

# ---------------- Fallback Data ----------------
def get_fallback_data():
    return {
        "learning_hub": [
            {
                "title": "Understanding Disabilities",
                "short_description": "Learn about different types of disabilities.",
                "step_by_step": [
                    "Step 1: Learn the basic types of disabilities.",
                    "Step 2: Understand accessibility needs.",
                    "Step 3: Learn communication tips."
                ],
                "do_and_dont": [
                    "Do respect personal space.",
                    "Do not assume abilities.",
                    "Do communicate clearly."
                ],
                "helpline_numbers": [
                    "1800-123-4567",
                    "1800-987-6543"
                ],
                "video_url": "",
                "image_url": ""
            },
            {
                "title": "Hospital Navigation",
                "short_description": "Guide PwD through hospital facilities.",
                "step_by_step": [
                    "Step 1: Help with form filling.",
                    "Step 2: Guide to different departments.",
                    "Step 3: Coordinate with staff for assistance."
                ],
                "do_and_dont": [
                    "Do be patient.",
                    "Do not rush them.",
                    "Do provide clear directions."
                ],
                "helpline_numbers": [
                    "1800-222-3333"
                ],
                "video_url": "",
                "image_url": ""
            }
        ]
    }

# ---------------- Load JSON Data ----------------
def load_learning_hub_data():
    data_path = Path("data/learning_hub.json")
    try:
        if not data_path.exists():
            return get_fallback_data()
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Validate minimal required keys
        for section in data.get("learning_hub", []):
            if not all(k in section for k in ["title", "short_description", "step_by_step", "do_and_dont"]):
                return get_fallback_data()
        return data
    except Exception:
        return get_fallback_data()

# ---------------- Accessibility Styles ----------------
def apply_accessibility_styles(font_size, high_contrast):
    size_map = {"Small": "14px", "Medium": "16px", "Large": "18px"}
    text_color = "#000000"
    bg_color = "#ffffff"
    if high_contrast:
        text_color = "#ffffff"
        bg_color = "#000000"

    css = f"""
    <style>
    html, body, [class*="css"] {{
        font-size: {size_map.get(font_size, "16px")};
        color: {text_color};
        background-color: {bg_color};
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ---------------- Streamlit Setup ----------------
st.set_page_config(page_title="Learning Hub – Afiora", layout="wide")

st.sidebar.header("Accessibility Settings")
font_size = st.sidebar.selectbox("Font Size", ["Small", "Medium", "Large"], index=1)
high_contrast = st.sidebar.toggle("High Contrast Mode", value=False)

apply_accessibility_styles(font_size, high_contrast)

st.title("Learning Hub – Afiora")
st.markdown("Simple step-by-step guides for PwD users and caregivers")

# Quick Actions
with st.container():
    st.subheader("Quick Actions")
    if st.button("Emergency Help"):
        st.markdown("**Emergency Number:** 112")
        st.markdown("**Ambulance:** 108")

    st.markdown("**Accessibility Checklist**")
    st.markdown(
        "- Carry disability ID if available\n"
        "- Ask for wheelchair or ramp support\n"
        "- Keep emergency contact saved\n"
        "- Don’t hesitate to ask hospital staff for help"
    )

# Load learning hub data
data = load_learning_hub_data()

# Display sections dynamically
for section in data.get("learning_hub", []):
    title = section.get("title", "No Title")
    with st.expander(title):
        st.markdown(section.get("short_description", ""))
        
        st.markdown("**Steps to follow:**")
        for step in section.get("step_by_step", []):
            st.markdown(f"- {step}")
        
        st.markdown("**Do and Don’t:**")
        for item in section.get("do_and_dont", []):
            st.markdown(f"- {item}")
        
        helplines = section.get("helpline_numbers", [])
        if helplines:
            st.markdown("**Helpline Numbers:**")
            for num in helplines:
                st.markdown(f"- {num}")
        
        # Display optional video/image
        video_url = section.get("video_url")
        image_url = section.get("image_url")
        if video_url:
            st.video(video_url)
        if image_url:
            st.image(image_url, use_column_width=True)
