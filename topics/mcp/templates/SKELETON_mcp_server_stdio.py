"""Minimal MCP server using stdio transport."""

from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-stdio-server")


class AddResult(BaseModel):
    total: int


@mcp.tool()
def add_numbers(a: int, b: int) -> AddResult:
    return AddResult(total=a + b)


def main() -> None:
    # Default FastMCP transport is stdio.
    mcp.run()


if __name__ == "__main__":
    main()
