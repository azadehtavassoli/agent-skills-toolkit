"""Placeholder Google ADK agent adapter complying with core standards."""

from pydantic import BaseModel


class GoogleAdkAgentRequest(BaseModel):
    request_id: str
    user_input: str


class GoogleAdkAgentResponse(BaseModel):
    request_id: str
    final_output: str


def run_google_adk_agent(request: GoogleAdkAgentRequest) -> GoogleAdkAgentResponse:
    return GoogleAdkAgentResponse(request_id=request.request_id, final_output="TODO")
