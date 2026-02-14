"""LangChain agent skeleton using create_agent + Pydantic structured output + debug rotating file logs."""

from __future__ import annotations

import json
import logging
import time
import uuid
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from langchain.agents import create_agent
from langchain_core.tools import tool
from pydantic import BaseModel, Field


class AgentInput(BaseModel):
    user_query: str = Field(..., description="User question")


class AgentOutput(BaseModel):
    answer: str = Field(..., description="Final answer")
    tool_used: str | None = Field(default=None, description="Tool used if any")


class SearchArgs(BaseModel):
    query: str = Field(..., description="Search query")


@tool(args_schema=SearchArgs)
def dummy_search(query: str) -> str:
    """Search an internal corpus (stub)."""
    return f"top result for: {query}"


def build_logger(
    logger_name: str = "langchain_agent",
    log_file: str = "logs/langchain_agent.log",
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
) -> logging.Logger:
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)
    return logger


def log_event(logger: logging.Logger, **payload: Any) -> None:
    logger.debug(json.dumps(payload, ensure_ascii=False))


def run_agent(agent_input: AgentInput) -> AgentOutput:
    request_id = str(uuid.uuid4())
    logger = build_logger()

    agent = create_agent(
        model="openai:gpt-4o-mini",
        tools=[dummy_search],
        system_prompt="You are a precise assistant. Always return structured output.",
        response_format=AgentOutput,
    )

    start = time.perf_counter()
    log_event(
        logger,
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        request_id=request_id,
        agent_type="create_agent",
        operation="invoke_start",
        status="pending",
        input=agent_input.model_dump(),
    )

    result = agent.invoke({"messages": [{"role": "user", "content": agent_input.user_query}]})
    structured = result["structured_response"]
    duration_ms = int((time.perf_counter() - start) * 1000)

    log_event(
        logger,
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        request_id=request_id,
        agent_type="create_agent",
        operation="invoke_complete",
        status="success",
        duration_ms=duration_ms,
        output=structured.model_dump(),
    )

    return structured
