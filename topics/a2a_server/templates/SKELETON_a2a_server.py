"""Minimal A2A server wiring with Agent Card + request handler."""

import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from SKELETON_a2a_agent_executor import EchoAgentExecutor

HOST = "0.0.0.0"
PORT = 9999
PUBLIC_URL = f"http://localhost:{PORT}"

AGENT_CARD = AgentCard(
    name="Echo Agent",
    description="Minimal A2A echo server.",
    url=PUBLIC_URL,
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[
        AgentSkill(
            id="echo",
            name="Echo",
            description="Echo a text-style prompt.",
            tags=["echo", "text"],
            examples=["Echo: hello world"],
        )
    ],
)

REQUEST_HANDLER = DefaultRequestHandler(
    agent_executor=EchoAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

APP = A2AStarletteApplication(
    agent_card=AGENT_CARD,
    http_handler=REQUEST_HANDLER,
).build()


def main() -> None:
    uvicorn.run(APP, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
