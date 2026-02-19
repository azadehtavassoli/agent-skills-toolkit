"""Minimal MCP server using Streamable HTTP transport."""

from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "mcp-streamable-http-server",
    stateless_http=True,
    json_response=True,
)


class AddResult(BaseModel):
    total: int


@mcp.tool()
def add_numbers(a: int, b: int) -> AddResult:
    return AddResult(total=a + b)


def main() -> None:
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
