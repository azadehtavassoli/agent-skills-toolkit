"""Minimal A2A client using modern ClientFactory APIs."""

import asyncio

from a2a.client import ClientConfig, ClientFactory
from a2a.client.helpers import create_text_message_object

AGENT_URL = "http://localhost:9999"


async def run() -> None:
    client_config = ClientConfig(streaming=True)
    client = await ClientFactory.connect(AGENT_URL, client_config=client_config)

    message = create_text_message_object(content="Hello from A2A client")
    async for event in client.send_message(message):
        if isinstance(event, tuple):
            task, update = event
            print(task.model_dump(mode="json", exclude_none=True))
            if update is not None:
                print(update.model_dump(mode="json", exclude_none=True))
        else:
            print(event.model_dump(mode="json", exclude_none=True))


if __name__ == "__main__":
    asyncio.run(run())
