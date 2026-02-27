# LangGraph Skill

## Capability

You can design and build stateful, long-running agents using LangGraph's low-level orchestration primitives and integrate observability via LangSmith for development and debugging.

## Key Abilities

### 1. Design Agents with LangGraph
- **Graph-based state machines**: Design agents as directed acyclic graphs (DAGs) using nodes (computation steps) and edges (transitions between them).
- **Explicit control flow**: Define precisely what happens at each step—no hidden abstractions or opaque "agent loops".
- **State management**: Define and manage state schemas that flow through the graph, enabling complex multi-step workflows.
- **Node types**:
  - Decision nodes (routing/branching)
  - Action nodes (call LLMs, tools, services)
  - Aggregate/transform nodes (process outputs)
- **Human-in-the-loop**: Pause execution at breakpoints to allow human review or intervention.
- **Streaming**: Stream token-by-token output and intermediate steps in real time.
- **Durable execution**: Build agents that persist state and can resume from interruptions.
- **Memory management**: Implement short-term working memory and long-term session memory.

### 2. Observability with LangSmith
- **Tracing**: Automatically capture and visualize the complete execution trace of agent runs.
- **Debugging**: View step-by-step agent reasoning, state transformations, and tool calls.
- **Performance monitoring**: Track latency, cost, token usage, and error rates.
- **Alerting**: Set up dashboards and alerts for business-critical metrics.
- **Zero overhead**: Async callback architecture ensures no performance impact on production agents.
- **Framework agnostic**: Works with any LLM framework via environment variables or SDK integration.

## Scope

This skill applies to:
- **Single-agent workflows** with complex decision logic
- **Multi-agent systems** where agents coordinate via shared state
- **Agentic RAG pipelines** with tool-augmented retrieval and reasoning
- **Hierarchical agents** (orchestrator + sub-agents)
- **Task automation** requiring durable, long-running execution
- **Development-time observability** for debugging and optimization

## Non-Scope

- High-level agent abstractions (use LangChain's `AgentExecutor` if you need pre-configured loops)
- Evaluation pipelines (covered under RAG/evaluation skills)
- Deployment infrastructure (LangSmith Agent Server is separate)
- LLM fine-tuning or model selection strategies

## Related Skills
- **Agent Framework (LangChain)**: Provides higher-level abstractions; LangGraph is the underlying orchestration layer
- **RAG**: LangGraph can enhance RAG pipelines with multi-step reasoning and tool integration
- **A2A Communication**: LangGraph agents can use A2A protocols for inter-agent coordination

## Success Criteria
You have successfully applied this skill when you can:
1. Define a multi-step agent workflow as a StateGraph with explicit nodes, edges, and state schema
2. Implement human-in-the-loop checkpoints to pause and inspect agent state
3. Enable streaming of agent output to show reasoning in real time
4. Set up LangSmith tracing with a single environment variable
5. Analyze agent behavior in LangSmith UI to debug failures and optimize performance
6. Deploy a durable agent that resumes from interruptions without losing context
