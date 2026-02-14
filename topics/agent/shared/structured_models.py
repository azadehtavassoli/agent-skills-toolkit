"""Framework-agnostic structured models for agent topic."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    request_id: str = Field(..., description="Unique request identifier")
    user_input: str = Field(..., description="User input payload")
    metadata: dict[str, Any] = Field(default_factory=dict)


class AgentStep(BaseModel):
    step_id: str
    operation: str
    status: Literal["pending", "success", "failure"]
    tool_name: str | None = None
    reasoning: str | None = None


class AgentResponse(BaseModel):
    request_id: str
    final_output: str
    steps: list[AgentStep] = Field(default_factory=list)
    deterministic: bool = True
