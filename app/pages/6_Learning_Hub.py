import streamlit as st
import json
from pathlib import Path


def get_fallback_data():
    return {
        "Preparing for a Hospital Visit": {
            "short_description": "Preparing in advance can make hospital visits less stressful and more comfortable.",
            "step_by_step": [
                "Carry all medical records and prescriptions",
                "Keep emergency contact numbers ready",
                "Arrive early to avoid rush",
                "Inform staff about any specific support you need"
            ],
            "do_and_dont": [
                "Do ask for assistance if needed",
                "Do keep important documents in one folder",
                "Don’t hesitate to explain your needs",
                "Don’t skip meals or medicines before visiting"
            ],
            "helpline_numbers": []
        },
        "Disability Rights (India)": {
            "short_description": "Persons with Disabilities have legal rights to equal access and dignity in healthcare.",
            "step_by_step": [
                "Know your rights under the RPwD Act, 2016",
                "Ask for accessible facilities in hospitals",
                "Report discrimination if it occurs"
            ],
            "do_and_dont": [
                "Do carry disability ID if available",
                "Do speak up if facilities are inaccessible",
                "Don’t accept denial of basic services",
                "Don’t hesitate to seek help from authorities"
            ],
            "helpline_numbers": ["1800-599-0019"]
        },
        "Healthcare Schemes – Basics": {
            "short_description": "Government healthcare schemes can reduce medical expenses for PwD.",
            "step_by_step": [
                "Check eligibility for schemes like Ayushman Bharat",
                "Keep Aadhaar and disability certificate ready",
                "Apply through official portals or help desks"
            ],
            "do_and_dont": [
                "Do verify scheme details from official sources",
                "Do keep copies of submitted documents",
                "Don’t rely on unofficial agents",
                "Don’t share personal details unnecessarily"
            ],
            "helpline_numbers": ["14555"]
        },
        "Emergency Tips": {
            "short_description": "Quick action during emergencies can save lives.",
            "step_by_step": [
                "Call emergency services immediately",
                "Stay calm and follow instructions",
                "Inform caregivers or family members"
            ],
            "do_and_dont": [
                "Do keep emergency numbers saved",
                "Do provide clear location details",
                "Don’t panic",
                "Don’t delay calling for help"
            ],
            "helpline_numbers": ["112", "108"]
        },
        "Accessibility Inside Hospitals": {
            "short_description": "Hospitals should provide accessible infrastructure and support.",
            "step_by_step": [
                "Ask for ramps, lifts, or wheelchairs",
                "Request priority seating if required",
                "Seek assistance from hospital staff"
            ],
            "do_and_dont": [
                "Do ask for reasonable accommodation",
                "Do report broken accessibility features",
                "Don’t struggle alone",
                "Don’t feel embarrassed asking for help"
            ],
            "helpline_numbers": []
        }
    }


def load_learning_hub_data():
    data_path = Path("data/learning_hub.json")
    try:
        if not data_path.exists():
            return get_fallback_data()
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        required_keys = {"short_description", "step_by_step", "do_and_dont"}
        for section, content in data.items():
            if not required_keys.issubset(content.keys()):
                return get_fallback_data()
        return data
    except Exception:
        return get_fallback_data()


def apply_accessibility_styles(font_size, high_contrast):
    size_map = {
        "Small": "14px",
        "Medium": "16px",
        "Large": "18px"
    }
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


st.set_page_config(page_title="Learning Hub – Afiora", layout="wide")

st.sidebar.header("Accessibility Settings")
font_size = st.sidebar.selectbox("Font Size", ["Small", "Medium", "Large"], index=1)
high_contrast = st.sidebar.toggle("High Contrast Mode", value=False)

apply_accessibility_styles(font_size, high_contrast)

st.title("Learning Hub – Afiora")
st.markdown("Simple step-by-step guides for PwD users and caregivers")

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

data = load_learning_hub_data()

for section_title in [
    "Preparing for a Hospital Visit",
    "Disability Rights (India)",
    "Healthcare Schemes – Basics",
    "Emergency Tips",
    "Accessibility Inside Hospitals"
]:
    content = data.get(section_title, {})
    with st.expander(section_title):
        st.markdown(content.get("short_description", ""))
        st.markdown("**Steps to follow:**")
        for step in content.get("step_by_step", []):
            st.markdown(f"- {step}")
        st.markdown("**Do and Don’t:**")
        for item in content.get("do_and_dont", []):
            st.markdown(f"- {item}")
        helplines = content.get("helpline_numbers", [])
        if helplines:
            st.markdown("**Helpline Numbers:**")
            for num in helplines:
                st.markdown(f"- {num}")
