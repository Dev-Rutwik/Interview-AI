from langgraph.graph import StateGraph
from agents_functions import interview_nodes  
from schema.types import InterviewState

def build_interview_flow():
    workflow = StateGraph(InterviewState)

    # Nodes
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

    workflow.add_conditional_edges(
        "generate_followup",
        interview_nodes.should_ask_followup,
        {
            True: "get_user_response", 
            False: "move_to_next",      
        }
    )

    workflow.add_conditional_edges(
        "move_to_next",
        interview_nodes.should_continue,
        {
            True: "generate_question", 
            False: "end"      
        }
    )

    workflow.set_entry_point("cluster_resume")
    workflow.set_finish_point("end")

    return workflow.compile()
