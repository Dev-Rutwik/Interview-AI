from workflows.interview_graph import build_interview_flow
from pdfminer.high_level import extract_text
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    return extract_text(BytesIO(uploaded_file.read()))

def run_interview(resume_text):
    interview_flow = build_interview_flow()
    interview_flow.invoke({
        "resume_text": resume_text,
        "clusters": {},
        "current_cluster": 0,
        "current_question": "",
        "user_response": "",
        "follow_up_needed": True
    })

if __name__ == "__main__":
    file_path = "Interview-AI/resume/AI_ML_LResume.pdf"
    with open(file_path, 'rb') as f:
            resume = extract_text_from_pdf(f)
            # print(resume)
    run_interview(resume)
