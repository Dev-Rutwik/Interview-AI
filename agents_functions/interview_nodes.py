from typing import Dict,TYPE_CHECKING
from agents_functions.clusterer import cluster_resume_sentences
from agents_functions.question_generator import generate_initial_question, generate_followup_question
if TYPE_CHECKING:
    from workflows.interview_graph import InterviewState
def cluster_resume(state: Dict):
    clusters = cluster_resume_sentences(state["resume_text"])
    return {"clusters": clusters, "current_cluster": 0}

def generate_question(state: "InterviewState"):
    if state["current_cluster"] == -1:
        return {}
    content = state["clusters"][state["current_cluster"]]
    question = generate_initial_question(content)
    return {"current_question": question, "follow_up_needed": True}

def get_user_response(state: Dict):
    print(f"\\nQuestion: {state['current_question']}")
    response = input("Your answer: ")
    return {"user_response": response}

def should_ask_followup(state):
    return state.get("follow_up_needed", False)


def generate_followup(state: "InterviewState"):
    if not state["follow_up_needed"]:
        return {"follow_up_needed": False}
    
    followup = generate_followup_question(state["current_question"], state["user_response"])
    return {"current_question": followup, "follow_up_needed": False}

def move_to_next_cluster(state: Dict):
    next_cluster = state["current_cluster"] + 1
    if next_cluster >= len(state["clusters"]):
        return {"current_cluster": -1}
    return {"current_cluster": next_cluster, "follow_up_needed": True}

def should_continue(state: Dict):
    return state["current_cluster"] != -1

def end_interview(state: Dict):
    print("\\nInterview completed! Thank you for your time.")
    return state
