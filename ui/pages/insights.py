import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Insights")

weak = requests.get(f"{BASE_URL}/weak-areas").json()
results = requests.get(f"{BASE_URL}/results").json()

st.subheader("Weak Areas")

if weak.get("weak_areas"):
    for concept, count in weak["weak_areas"]:
        st.write(f"{concept} — missed {count} times")
else:
    st.write("No weak areas detected")

st.subheader("Performance Trend")

scores = [r["score"] for r in results]

if scores:
    st.line_chart(scores)
else:
    st.write("No data yet")