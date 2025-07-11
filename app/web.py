import streamlit as st
from workflows.interview_graph import build_interview_flow
from io import BytesIO
from pdfminer.high_level import extract_text

st.set_page_config(page_title="AI Interviewer", layout="centered")
st.title("🤖 AI-Powered Interviewer (PDF Resume)")

st.markdown("Upload your **PDF resume** and start an interactive interview. (Interview runs in terminal for now.)")

resume_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

def extract_text_from_pdf(uploaded_file):
    # Read PDF content as text
    return extract_text(BytesIO(uploaded_file.read()))

if resume_file is not None:
    resume_text = extract_text_from_pdf(resume_file)

    if st.button("🚀 Start Interview"):
        st.success("Interview started! Follow the questions in your terminal.")
        interview_flow = build_interview_flow()
        interview_flow.invoke({
            "resume_text": resume_text,
            "clusters": {},
            "current_cluster": 0,
            "current_question": "",
            "user_response": "",
            "follow_up_needed": True
        })
