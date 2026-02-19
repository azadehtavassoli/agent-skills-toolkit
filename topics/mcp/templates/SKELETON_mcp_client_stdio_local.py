"""MCP client example for local stdio servers."""

import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PARAMS = StdioServerParameters(
    command="python",
    args=["topics/mcp/templates/SKELETON_mcp_server_stdio.py"],
)


async def run() -> None:
    async with stdio_client(SERVER_PARAMS) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "add_numbers",
                arguments={"a": 2, "b": 3},
            )
            print(result.model_dump(mode="json", exclude_none=True))


if __name__ == "__main__":
    asyncio.run(run())
