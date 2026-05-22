import streamlit as st
import requests
import json
import random

BASE_URL = "http://127.0.0.1:8000"

st.title("Live Interview Simulation")

with open("../data/dataset.json") as f:
    dataset = json.load(f)

if "current_q" not in st.session_state:
    st.session_state.current_q = random.choice(dataset)

if "result" not in st.session_state:
    st.session_state.result = None

# Layout
left, right = st.columns([2, 1])

# LEFT (Interview)
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Interviewer")
    st.write(f"**{st.session_state.current_q['question']}**")

    answer = st.text_area("Your Answer", height=180)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit"):
            response = requests.post(
                f"{BASE_URL}/evaluate",
                json={
                    "question": st.session_state.current_q["question"],
                    "answer": answer
                }
            )
            if response.status_code == 200:
                st.session_state.result = response.json()

    with col2:
        if st.button("Next"):
            st.session_state.current_q = random.choice(dataset)
            st.session_state.result = None

    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT (Evaluation)
with right:
    if st.session_state.result:
        r = st.session_state.result

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("Evaluation")

        st.metric("Score", f"{r['score']} / 10")

        cov = float(r["concept_coverage"].replace("%", ""))
        st.progress(cov / 100)

        st.markdown("### Strengths")
        st.write(", ".join(r["matched_keywords"]) or "Basic understanding")

        st.markdown("### Improve")
        st.write(", ".join(r["missing_keywords"]) or "Good coverage")

        st.markdown("### Feedback")
        st.success(r["feedback"])

        st.markdown('</div>', unsafe_allow_html=True)