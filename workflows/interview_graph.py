from typing import TypedDict, Dict, Annotated
from langgraph.graph import StateGraph
from langgraph.channels import LastValue
from agents_functions import interview_nodes  

class InterviewState(TypedDict):
    resume_text: str
    clusters: Dict[int, list]
    current_cluster: int
    current_question: Annotated[str, LastValue]
    user_response: str
    follow_up_needed: bool

def build_interview_flow():
    workflow = StateGraph(InterviewState)

    workflow.add_node("cluster_resume", interview_nodes.cluster_resume)
    workflow.add_node("generate_question", interview_nodes.generate_question)
    workflow.add_node("get_user_response", interview_nodes.get_user_response)
    workflow.add_node("generate_followup", interview_nodes.generate_followup)
    workflow.add_node("move_to_next", interview_nodes.move_to_next_cluster)
    workflow.add_node("end", interview_nodes.end_interview)

    # Edges
    workflow.add_edge("cluster_resume", "generate_question")
    workflow.add_edge("generate_question", "get_user_response")
    workflow.add_edge("get_user_response", "generate_followup")
    workflow.add_edge("generate_followup", "get_user_response")

    # Branching based on followup
    workflow.add_conditional_edges(
        "generate_followup",
        interview_nodes.should_continue,
        {
            True: "move_to_next",
            False: "end"
        }
    )

    workflow.add_edge("move_to_next", "generate_question")

    workflow.set_entry_point("cluster_resume")
    workflow.set_finish_point("end")

    return workflow.compile()
