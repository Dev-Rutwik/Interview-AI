from typing import Dict, TYPE_CHECKING
import json
from agents_functions.clusterer import cluster_resume_sentences
from agents_functions.question_generator import generate_initial_question, generate_followup_question, is_followup_req

if TYPE_CHECKING:
    from workflows.interview_graph import InterviewState


def cluster_resume(state):
    clusters = cluster_resume_sentences(state["resume_text"])
    return {
        "clusters": clusters,
        "current_cluster": 0,
        "current_question": "",     
        "user_response": "",      
        "follow_up_needed": True
    }


def generate_question(state):
    if state["current_cluster"] == -1:
        return {}

    content = state["clusters"][state["current_cluster"]]
    question = generate_initial_question(content)

    return {
        "current_question": question,
        "user_response": "",      
        # "follow_up_needed": True
    }


def get_user_response(state):
   
    return {
        "current_question": state["current_question"],
        "user_response": state.get("user_response", ""),
        # "follow_up_needed": state.get('follow_up_needed')
    }


def should_ask_followup(state):
    return state.get("follow_up_needed", False)

def generate_followup(state):
    if not state.get("follow_up_needed", False):
        return {"follow_up_needed": False}

    followup_response = is_followup_req(
        state.get("user_response", "")
    )
    print("Is follow up required >>", followup_response)
    try:
        followup_data = json.loads(followup_response)
        print("The follow up data is ", followup_data)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON from LLM:", followup_response)
        return {"follow_up_needed": False}

    if not followup_data.get("follow_up_needed", False):
        return {"follow_up_needed": False}

    return {
        "current_question": followup_data.get("question", ""),
        "user_response": "",
        "follow_up_needed": True
    }

def move_to_next_cluster(state):
    next_cluster = state["current_cluster"] + 1
    # print(next_cluster)
    if next_cluster >= len(state["clusters"]):
        return {
            "current_cluster": -1,
            "current_question": "",
            "user_response": "",
            "follow_up_needed": False
        }
    return {
        "current_cluster": next_cluster,
        "current_question": "", 
        "user_response": "",
        # "follow_up_needed": True
    }



def should_continue(state):
    return state["current_cluster"] != -1


def end_interview(state):
    return {
        "current_cluster": -1,
        "current_question": "",
        "user_response": "",
        "follow_up_needed": False
    }
