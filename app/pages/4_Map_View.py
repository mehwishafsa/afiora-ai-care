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
    "nav_map_view": "Accessibility Map View",
    "location": "Location",
    "show_hospitals": "Show Hospitals",
    "show_barriers": "Show Barriers",
    "show_volunteers": "Show Volunteers",
    "ramp": "Ramp",
    "lift": "Lift",
    "accessible_toilet": "Accessible Toilet",
    "sign_language": "Sign Language Support",
    "min_score": "Minimum Accessibility Score",
    "demo_note": "Demo-safe: works without external APIs"
}

def t(key):
    return translations.get(key, fallback_labels.get(key, key))

st.set_page_config(page_title=t("nav_map_view"), page_icon="🗺️", layout="wide")

st.title(t("nav_map_view"))
st.write("View hospitals, accessibility features, barriers, and volunteers (Demo).")

demo_hospitals = [
    {"name": "Apollo Hospital", "lat": 17.4435, "lon": 78.3772, "ramp": True, "lift": True, "accessible_toilet": True, "sign_language": True, "score": 95},
    {"name": "Care Hospital", "lat": 17.4239, "lon": 78.4738, "ramp": True, "lift": True, "accessible_toilet": False, "sign_language": False, "score": 75},
    {"name": "Yashoda Hospital", "lat": 17.4399, "lon": 78.4983, "ramp": True, "lift": False, "accessible_toilet": True, "sign_language": True, "score": 85},
    {"name": "Continental Hospital", "lat": 17.4301, "lon": 78.3420, "ramp": False, "lift": True, "accessible_toilet": True, "sign_language": False, "score": 70},
    {"name": "KIMS Hospital", "lat": 17.4504, "lon": 78.3808, "ramp": True, "lift": True, "accessible_toilet": True, "sign_language": False, "score": 80}
]

demo_barriers = [
    {"type": "Blocked Ramp", "lat": 17.4385, "lon": 78.3915, "severity": "High"},
    {"type": "Broken Lift", "lat": 17.4289, "lon": 78.4585, "severity": "Medium"},
    {"type": "Missing Tactile Paving", "lat": 17.4412, "lon": 78.4821, "severity": "Low"},
    {"type": "Narrow Doorway", "lat": 17.4358, "lon": 78.3598, "severity": "Medium"}
]

demo_volunteers = [
    {"name": "Rajesh Kumar", "skill": "Wheelchair assistance", "lat": 17.4425, "lon": 78.3812, "available": True},
    {"name": "Priya Sharma", "skill": "Sign language", "lat": 17.4279, "lon": 78.4668, "available": True},
    {"name": "Mohammed Ali", "skill": "Guiding", "lat": 17.4389, "lon": 78.4923, "available": False},
    {"name": "Lakshmi Reddy", "skill": "General support", "lat": 17.4321, "lon": 78.3480, "available": True}
]

st.subheader("🔍 Filters" if lang != "hi" else "🔍 फ़िल्टर")

location = st.text_input(t("location"), value="Hyderabad, Telangana")

col1, col2, col3 = st.columns(3)
with col1:
    show_hospitals = st.checkbox(t("show_hospitals"), value=True)
with col2:
    show_barriers = st.checkbox(t("show_barriers"), value=True)
with col3:
    show_volunteers = st.checkbox(t("show_volunteers"), value=True)

