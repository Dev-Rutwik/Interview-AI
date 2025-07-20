import streamlit as st
from io import BytesIO
from pdfminer.high_level import extract_text
from workflows.interview_graph import build_interview_flow

# === Streamlit Page Setup ===
st.set_page_config(page_title="AI Interviewer", layout="centered")
st.title("AI-Powered Interviewer")

# === Session Initialization ===
if "state" not in st.session_state:
    st.session_state.state = {
        "resume_text": "",
        "clusters": {},
        "current_cluster": 0,
        "current_question": "",
        "user_response": "",
        "follow_up_needed": True
    }

if "generator" not in st.session_state:
    st.session_state.generator = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# === Helper to extract text from PDF ===
def extract_text_from_pdf(uploaded_file):
    return extract_text(BytesIO(uploaded_file.read()))

def update_state_with_result(result):
    if isinstance(result, dict):
        for node_output in result.values():
            if isinstance(node_output, dict):
                st.session_state.state.update(node_output)

# === Resume Upload ===
if not st.session_state.state["resume_text"]:
    st.markdown("### Upload your **PDF Resume** to start the interview.")
    uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf"])
    if uploaded_file:
        st.session_state.state["resume_text"] = extract_text_from_pdf(uploaded_file)
        st.success("✅ Resume uploaded and extracted successfully!")
        st.rerun()

# === Display Resume and Start Button ===
if st.session_state.state["resume_text"] and st.session_state.generator is None:

    if st.button("🚀 Start Interview"):
        interview_flow = build_interview_flow()
        st.session_state.generator = interview_flow.stream(st.session_state.state)
        st.session_state.chat_history = []

        try:
            # Run the generator ONCE to start with clusters and first question
            result = next(st.session_state.generator)
            st.session_state.state.update(result)

            # If first question not ready yet, next() again once
            if not st.session_state.state.get("current_question"):
                result = next(st.session_state.generator)
                update_state_with_result(result)
        except StopIteration:
            st.success("🎉 Interview finished immediately — no questions.")
            st.session_state.generator = None

        st.rerun()
# === Main Interview Chat Logic ===
if st.session_state.generator:
    try:
        for turn in st.session_state.chat_history:
            with st.chat_message("interviewer"):
                st.markdown(turn["question"])
            with st.chat_message("user"):
                st.markdown(turn["answer"])

        question = st.session_state.state.get("current_question", "")
        print("The question is", question)

        if question:
            with st.chat_message("interviewer"):
                st.markdown(question)

            user_input = st.chat_input("Type your answer here...")
            if user_input:
                st.session_state.chat_history.append({
                    "question": question,
                    "answer": user_input
                })
                st.session_state.state["user_response"] = user_input

                try:
                    result = st.session_state.generator.send({"user_response": user_input})
                    update_state_with_result(result)

                    while True:
                        current_q = st.session_state.state.get("current_question", "")
                        if current_q and current_q != question:
                            break
                        result = next(st.session_state.generator)
                        update_state_with_result(result)

                    st.rerun()

                except StopIteration:
                    st.success("🎉 Interview completed! Thank you.")
                    st.session_state.generator = None

    except StopIteration:
        st.success("🎉 Interview completed! Thank you.")
        st.session_state.generator = None
