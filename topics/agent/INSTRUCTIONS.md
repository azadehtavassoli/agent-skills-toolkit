# AGENT TOPIC INSTRUCTIONS

## Usage Guidance for Copilot/ChatGPT
- Prioritize `topics/agent/shared/` for framework-agnostic logic.
- Implement framework-specific code only under `topics/agent/frameworks/<framework>/`.

## Required Imports (Python)
- `from pydantic import BaseModel`
- `from topics.agent.shared.routing_policy import RoutingDecision, RoutingPolicy`
- `from topics.agent.shared.logging_adapter import build_topic_logger, log_event`
- `from topics.agent.shared.structured_models import AgentRequest, AgentResponse`

## Compliance Enforcement
- Enforce `core/GLOBAL_RULES.md`, `core/LOGGING_STANDARD.md`, `core/TESTING_STANDARD.md`, and `core/STRUCTURED_OUTPUT_STANDARD.md`.
- Reject deprecated runtime patterns in framework adapters.

## Required Logging Configuration
- DEBUG file logging with rotation (`10MB`, `5 backups`).
- Structured JSON-lines with required fields.

## Required Test Coverage
- Routing determinism tests
- Structured response validation tests
- Tool invocation trace tests
- Memory policy tests
