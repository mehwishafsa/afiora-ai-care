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

lang = st.session_state.get("lang", "en")
translations = load_translations(lang)

fallback_labels = {
    "nav_scheme_advisor": "Scheme Advisor",
    "age": "Age",
    "disability_type": "Disability Type",
    "disability_percent": "Disability Percentage",
    "income_range": "Income Range",
    "student_status": "Student Status",
    "state": "State",
    "check_schemes": "Check possible schemes",
    "demo_note": "Demo-safe: works without AI modules"
}

def t(key):
    return translations.get(key, fallback_labels.get(key, key))

st.set_page_config(page_title=t("nav_scheme_advisor"), page_icon="📋")

st.title(t("nav_scheme_advisor"))
st.write("Check possible schemes for PwD students (Demo-safe).")

with st.form("scheme_form"):
    age = st.number_input(t("age"), min_value=10, max_value=60, value=19)
    
    disability_type = st.selectbox(
        t("disability_type"),
        ["Locomotive", "Visual", "Hearing", "Speech", "Multiple"]
    )
    
    disability_percent = st.slider(
        t("disability_percent"),
        min_value=0,
        max_value=100,
        value=60
    )
    
    income_range = st.selectbox(
        t("income_range"),
        ["<1L", "1L-3L", "3L-5L", ">5L"]
    )
    
    student_status = st.selectbox(
        t("student_status"),
        ["School", "Diploma", "B.Tech", "PG"]
    )
    
    state = st.text_input(t("state"), value="Telangana")
    
    submitted = st.form_submit_button(t("check_schemes"))

