from typing import TypedDict, Dict, Annotated
from langgraph.channels import LastValue

class InterviewState(TypedDict):
    resume_text: str
    clusters: Dict[int, list]
    current_cluster: int
    current_question: Annotated[str, LastValue]
    user_response: str
    follow_up_needed: bool
