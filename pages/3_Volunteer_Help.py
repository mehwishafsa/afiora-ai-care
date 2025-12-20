import streamlit as st
import json
import os
import math

def load_translations(lang):
    try:
        path = os.path.join("app", "i18n", f"{lang}.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

lang = st.session_state.get("lang", "en")
translations = load_translations(lang)

fallback_labels = {
    "nav_volunteer_help": "Volunteer Help",
    "name": "Name",
    "phone": "Phone",
    "location": "Location",
    "help_type": "Help Type",
    "urgency": "Urgency",
    "notes": "Notes",
    "find_volunteers": "Find volunteers",
    "demo_note": "Demo-safe: works without backend"
}

def t(key):
    return translations.get(key, fallback_labels.get(key, key))

st.set_page_config(page_title=t("nav_volunteer_help"), page_icon="🤝")

st.title(t("nav_volunteer_help"))
st.write("Request nearby verified volunteer support (Demo).")

demo_volunteers = [
    {
        "name": "Rajesh Kumar",
        "skills": ["Wheelchair assistance", "General support"],
        "area": "Hitech City",
        "availability": True,
        "distance_km": 2.3,
        "verified": True
    },
    {
        "name": "Priya Sharma",
        "skills": ["Guiding blind user", "Sign language support"],
        "area": "Gachibowli",
        "availability": True,
        "distance_km": 3.8,
        "verified": True
    },
    {
        "name": "Mohammed Ali",
        "skills": ["Sign language support", "General support"],
        "area": "Madhapur",
        "availability": False,
        "distance_km": 4.1,
        "verified": True
    },
    {
        "name": "Lakshmi Reddy",
        "skills": ["Wheelchair assistance", "Guiding blind user"],
        "area": "Kondapur",
        "availability": True,
        "distance_km": 5.2,
        "verified": True
    },
    {
        "name": "Amit Patel",
        "skills": ["General support", "Wheelchair assistance"],
        "area": "Jubilee Hills",
        "availability": True,
        "distance_km": 6.5,
        "verified": True
    }
]

with st.form("volunteer_form"):
    user_name = st.text_input(t("name"), value="")
    
    phone = st.text_input(t("phone") + " (optional)", value="")
    
    location = st.text_input(t("location"), value="Hyderabad, Telangana")
    
    help_type = st.selectbox(
        t("help_type"),
        ["Wheelchair assistance", "Guiding blind user", "Sign language support", "General support"]
    )
    
    urgency = st.selectbox(
        t("urgency"),
        ["Normal", "Urgent"]
    )
    
    notes = st.text_area(t("notes"), value="")
    
    submitted = st.form_submit_button(t("find_volunteers"))

if submitted:
    filtered_volunteers = []
    
    for vol in demo_volunteers:
        if vol["availability"] and help_type in vol["skills"]:
            filtered_volunteers.append(vol)
    
    filtered_volunteers.sort(key=lambda x: x["distance_km"])
    
    if not filtered_volunteers:
        if lang == "hi":
            st.warning("कोई उपलब्ध स्वयंसेवक नहीं मिला। कृपया बाद में पुनः प्रयास करें या सामान्य सहायता चुनें।")
        else:
            st.warning("No available volunteers found. Please try again later or choose General support.")
    else:
        top_volunteers = filtered_volunteers[:3]
        
        if lang == "hi":
            st.success(f"{len(top_volunteers)} स्वयंसेवक मिले!")
            
            for vol in top_volunteers:
                with st.expander(f"✅ {vol['name']} - {vol['area']} ({vol['distance_km']} km)"):
                    st.write(f"**सत्यापित स्वयंसेवक:** {'✓' if vol['verified'] else '✗'}")
                    st.write(f"**कौशल:** {', '.join(vol['skills'])}")
                    st.write(f"**क्षेत्र:** {vol['area']}")
                    st.write(f"**दूरी:** {vol['distance_km']} km")
                    
                    st.markdown("---")
                    st.write("**सुझाया गया संदेश:**")
                    message = f"नमस्ते {vol['name']}, मुझे {help_type} के लिए सहायता चाहिए। स्थान: {location}. क्या आप मदद कर सकते हैं?"
                    if urgency == "Urgent":
                        message += " (तत्काल आवश्यक)"
                    st.code(message, language=None)
        else:
            st.success(f"Found {len(top_volunteers)} volunteer(s)!")
            
            for vol in top_volunteers:
                with st.expander(f"✅ {vol['name']} - {vol['area']} ({vol['distance_km']} km)"):
                    st.write(f"**Verified Volunteer:** {'✓' if vol['verified'] else '✗'}")
                    st.write(f"**Skills:** {', '.join(vol['skills'])}")
                    st.write(f"**Area:** {vol['area']}")
                    st.write(f"**Distance:** {vol['distance_km']} km")
                    
                    st.markdown("---")
                    st.write("**Suggested message:**")
                    message = f"Hi {vol['name']}, I need help with {help_type}. Location: {location}. Can you assist?"
                    if urgency == "Urgent":
                        message += " (Urgent)"
                    st.code(message, language=None)

st.markdown("---")

if lang == "hi":
    st.subheader("स्वयंसेवक सत्यापन कैसे काम करता है (डेमो)")
    st.markdown("""
    - सभी स्वयंसेवकों की पृष्ठभूमि जांच की जाती है
    - पहचान और कौशल प्रमाण पत्र सत्यापित किए जाते हैं
    - नियमित प्रशिक्षण और फीडबैक प्रणाली बनाए रखी जाती है
    """)
else:
    st.subheader("How volunteer verification works (demo)")
    st.markdown("""
    - All volunteers undergo background checks
    - Identity and skill certificates are verified
    - Regular training and feedback system maintained
    """)

st.info(t("demo_note"))