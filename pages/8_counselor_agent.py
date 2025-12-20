import streamlit as st

st.set_page_config(
    page_title="AI Counselor",
    layout="centered"
)

st.title("🧠 AI Counselor")

st.write("Talk to the counselor below:")

query = st.text_input("Enter your concern")

if query:
    st.success("Query received")
    st.write("Summary: We are here to support you.")
    st.write("Next steps:")
    st.write("• Stay calm")
    st.write("• Reach out to trusted people")
    st.write("• Seek professional help if needed")
