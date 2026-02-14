# UI TOPIC SKILL

## Purpose
Define deterministic UI implementation patterns with accessibility, component decomposition, and reproducible behavior.

## Framework Adapters
- `topics/ui/frameworks/streamlit/`
- `topics/ui/frameworks/gradio/`

## Hard MUST Rules
- Component contracts must be explicit.
- Accessibility checks are mandatory.
- UI state transitions must be predictable and testable.
- Framework-specific UI logic MUST remain inside adapter folders.
