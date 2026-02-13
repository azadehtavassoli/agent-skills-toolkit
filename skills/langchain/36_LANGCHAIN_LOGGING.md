# LangChain Agent Logging Skill
**Version:** 1.0.0  
**Purpose:** Enforce debug-level file-based logging for all LangChain agents with complete traceability

## When to Use
- All LangChain agent implementations
- Any agentic workflow requiring audit trail
- Production deployments requiring debugging capability
- Multi-agent orchestrations

## MUST Rules

### Log File Requirements
- MUST create log files with debug-level output (not just console)
- MUST include timestamps in ISO 8601 format with timezone
- MUST log to rotating file handlers (max 10MB per file, 5 backup files)
- MUST use structured logging (JSON format preferred)
- MUST NOT log sensitive data (API keys, passwords, PII)

### Required Log Fields
- `timestamp`: ISO 8601 format with timezone
- `request_id`: Unique identifier for request tracing
- `agent_type`: Name/type of agent (e.g., "ReActAgent", "PlanAndExecute")
- `operation`: Current operation (e.g., "tool_call", "llm_invoke", "state_update")
- `status`: "success", "failure", "pending"
- `duration_ms`: Operation duration in milliseconds
- `input`: Sanitized input data
- `output`: Sanitized output data
- `error_type`: Exception type if failed
- `error_message`: Error details if failed
- `tool_name`: Name of tool being called (if applicable)
- `tokens_used`: Token count (if applicable)

### Log Levels
- DEBUG: Agent steps, tool inputs/outputs, state transitions, LLM prompts
- INFO: Agent start/completion, major workflow transitions
- WARNING: Retries, fallback activations, degraded performance
- ERROR: Tool failures, LLM errors, validation failures
- CRITICAL: System-breaking failures, unrecoverable errors

## Workflow

1. **Initialize Logging at Module Level**
   ```python
   import logging
   from logging.handlers import RotatingFileHandler
   import json
   from datetime import datetime
   
   def setup_agent_logger(name: str, log_dir: str = "logs") -> logging.Logger:
       logger = logging.getLogger(name)
       logger.setLevel(logging.DEBUG)
       
       # File handler with rotation
       handler = RotatingFileHandler(
           f"{log_dir}/{name}.log",
           maxBytes=10*1024*1024,  # 10MB
           backupCount=5
       )
       handler.setLevel(logging.DEBUG)
       
       # JSON formatter
       formatter = logging.Formatter(
           '{"timestamp":"%(asctime)s","level":"%(levelname)s","message":%(message)s}'
       )
       handler.setFormatter(formatter)
       logger.addHandler(handler)
       
       return logger
   ```

2. **Create Custom Callback Handler**
   ```python
   from langchain.callbacks.base import BaseCallbackHandler
   
   class AgentLoggingCallback(BaseCallbackHandler):
       def __init__(self, logger: logging.Logger, request_id: str):
           self.logger = logger
           self.request_id = request_id
       
       def on_llm_start(self, serialized, prompts, **kwargs):
           self.logger.debug(json.dumps({
               "request_id": self.request_id,
               "operation": "llm_start",
               "prompts": prompts,
               "model": serialized.get("name", "unknown")
           }))
       
       def on_tool_start(self, serialized, input_str, **kwargs):
           self.logger.debug(json.dumps({
               "request_id": self.request_id,
               "operation": "tool_start",
               "tool_name": serialized.get("name"),
               "input": input_str
           }))
   ```

3. **Attach Logger to Agent**
   ```python
   logger = setup_agent_logger("my_agent")
   callback = AgentLoggingCallback(logger, request_id)
   
   agent_executor = AgentExecutor(
       agent=agent,
       tools=tools,
       callbacks=[callback],
       verbose=True
   )
   ```

## Output Checklist
- [ ] Log directory created and writable
- [ ] Rotating file handler configured (10MB, 5 backups)
- [ ] JSON structured logging format used
- [ ] All required fields present in log entries
- [ ] Custom callback handler attached to agent
- [ ] Sensitive data sanitized before logging
- [ ] Log levels appropriately assigned
- [ ] Request ID generated and propagated
- [ ] Error stack traces captured in ERROR/CRITICAL logs
- [ ] Log file rotation tested
