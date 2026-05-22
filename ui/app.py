import streamlit as st

st.set_page_config(
    page_title="AI Interview Coach",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium UI styling
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Headings */
h1, h2, h3 {
    color: #e2e8f0;
}

/* Card */
.card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border: none;
    padding: 10px 20px;
}

/* Text Area */
textarea {
    border-radius: 10px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Interview Coach")
st.caption("Practice. Improve. Get Interview Ready.")