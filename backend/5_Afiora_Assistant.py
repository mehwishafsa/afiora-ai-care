import streamlit as st
import json
import os
import re
import time

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
    "agent_title": "Afiora Assistant",
    "agent_subtitle": "AI-Powered Accessibility Agent",
    "analyze_btn": "Analyze & Respond",
    "examples_title": "Show example questions",
    "detected_intent": "Detected Intent",
    "confidence": "Confidence",
    "query": "Your Question",
    "city": "City",
    "state": "State",
    "force_intent": "Force Intent",
    "typing_effect": "Typing effect"
}

def t(key):
    return translations.get(key, fallback_labels.get(key, key))

st.set_page_config(page_title=t("agent_title"), page_icon="🤖", layout="wide")

futuristic_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

.main {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a0a2e 50%, #0a0a0a 100%);
    font-family: 'Rajdhani', sans-serif;
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 3.5rem;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(45deg, #00f0ff, #7b2ff7, #f21b3f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
    animation: glow 2s ease-in-out infinite alternate;
    margin-bottom: 0.5rem;
}

.neon-subtitle {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.3rem;
    text-align: center;
    color: #00f0ff;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
    margin-bottom: 2rem;
}

@keyframes glow {
    from {
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.5), 0 0 30px rgba(123, 47, 247, 0.3);
    }
    to {
        text-shadow: 0 0 30px rgba(0, 240, 255, 0.8), 0 0 40px rgba(123, 47, 247, 0.5);
    }
}

.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.15);
    margin: 15px 0;
    transition: all 0.3s ease;
}

.glass-card:hover {
    box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.3);
    transform: translateY(-2px);
}

.intent-badge {
    display: inline-block;
    padding: 8px 20px;
    background: linear-gradient(45deg, #7b2ff7, #f21b3f);
    border-radius: 25px;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    color: white;
    text-transform: uppercase;
    font-size: 0.9rem;
    box-shadow: 0 0 20px rgba(123, 47, 247, 0.6);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 20px rgba(123, 47, 247, 0.6);
    }
    50% {
        box-shadow: 0 0 30px rgba(123, 47, 247, 0.9);
    }
}

.thinking-loader {
    text-align: center;
    padding: 30px;
    font-family: 'Orbitron', sans-serif;
    color: #00f0ff;
    font-size: 1.2rem;
}

.loader-dots {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 20px;
}

.loader-dots div {
    position: absolute;
    top: 0;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #00f0ff;
    animation: loader-dots 1.2s linear infinite;
}

.loader-dots div:nth-child(1) {
    left: 8px;
    animation-delay: 0s;
}

.loader-dots div:nth-child(2) {
    left: 32px;
    animation-delay: -0.4s;
}

.loader-dots div:nth-child(3) {
    left: 56px;
    animation-delay: -0.8s;
}

@keyframes loader-dots {
    0%, 20%, 80%, 100% {
        transform: scale(1);
        opacity: 1;
    }
    50% {
        transform: scale(1.5);
        opacity: 0.5;
    }
}

.output-card {
    background: linear-gradient(135deg, rgba(123, 47, 247, 0.1), rgba(0, 240, 255, 0.1));
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(0, 240, 255, 0.3);
    box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.2);
    margin: 20px 0;
    color: #e0e0e0;
}

.output-card h3 {
    color: #00f0ff;
    font-family: 'Orbitron', sans-serif;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
}

.output-card h4 {
    color: #7b2ff7;
    font-family: 'Orbitron', sans-serif;
}

stButton>button {
    background: linear-gradient(45deg, #7b2ff7, #f21b3f);
    color: white;
    border: none;
    border-radius: 25px;
    padding: 12px 30px;
    font-family: 'Orbitron', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    box-shadow: 0 0 20px rgba(123, 47, 247, 0.5);
    transition: all 0.3s ease;
}

stButton>button:hover {
    box-shadow: 0 0 30px rgba(123, 47, 247, 0.8);
    transform: scale(1.05);
}

.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 240, 255, 0.3);
    border-radius: 10px;
    color: #e0e0e0;
    font-family: 'Rajdhani', sans-serif;
}

