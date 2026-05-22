import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Interview Readiness")

if st.button("Analyze My Performance"):

    data = requests.get(f"{BASE_URL}/interview-prep").json()

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.metric("Average Score", data["average_score"])

    st.markdown("### Focus Areas")

    # cleaner display
    topics = data["focus_topics"]

    for t in topics:
        st.write(f"• {t.capitalize()}")

    st.markdown("### Advice")
    st.info(data["advice"])

    st.markdown('</div>', unsafe_allow_html=True)