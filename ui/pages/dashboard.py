import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Dashboard")

# Fetch data
avg = requests.get(f"{BASE_URL}/analytics/average-score").json()
weak = requests.get(f"{BASE_URL}/weak-areas").json()
results = requests.get(f"{BASE_URL}/results").json()

# Metrics row
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Score", avg.get("average_score", 0))

with col2:
    st.metric("Total Attempts", len(results))

with col3:
    if weak.get("weak_areas"):
        st.metric("Top Weak Area", weak["weak_areas"][0][0])
    else:
        st.metric("Top Weak Area", "N/A")

# Recent attempts
st.subheader("Recent Performance")

for r in results[-5:][::-1]:
    with st.container():
        st.markdown(f"""
        **Question:** {r['question']}  
        **Score:** {r['score']}  
        **Feedback:** {r['feedback']}
        """)
        st.divider()
        