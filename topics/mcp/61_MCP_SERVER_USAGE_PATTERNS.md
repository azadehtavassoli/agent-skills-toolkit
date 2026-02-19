# Skill: MCP_SERVER_USAGE_PATTERNS

## Purpose
Provide client usage patterns for MCP servers across local `stdio` and online/remote Streamable HTTP deployments.

## When to Use
- Connecting to local MCP servers started as subprocesses
- Connecting to remote or hosted MCP endpoints over HTTP
- Building reusable client adapters for tools discovery and invocation

## Hard Rules (MUST)
1. Use `stdio_client` with `StdioServerParameters` for local usage.
2. Use `streamable_http_client` for remote/hosted usage.
3. Always call `session.initialize()` before listing/calling tools.
4. Surface tool call failures explicitly; do not ignore failed results.
5. Keep URL/command configuration externalized and environment-specific.

## Workflow
1. Choose transport by deployment mode:
   - Local subprocess: `stdio`
   - Hosted endpoint: Streamable HTTP
2. Open transport context manager and create `ClientSession`.
3. Initialize session, inspect tool registry, then call tools.
4. Serialize outputs to structured logs for traceability.

## Output Checklist
- [ ] Local `stdio` client template present
- [ ] Remote Streamable HTTP client template present
- [ ] Initialization and call sequence is correct
- [ ] Error handling path documented
