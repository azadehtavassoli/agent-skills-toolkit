# MCP TOPIC SKILL

## Purpose
Implement Model Context Protocol (MCP) servers and clients with the official MCP Python SDK (`mcp`) using deterministic, transport-explicit patterns.

## When to Use
- Building MCP servers over `stdio` for local process integration
- Building MCP servers over Streamable HTTP for remote/networked access
- Building MCP clients that connect to local (`stdio`) or online (`streamable-http`) servers
- Defining reusable MCP templates and transport-specific implementation patterns

## Hard MUST Rules
1. Use official SDK APIs from the `mcp` package.
2. Keep tool behavior deterministic for fixed inputs.
3. Implement transport explicitly (`stdio` vs `streamable-http`) instead of implicit defaults in production code.
4. Use Streamable HTTP production defaults (`stateless_http=True`, `json_response=True`) unless there is a documented reason not to.
5. Keep structured output boundaries typed and validated.
6. Add deterministic tests with no live provider/network dependencies in CI.

## Workflow
1. Define typed tool inputs/outputs.
2. Implement server transport (`stdio` and/or `streamable-http`).
3. Implement client usage for local and remote server connections.
4. Validate behavior and failure paths with deterministic tests.

## Output Checklist
- [ ] Server transport is explicit and documented
- [ ] Tool inputs/outputs are typed
- [ ] Local `stdio` usage template included
- [ ] Remote Streamable HTTP usage template included
- [ ] Test plan covers routing, typing, and error paths