if submitted:
    profile = {
        "age": age,
        "disability_type": disability_type,
        "disability_percent": disability_percent,
        "income_range": income_range,
        "student_status": student_status,
        "state": state
    }
    
    if lang == "hi":
        st.subheader("📝 प्रोफ़ाइल सारांश")
        st.markdown(f"""
        - **आयु:** {profile['age']} वर्ष
        - **विकलांगता प्रकार:** {profile['disability_type']}
        - **विकलांगता प्रतिशत:** {profile['disability_percent']}%
        - **आय सीमा:** {profile['income_range']}
        - **छात्र स्थिति:** {profile['student_status']}
        - **राज्य:** {profile['state']}
        """)
        
        st.subheader("🎯 संभावित योजनाएं")
        
        st.markdown("#### राष्ट्रीय योजनाएं")
        st.markdown("""
        **1. प्रधानमंत्री छात्रवृत्ति योजना (विकलांग छात्रों के लिए)**
        - शैक्षिक खर्च के लिए वित्तीय सहायता
        - पात्रता: 40% या अधिक विकलांगता
        - आय सीमा: 2.5 लाख प्रति वर्ष तक
        - लाभ: ₹10,000 - ₹50,000 प्रति वर्ष
        
        **2. दीनदयाल विकलांग पुनर्वास योजना**
        - कौशल विकास और प्रशिक्षण
        - रोजगार सहायता और मार्गदर्शन
        - सभी प्रकार की विकलांगताओं के लिए
        - आयु सीमा: 18-60 वर्ष
        """)
        
        if profile['state'].lower() == "telangana":
            st.markdown("#### तेलंगाना राज्य योजना")
            st.markdown("""
            **3. आसरा पेंशन योजना (विकलांग व्यक्तियों के लिए)**
            - मासिक वित्तीय सहायता: ₹3,016
            - पात्रता: 18+ वर्ष, 40%+ विकलांगता
            - परिवार की आय: 1.5 लाख से कम
            - सीधे बैंक खाते में भुगतान
            """)
        
        st.subheader("📄 आवश्यक दस्तावेज़")
        st.markdown("""
        - विकलांगता प्रमाण पत्र (40% या अधिक)
        - आधार कार्ड
        - आय प्रमाण पत्र
        - निवास प्रमाण पत्र
        - शैक्षिक प्रमाण पत्र (मार्कशीट/प्रमाण पत्र)
        - बैंक खाता विवरण (पासबुक की कॉपी)
        - पासपोर्ट साइज फोटो
        """)
        
        st.subheader("🚀 आवेदन कैसे करें")
        st.markdown("""
        **चरण 1:** नजदीकी जिला समाज कल्याण कार्यालय जाएं
        
        **चरण 2:** सभी आवश्यक दस्तावेज़ एकत्र करें
        
        **चरण 3:** आवेदन फॉर्म भरें (ऑनलाइन या ऑफलाइन)
        
        **चरण 4:** दस्तावेज़ जमा करें और सत्यापन की प्रतीक्षा करें
        
        **चरण 5:** स्वीकृति के बाद लाभ प्राप्त करना शुरू करें
        """)
        
        st.subheader("⚠️ पुष्टि करने योग्य बातें")
        st.markdown("""
        **अस्वीकरण:** यह केवल सामान्य मार्गदर्शन है। अंतिम पात्रता सरकारी नियमों पर निर्भर करती है।
        
        **कृपया पुष्टि करें:**
        - नवीनतम योजना दिशानिर्देश आधिकारिक वेबसाइट से
        - अपने क्षेत्र में लागू विशिष्ट पात्रता मानदंड
        - आवेदन की समय सीमा और प्रक्रिया
        - आवश्यक दस्तावेज़ों की पूर्णता
        """)
        
    else:
        st.subheader("📝 Profile Summary")
        st.markdown(f"""
        - **Age:** {profile['age']} years
        - **Disability Type:** {profile['disability_type']}
        - **Disability Percentage:** {profile['disability_percent']}%
        - **Income Range:** {profile['income_range']}
        - **Student Status:** {profile['student_status']}
        - **State:** {profile['state']}
        """)
        
        st.subheader("🎯 Possible Schemes")
        
        st.markdown("#### National Schemes")
        st.markdown("""
        **1. Prime Minister Scholarship Scheme (for PwD Students)**
        - Financial assistance for educational expenses
        - Eligibility: 40% or more disability
        - Income limit: up to 2.5 lakhs per annum
        - Benefit: ₹10,000 - ₹50,000 per year
        
        **2. Deen Dayal Disability Rehabilitation Scheme**
        - Skill development and training programs
        - Employment assistance and guidance
        - For all types of disabilities
        - Age limit: 18-60 years
        """)
        
        if profile['state'].lower() == "telangana":
            st.markdown("#### Telangana State Scheme")
            st.markdown("""
            **3. Aasara Pension Scheme (for Persons with Disabilities)**
            - Monthly financial assistance: ₹3,016
            - Eligibility: 18+ years, 40%+ disability
            - Family income: below 1.5 lakhs
            - Direct bank transfer payment
            """)
        
        st.subheader("📄 Documents Usually Needed")
        st.markdown("""
        - Disability certificate (40% or above)
        - Aadhaar card
        - Income certificate
        - Residence proof
        - Educational certificates (mark sheets/degree)
        - Bank account details (passbook copy)
        - Passport size photographs
        """)
        
        st.subheader("🚀 How to Apply")
        st.markdown("""
        **Step 1:** Visit nearest District Social Welfare Office
        
        **Step 2:** Collect all required documents
        
        **Step 3:** Fill application form (online or offline)
        
        **Step 4:** Submit documents and wait for verification
        
        **Step 5:** Start receiving benefits after approval
        """)
        
        st.subheader("⚠️ What to Confirm")
        st.markdown("""
        **Disclaimer:** This is general guidance only. Final eligibility depends on official government rules.
        
        **Please confirm:**
        - Latest scheme guidelines from official websites
        - Specific eligibility criteria applicable in your area
        - Application deadlines and procedures
        - Completeness of required documentation
        """)
    
    st.info("Guidance only; verify with official sources.")

st.info(t("demo_note"))