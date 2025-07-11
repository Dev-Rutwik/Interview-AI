import streamlit as st
from ai_interviewer.agents_functions.main_agent import run_interview
from ai_interviewer.interface.resume_parser import extract_text_from_pdf

def main():
    st.set_page_config(page_title="AI Interviewer", layout="centered")
    st.title("🤖 AI-Powered Interviewer")
    st.write("Upload your resume to start a simulated technical interview.")

    resume_file = st.file_uploader("Upload Resume (.PDF only for now)", type=["pdf"])

    if resume_file is not None:
        resume_text = extract_text_from_pdf(resume_file)

        if st.button("Start Interview"):
            st.success("Interview Started — follow the terminal or console to respond!")
            run_interview(resume_text)

if __name__ == "__main__":
    main()