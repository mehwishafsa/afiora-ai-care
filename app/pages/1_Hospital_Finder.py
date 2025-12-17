import streamlit as st
import json
import os

def load_translations(lang):
    try:
        path = os.path.join("app", "i18n", f"{lang}.json")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

translations = load_translations(st.session_state["lang"])

def t(key):
    return translations.get(key, key)

st.set_page_config(page_title=t("nav_hospital_finder"), page_icon="🏥")

st.title(t("nav_hospital_finder"))

location = st.text_input(t("location") if "location" in translations else "Location", value="Hyderabad, Telangana")

st.subheader(t("accessibility_features") if "accessibility_features" in translations else "Accessibility Features")

filter_ramp = st.checkbox(t("ramp") if "ramp" in translations else "Ramp")
filter_lift = st.checkbox(t("lift") if "lift" in translations else "Lift")
filter_toilet = st.checkbox(t("accessible_toilet") if "accessible_toilet" in translations else "Accessible Toilet")
filter_sign = st.checkbox(t("sign_language") if "sign_language" in translations else "Sign Language Support")

search_clicked = st.button(t("search") if "search" in translations else "Search")

demo_hospitals = [
    {
        "name": "Apollo Hospital",
        "distance_km": 3.2,
        "ramp": True,
        "lift": True,
        "accessible_toilet": True,
        "sign_language": True,
        "score": 95
    },
    {
        "name": "Care Hospital",
        "distance_km": 5.8,
        "ramp": True,
        "lift": True,
        "accessible_toilet": False,
        "sign_language": False,
        "score": 75
    },
    {
        "name": "Yashoda Hospital",
        "distance_km": 7.5,
        "ramp": True,
        "lift": False,
        "accessible_toilet": True,
        "sign_language": True,
        "score": 85
    }
]

if search_clicked:
    filtered = []
    for h in demo_hospitals:
        if filter_ramp and not h["ramp"]:
            continue
        if filter_lift and not h["lift"]:
            continue
        if filter_toilet and not h["accessible_toilet"]:
            continue
        if filter_sign and not h["sign_language"]:
            continue
        filtered.append(h)
    
    if filtered:
        st.success(f"{t('found') if 'found' in translations else 'Found'} {len(filtered)} {t('hospitals') if 'hospitals' in translations else 'hospital(s)'}")
        for h in filtered:
            with st.expander(f"{h['name']} - {h['distance_km']} km"):
                st.write(f"**{t('score') if 'score' in translations else 'Score'}:** {h['score']}/100")
                st.write(f"**{t('ramp') if 'ramp' in translations else 'Ramp'}:** {'✅' if h['ramp'] else '❌'}")
                st.write(f"**{t('lift') if 'lift' in translations else 'Lift'}:** {'✅' if h['lift'] else '❌'}")
                st.write(f"**{t('accessible_toilet') if 'accessible_toilet' in translations else 'Accessible Toilet'}:** {'✅' if h['accessible_toilet'] else '❌'}")
                st.write(f"**{t('sign_language') if 'sign_language' in translations else 'Sign Language'}:** {'✅' if h['sign_language'] else '❌'}")
    else:
        st.warning(t("no_results") if "no_results" in translations else "No hospitals match your criteria")
    
    st.info(t("demo_note") if "demo_note" in translations else "Demo-safe: works even without datasets")