if show_hospitals:
    st.write("**Hospital Features:**" if lang != "hi" else "**अस्पताल सुविधाएं:**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        filter_ramp = st.checkbox(t("ramp"), value=False)
    with col2:
        filter_lift = st.checkbox(t("lift"), value=False)
    with col3:
        filter_toilet = st.checkbox(t("accessible_toilet"), value=False)
    with col4:
        filter_sign = st.checkbox(t("sign_language"), value=False)
    
    min_score = st.slider(t("min_score"), min_value=0, max_value=100, value=50)
else:
    filter_ramp = False
    filter_lift = False
    filter_toilet = False
    filter_sign = False
    min_score = 0

filtered_hospitals = []
if show_hospitals:
    for h in demo_hospitals:
        if h["score"] < min_score:
            continue
        if filter_ramp and not h["ramp"]:
            continue
        if filter_lift and not h["lift"]:
            continue
        if filter_toilet and not h["accessible_toilet"]:
            continue
        if filter_sign and not h["sign_language"]:
            continue
        filtered_hospitals.append(h)

filtered_barriers = demo_barriers if show_barriers else []
filtered_volunteers = [v for v in demo_volunteers if v["available"]] if show_volunteers else []

st.markdown("---")

if lang == "hi":
    st.subheader("📌 लीजेंड")
    st.markdown("""
    - 🏥 **अस्पताल**: पहुंच सुविधाओं के साथ स्वास्थ्य सुविधाएं
    - 🚧 **बाधाएं**: सूचित की गई पहुंच संबंधी समस्याएं
    - 🤝 **स्वयंसेवक**: उपलब्ध सहायता प्रदाता
    """)
else:
    st.subheader("📌 Legend")
    st.markdown("""
    - 🏥 **Hospitals**: Healthcare facilities with accessibility features
    - 🚧 **Barriers**: Reported accessibility issues
    - 🤝 **Volunteers**: Available support providers
    """)

st.subheader("🗺️ Map Data (Demo)" if lang != "hi" else "🗺️ मानचित्र डेटा (डेमो)")

map_data = []

for h in filtered_hospitals:
    features = []
    if h["ramp"]:
        features.append("Ramp" if lang != "hi" else "रैंप")
    if h["lift"]:
        features.append("Lift" if lang != "hi" else "लिफ्ट")
    if h["accessible_toilet"]:
        features.append("Toilet" if lang != "hi" else "शौचालय")
    if h["sign_language"]:
        features.append("Sign Lang" if lang != "hi" else "संकेत भाषा")
    
    map_data.append({
        "Layer": "Hospital" if lang != "hi" else "अस्पताल",
        "Name/Type": h["name"],
        "Latitude": h["lat"],
        "Longitude": h["lon"],
        "Details": f"Score: {h['score']}, Features: {', '.join(features)}" if lang != "hi" else f"स्कोर: {h['score']}, सुविधाएं: {', '.join(features)}"
    })

for b in filtered_barriers:
    map_data.append({
        "Layer": "Barrier" if lang != "hi" else "बाधा",
        "Name/Type": b["type"],
        "Latitude": b["lat"],
        "Longitude": b["lon"],
        "Details": f"Severity: {b['severity']}" if lang != "hi" else f"गंभीरता: {b['severity']}"
    })

for v in filtered_volunteers:
    map_data.append({
        "Layer": "Volunteer" if lang != "hi" else "स्वयंसेवक",
        "Name/Type": v["name"],
        "Latitude": v["lat"],
        "Longitude": v["lon"],
        "Details": f"Skill: {v['skill']}" if lang != "hi" else f"कौशल: {v['skill']}"
    })

if map_data:
    st.dataframe(map_data, use_container_width=True)
    
    try:
        chart_data = []
        for item in map_data:
            chart_data.append({"lat": item["Latitude"], "lon": item["Longitude"]})
        
        st.map(chart_data)
    except Exception as e:
        st.info("Map visualization unavailable in this demo environment." if lang != "hi" else "इस डेमो में मानचित्र दृश्य उपलब्ध नहीं है।")
else:
    st.info("No data to display with current filters." if lang != "hi" else "वर्तमान फ़िल्टर के साथ कोई डेटा प्रदर्शित करने के लिए नहीं।")

st.markdown("---")

if lang == "hi":
    st.subheader("💡 नजदीकी जानकारी")
    
    if filtered_hospitals:
        sorted_hospitals = sorted(filtered_hospitals, key=lambda x: x["score"], reverse=True)
        top_hospitals = sorted_hospitals[:3]
        
        st.write(f"**शीर्ष {len(top_hospitals)} अस्पताल:**")
        for h in top_hospitals:
            with st.expander(f"{h['name']} - स्कोर: {h['score']}"):
                st.write(f"**रैंप:** {'✅' if h['ramp'] else '❌'}")
                st.write(f"**लिफ्ट:** {'✅' if h['lift'] else '❌'}")
                st.write(f"**सुलभ शौचालय:** {'✅' if h['accessible_toilet'] else '❌'}")
                st.write(f"**संकेत भाषा:** {'✅' if h['sign_language'] else '❌'}")
    
    st.write(f"**सूचित बाधाएं:** {len(filtered_barriers)}")
    st.write(f"**उपलब्ध स्वयंसेवक:** {len(filtered_volunteers)}")
    
else:
    st.subheader("💡 Nearby Insights")
    
    if filtered_hospitals:
        sorted_hospitals = sorted(filtered_hospitals, key=lambda x: x["score"], reverse=True)
        top_hospitals = sorted_hospitals[:3]
        
        st.write(f"**Top {len(top_hospitals)} Hospitals:**")
        for h in top_hospitals:
            with st.expander(f"{h['name']} - Score: {h['score']}"):
                st.write(f"**Ramp:** {'✅' if h['ramp'] else '❌'}")
                st.write(f"**Lift:** {'✅' if h['lift'] else '❌'}")
                st.write(f"**Accessible Toilet:** {'✅' if h['accessible_toilet'] else '❌'}")
                st.write(f"**Sign Language:** {'✅' if h['sign_language'] else '❌'}")
    
    st.write(f"**Reported Barriers:** {len(filtered_barriers)}")
    st.write(f"**Available Volunteers:** {len(filtered_volunteers)}")

st.info("Demo-safe: real Telangana hospital coordinates and layers will be plugged in from geo module." if lang != "hi" else "डेमो-सुरक्षित: वास्तविक तेलंगाना अस्पताल निर्देशांक और परतें भू मॉड्यूल से जोड़ी जाएंगी।")