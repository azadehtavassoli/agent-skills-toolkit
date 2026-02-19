# Skill: MCP_SERVER_IMPLEMENTATION

## Purpose
Provide deterministic MCP server implementation patterns using the official `mcp` SDK for both `stdio` and Streamable HTTP transports.

## Version Baseline
- SDK package: `mcp`
- Stable baseline verified: `1.26.0` (PyPI, January 8, 2026)
- Pre-release note: `2.0.0a6` exists (pre-alpha), not the default production target

## When to Use
- Creating new MCP servers
- Refactoring older MCP servers to modern transport patterns
- Adding transport support (`stdio` and `streamable-http`) in one codebase

## Hard Rules (MUST)
1. Use `FastMCP` from `mcp.server.fastmcp`.
2. Keep tools pure/deterministic for fixed inputs.
3. Expose both transports with explicit runtime configuration.
4. Use `stateless_http=True` and `json_response=True` for Streamable HTTP defaults.
5. Fail explicitly on invalid inputs; do not silently coerce behavior.

## Workflow
1. Define tool inputs/outputs with typed contracts.
2. Implement `stdio` entrypoint for local integration.
3. Implement Streamable HTTP entrypoint for remote integration.
4. Add transport-specific tests and a common behavior regression suite.

## Output Checklist
- [ ] `stdio` server skeleton present
- [ ] Streamable HTTP server skeleton present
- [ ] Typed tool contracts defined
- [ ] Transport-specific startup instructions included
- [ ] Deterministic test plan exists
