import streamlit as st

st.set_page_config(
    page_title="Afiora – Inclusive Care",
    layout="wide"
)

st.title("🌈 Afiora")
st.subheader("An Inclusive Care & Support Platform")

st.markdown("""
Afiora helps **Persons with Disabilities (PwD)**, **Volunteers**, and  
**Counselors** navigate healthcare, emergencies, and emotional support  
with clarity, dignity, and ease.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📘 Learning Hub")
    st.write("Visual guides, videos, and steps for real-life situations.")

with col2:
    st.markdown("### 🧑‍🤝‍🧑 Volunteer Training")
    st.write("Learn how to help respectfully and effectively.")

with col3:
    st.markdown("### 🧠 Counselor Support")
    st.write("Interactive guidance for emotional well-being.")

st.divider()

st.error("🚨 Emergency: **112**   |   🚑 Ambulance: **108**")

st.caption("Built with empathy, technology, and accessibility 💙")