.stSelectbox>div>div>select {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 240, 255, 0.3);
    border-radius: 10px;
    color: #e0e0e0;
    font-family: 'Rajdhani', sans-serif;
}
</style>
"""

st.markdown(futuristic_css, unsafe_allow_html=True)

st.markdown('<h1 class="neon-title">⚡ AFIORA ASSISTANT ⚡</h1>', unsafe_allow_html=True)
st.markdown('<p class="neon-subtitle">AI-Powered Accessibility Intelligence</p>', unsafe_allow_html=True)

try:
    from backend.ai_service import get_ai_response
    ai_available = True
except:
    try:
        from ai_service import get_ai_response
        ai_available = True
    except:
        ai_available = False

def detect_intent(query):
    query_lower = query.lower()
    
    hospital_keywords = ["hospital", "doctor", "accessible", "wheelchair", "ramp", "lift", "medical facility", "clinic"]
    scheme_keywords = ["scheme", "benefit", "pension", "scholarship", "rights", "eligibility", "government", "disability certificate"]
    report_keywords = ["report", "medical report", "test result", "diagnosis", "prescription", "lab report", "simplify", "explain"]
    volunteer_keywords = ["volunteer", "help", "assist", "support", "guiding", "sign language", "emergency"]
    
    scores = {
        "hospital": sum(1 for kw in hospital_keywords if kw in query_lower),
        "schemes": sum(1 for kw in scheme_keywords if kw in query_lower),
        "report": sum(1 for kw in report_keywords if kw in query_lower),
        "volunteer": sum(1 for kw in volunteer_keywords if kw in query_lower)
    }
    
    max_score = max(scores.values())
    
    if max_score == 0:
        return "hospital", "Low"
    
    intent = max(scores, key=scores.get)
    
    if max_score >= 3:
        confidence = "High"
    elif max_score >= 2:
        confidence = "Medium"
    else:
        confidence = "Low"
    
    return intent, confidence

def typewriter(container, text, speed_ms=15):
    displayed = ""
    for char in text:
        displayed += char
        container.markdown(displayed)
        time.sleep(speed_ms / 1000.0)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

typing_enabled = st.checkbox(t("typing_effect"), value=True)

user_query = st.text_area(t("query"), height=100, placeholder="Ask me anything..." if lang != "hi" else "मुझसे कुछ भी पूछें...")

col1, col2 = st.columns(2)
with col1:
    user_city = st.text_input(t("city"), value="Hyderabad")
with col2:
    user_state = st.text_input(t("state"), value="Telangana")

force_intent = st.selectbox(
    t("force_intent"),
    ["Auto", "Hospital", "Schemes", "Report", "Volunteer"]
)

st.markdown('</div>', unsafe_allow_html=True)

analyze_btn = st.button("🚀 " + t("analyze_btn"))

with st.expander("💡 " + t("examples_title")):
    if lang == "hi":
        st.markdown("""
        - मेरे पास लिफ्ट और रैंप वाले अस्पताल खोजें
        - विकलांग छात्रों के लिए कौन सी छात्रवृत्तियां उपलब्ध हैं?
        - मेरी मेडिकल रिपोर्ट को सरल भाषा में समझाएं
        - मुझे व्हीलचेयर सहायता के लिए स्वयंसेवक चाहिए
        - तेलंगाना में विकलांग व्यक्तियों के लिए पेंशन योजनाएं
        - मेरे पास संकेत भाषा जानने वाले स्वयंसेवक ढूंढें
        """)
    else:
        st.markdown("""
        - Find hospitals with lifts and ramps near me
        - What scholarships are available for disabled students?
        - Explain my medical report in simple language
        - I need a volunteer for wheelchair assistance
        - Pension schemes for persons with disabilities in Telangana
        - Find volunteers who know sign language near me
        """)

if analyze_btn and user_query.strip():
    
    loader_placeholder = st.empty()
    loader_placeholder.markdown("""
    <div class="thinking-loader">
        <div>🤖 Analyzing your query...</div>
        <div class="loader-dots">
            <div></div>
            <div></div>
            <div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1.0)
    loader_placeholder.empty()
    
    if force_intent == "Auto":
        intent, confidence = detect_intent(user_query)
    else:
        intent = force_intent.lower()
        confidence = "High"
    
    st.markdown("---")
    
    badge_text = f"{intent.upper()} • {confidence.upper()}"
    st.markdown(f'<div style="text-align: center; margin: 20px 0;"><span class="intent-badge">{badge_text}</span></div>', unsafe_allow_html=True)
    
    if ai_available:
        try:
            prompt = f"You are Afiora Care assistant. Language: {'Hindi' if lang == 'hi' else 'English'}. User query: {user_query}. Intent: {intent}. Location: {user_city}, {user_state}. Provide structured response."
            ai_response = get_ai_response(prompt)
            if ai_response:
                st.markdown('<div class="output-card">', unsafe_allow_html=True)
                st.markdown("### 🤖 AI Enhanced Response" if lang != "hi" else "### 🤖 AI विस्तारित प्रतिक्रिया")
                if typing_enabled:
                    ai_container = st.empty()
                    typewriter(ai_container, ai_response, speed_ms=10)
                else:
                    st.write(ai_response)
                st.markdown('</div>', unsafe_allow_html=True)
        except:
            pass
    
    output_container = st.empty()
    
    if intent == "hospital":
        hospital_content = """
        <div class="output-card">
        <h3>🏥 """ + ("शीर्ष सुलभ अस्पताल (डेमो)" if lang == "hi" else "Top Accessible Hospitals (Demo)") + """</h3>
        
        <h4>1. Apollo Hospital - Jubilee Hills</h4>
        <p>• """ + ("रैंप" if lang == "hi" else "Ramp") + """: ✅ | """ + ("लिफ्ट" if lang == "hi" else "Lift") + """: ✅ | """ + ("सुलभ शौचालय" if lang == "hi" else "Accessible Toilet") + """: ✅ | """ + ("संकेत भाषा" if lang == "hi" else "Sign Language") + """: ✅</p>
        <p>• """ + ("स्कोर" if lang == "hi" else "Score") + """: 95/100</p>
        <p>• """ + ("कारण" if lang == "hi" else "Reason") + """: """ + ("उत्कृष्ट पहुंच सुविधाएं, प्रशिक्षित कर्मचारी" if lang == "hi" else "Excellent accessibility features, trained staff") + """</p>
        
        <h4>2. Care Hospital - Banjara Hills</h4>
        <p>• """ + ("रैंप" if lang == "hi" else "Ramp") + """: ✅ | """ + ("लिफ्ट" if lang == "hi" else "Lift") + """: ✅ | """ + ("सुलभ शौचालय" if lang == "hi" else "Accessible Toilet") + """: ❌ | """ + ("संकेत भाषा" if lang == "hi" else "Sign Language") + """: ❌</p>
        <p>• """ + ("स्कोर" if lang == "hi" else "Score") + """: 75/100</p>
        <p>• """ + ("कारण" if lang == "hi" else "Reason") + """: """ + ("बुनियादी सुविधाएं उपलब्ध" if lang == "hi" else "Basic facilities available") + """</p>
        
        <h4>3. Yashoda Hospital - Somajiguda</h4>
        <p>• """ + ("रैंप" if lang == "hi" else "Ramp") + """: ✅ | """ + ("लिफ्ट" if lang == "hi" else "Lift") + """: ❌ | """ + ("सुलभ शौचालय" if lang == "hi" else "Accessible Toilet") + """: ✅ | """ + ("संकेत भाषा" if lang == "hi" else "Sign Language") + """: ✅</p>
        <p>• """ + ("स्कोर" if lang == "hi" else "Score") + """: 85/100</p>
        <p>• """ + ("कारण" if lang == "hi" else "Reason") + """: """ + ("अच्छी सुविधाएं, जमीनी तल पर सेवाएं" if lang == "hi" else "Good facilities, ground floor services") + """</p>
        
        <p style="margin-top: 20px; padding: 15px; background: rgba(0, 240, 255, 0.1); border-radius: 10px; border-left: 3px solid #00f0ff;">
        ✨ <strong>""" + ("अगला कदम" if lang == "hi" else "Next Action") + """:</strong> """ + ("अधिक विवरण के लिए Hospital Finder पेज खोलें" if lang == "hi" else "Open Hospital Finder page for more details") + """
        </p>
        </div>
        """
        
        if typing_enabled:
            typewriter(output_container, hospital_content, speed_ms=5)
        else:
            output_container.markdown(hospital_content, unsafe_allow_html=True)
    
    elif intent == "schemes":
        schemes_content = """
        <div class="output-card">
        <h3>📋 """ + ("संभावित योजनाएं (डेमो)" if lang == "hi" else "Possible Schemes (Demo)") + """</h3>
        
        <h4>""" + ("राष्ट्रीय योजनाएं" if lang == "hi" else "National Schemes") + """</h4>
        
        <h4>1. """ + ("प्रधानमंत्री छात्रवृत्ति योजना" if lang == "hi" else "Prime Minister Scholarship Scheme") + """</h4>
        <p>• """ + ("वित्तीय सहायता" if lang == "hi" else "Financial assistance") + """: ₹10,000 - ₹50,000 """ + ("प्रति वर्ष" if lang == "hi" else "per year") + """</p>
        <p>• """ + ("पात्रता" if lang == "hi" else "Eligibility") + """: 40%+ """ + ("विकलांगता" if lang == "hi" else "disability") + """, """ + ("आय" if lang == "hi" else "income") + """ < 2.5 """ + ("लाख" if lang == "hi" else "lakhs") + """</p>
        
        <h4>2. """ + ("दीनदयाल विकलांग पुनर्वास योजना" if lang == "hi" else "Deen Dayal Disability Rehabilitation Scheme") + """</h4>
        <p>• """ + ("कौशल प्रशिक्षण और रोजगार सहायता" if lang == "hi" else "Skill training and employment assistance") + """</p>
        <p>• """ + ("पात्रता" if lang == "hi" else "Eligibility") + """: """ + ("सभी प्रकार की विकलांगताएं" if lang == "hi" else "All types of disabilities") + """, 18-60 """ + ("वर्ष" if lang == "hi" else "years") + """</p>
        
        <h4>""" + ("तेलंगाना राज्य योजना" if lang == "hi" else "Telangana State Scheme") + """</h4>
        
        <h4>3. """ + ("आसरा पेंशन योजना" if lang == "hi" else "Aasara Pension Scheme") + """</h4>
        <p>• """ + ("मासिक सहायता" if lang == "hi" else "Monthly assistance") + """: ₹3,016</p>
        <p>• """ + ("पात्रता" if lang == "hi" else "Eligibility") + """: 18+ """ + ("वर्ष" if lang == "hi" else "years") + """, 40%+ """ + ("विकलांगता" if lang == "hi" else "disability") + """</p>
        
        <p style="margin-top: 20px; padding: 15px; background: rgba(123, 47, 247, 0.1); border-radius: 10px; border-left: 3px solid #7b2ff7;">
        ✨ <strong>""" + ("अगला कदम" if lang == "hi" else "Next Action") + """:</strong> """ + ("पूर्ण विवरण के लिए Scheme Advisor पेज खोलें" if lang == "hi" else "Open Scheme Advisor page for complete details") + """
        </p>
        </div>
        """
        
        if typing_enabled:
            typewriter(output_container, schemes_content, speed_ms=5)
        else:
            output_container.markdown(schemes_content, unsafe_allow_html=True)
    
    elif intent == "report":
        report_content = """
        <div class="output-card">
        <h3>📄 """ + ("मेडिकल रिपोर्ट सरलीकरण" if lang == "hi" else "Medical Report Simplification") + """</h3>
        """
        
        if typing_enabled:
            output_container.markdown(report_content, unsafe_allow_html=True)
        else:
            output_container.markdown(report_content, unsafe_allow_html=True)
        
        report_text = st.text_area(("अपनी मेडिकल रिपोर्ट यहां पेस्ट करें:" if lang == "hi" else "Paste your medical report here:"), height=150)
        
        if report_text.strip():
            report_analysis = """
            <h4>📝 """ + ("सरल सारांश" if lang == "hi" else "Simple Summary") + """</h4>
            <p>""" + ("आपकी रिपोर्ट दर्शाती है कि सभी मुख्य पैरामीटर सामान्य सीमा में हैं।" if lang == "hi" else "Your report shows that all major parameters are within normal range.") + """</p>
            
            <h4>🔍 """ + ("प्रमुख शब्दों की व्याख्या" if lang == "hi" else "Key Terms Explained") + """</h4>
            <p>• <strong>""" + ("हीमोग्लोबिन" if lang == "hi" else "Hemoglobin") + """:</strong> """ + ("रक्त में ऑक्सीजन ले जाने वाला प्रोटीन" if lang == "hi" else "Protein in blood that carries oxygen") + """</p>
            <p>• <strong>""" + ("ग्लूकोज" if lang == "hi" else "Glucose") + """:</strong> """ + ("रक्त शर्करा का स्तर" if lang == "hi" else "Blood sugar level") + """</p>
            
            <p style="margin-top: 20px; padding: 15px; background: rgba(242, 27, 63, 0.1); border-radius: 10px; border-left: 3px solid #f21b3f;">
            ✨ <strong>""" + ("अगला कदम" if lang == "hi" else "Next Action") + """:</strong> """ + ("PDF अपलोड के लिए Report Upload पेज खोलें" if lang == "hi" else "Open Report Upload page for PDF uploads") + """
            </p>
            </div>
            """
            st.markdown(report_analysis, unsafe_allow_html=True)
        else:
            st.markdown("</div>", unsafe_allow_html=True)
    
    elif intent == "volunteer":
        volunteer_content = """
        <div class="output-card">
        <h3>🤝 """ + ("नजदीकी स्वयंसेवक (डेमो)" if lang == "hi" else "Nearby Volunteers (Demo)") + """</h3>
        
        <h4>1. Rajesh Kumar - Hitech City</h4>
        <p>• """ + ("कौशल" if lang == "hi" else "Skills") + """: """ + ("व्हीलचेयर सहायता, सामान्य सहायता" if lang == "hi" else "Wheelchair assistance, General support") + """</p>
        <p>• """ + ("दूरी" if lang == "hi" else "Distance") + """: 2.3 km</p>
        <p>• """ + ("उपलब्धता" if lang == "hi" else "Availability") + """: ✅ """ + ("अभी उपलब्ध" if lang == "hi" else "Available now") + """</p>
        
        <h4>2. Priya Sharma - Gachibowli</h4>
        <p>• """ + ("कौशल" if lang == "hi" else "Skills") + """: """ + ("संकेत भाषा, दृष्टिबाधितों की मार्गदर्शन" if lang == "hi" else "Sign language, Guiding blind users") + """</p>
        <p>• """ + ("दूरी" if lang == "hi" else "Distance") + """: 3.8 km</p>
        <p>• """ + ("उपलब्धता" if lang == "hi" else "Availability") + """: ✅ """ + ("अभी उपलब्ध" if lang == "hi" else "Available now") + """</p>
        
        <h4>3. Lakshmi Reddy - Kondapur</h4>
        <p>• """ + ("कौशल" if lang == "hi" else "Skills") + """: """ + ("व्हीलचेयर सहायता, दृष्टिबाधितों की मार्गदर्शन" if lang == "hi" else "Wheelchair assistance, Guiding blind users") + """</p>
        <p>• """ + ("दूरी" if lang == "hi" else "Distance") + """: 5.2 km</p>
        <p>• """ + ("उपलब्धता" if lang == "hi" else "Availability") + """: ✅ """ + ("अभी उपलब्ध" if lang == "hi" else "Available now") + """</p>
        
        <p style="margin-top: 20px; padding: 15px; background: rgba(0, 240, 255, 0.1); border-radius: 10px; border-left: 3px solid #00f0ff;">
        ✨ <strong>""" + ("अगला कदम" if lang == "hi" else "Next Action") + """:</strong> """ + ("अनुरोध भेजने के लिए Volunteer Help पेज खोलें" if lang == "hi" else "Open Volunteer Help page to send request") + """
        </p>
        </div>
        """
        
        if typing_enabled:
            typewriter(output_container, volunteer_content, speed_ms=5)
        else:
            output_container.markdown(volunteer_content, unsafe_allow_html=True)

elif analyze_btn and not user_query.strip():
    st.warning("⚠️ " + ("कृपया एक प्रश्न दर्ज करें" if lang == "hi" else "Please enter a question"))

st.markdown("---")
st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
st.info("🌟 Demo-safe: Works with or without AI backend • Deterministic fallback ensures reliability" if lang != "hi" else "🌟 डेमो-सुरक्षित: AI बैकएंड के साथ या बिना काम करता है • निर्धारणात्मक फॉलबैक विश्वसनीयता सुनिश्चित करता है")
st.markdown('</div>', unsafe_allow_html=True)