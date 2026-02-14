"""Framework-agnostic routing abstractions for deterministic tool selection."""

from __future__ import annotations

from typing import Callable

from pydantic import BaseModel, Field


class RoutingDecision(BaseModel):
    tool_name: str
    reason: str
    confidence: float = Field(ge=0.0, le=1.0)


class RoutingPolicy(BaseModel):
    name: str
    deterministic: bool = True


def route_by_rules(user_input: str, rules: dict[str, str]) -> RoutingDecision:
    lowered = user_input.lower()
    for keyword, tool_name in rules.items():
        if keyword.lower() in lowered:
            return RoutingDecision(tool_name=tool_name, reason=f"keyword:{keyword}", confidence=1.0)
    return RoutingDecision(tool_name="default", reason="no_keyword_match", confidence=1.0)


def execute_with_policy(user_input: str, router: Callable[[str], RoutingDecision]) -> RoutingDecision:
    return router(user_input)
