"""Gradio UI skeleton aligned with UI topic governance."""

from __future__ import annotations

from pydantic import BaseModel


class UIInput(BaseModel):
    user_message: str


class UIOutput(BaseModel):
    response_text: str


def handle_ui(input_model: UIInput) -> UIOutput:
    return UIOutput(response_text=f"Echo: {input_model.user_message}")
