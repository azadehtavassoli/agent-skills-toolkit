"""MCP client example for remote Streamable HTTP servers."""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

SERVER_URL = "http://localhost:8000/mcp"


async def run() -> None:
    async with streamable_http_client(SERVER_URL) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "add_numbers",
                arguments={"a": 4, "b": 5},
            )
            print(result.model_dump(mode="json", exclude_none=True))


if __name__ == "__main__":
    asyncio.run(run())
