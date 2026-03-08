import streamlit as st
import requests

st.title("CareerPilot AI")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file is not None:

    files = {"file": uploaded_file}

    response = requests.post(
        "http://127.0.0.1:8000/uploadfile/",
        files=files
    )

    if response.status_code == 200:

        data = response.json()

        st.subheader("Detected Skills")
        st.write(data.get("skills_detected"))

        st.subheader("Recommended Jobs")
        st.write(data.get("recommended_jobs"))

        st.subheader("Match Score")
        st.write(data.get("match_score"))

        if data.get("improved_resume"):
            st.subheader("Improved Resume")
            st.write(data.get("improved_resume"))

        if data.get("application_status"):
            st.subheader("Application Status")
            st.write(data.get("application_status"))

    else:
        st.error("Backend API error")
        st.text(response.text)