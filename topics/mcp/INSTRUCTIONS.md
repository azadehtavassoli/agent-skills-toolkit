# MCP TOPIC INSTRUCTIONS

- Use the official MCP Python SDK package: `mcp`.
- Keep reusable implementation templates under `topics/mcp/templates/`.
- Use `stdio` for local process/server integration.
- Use `mcp.run(transport="streamable-http")` for networked deployments.
- For Streamable HTTP deployments, default to `FastMCP(..., stateless_http=True, json_response=True)`.
- Enforce all core standards:
  - `core/GLOBAL_RULES.md`
  - `core/LOGGING_STANDARD.md`
  - `core/TESTING_STANDARD.md`
  - `core/STRUCTURED_OUTPUT_STANDARD.md`
