"""
ReAct Agent Template with Logging and Structured Output
Follows agent-skills-toolkit patterns
"""
from typing import List, Optional
from pydantic import BaseModel, Field
import logging
from logging.handlers import RotatingFileHandler
import json
import uuid
from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.prompts import PromptTemplate


# Structured Output Models (MUST use Pydantic)
class AgentInput(BaseModel):
    """Input to the agent"""
    query: str = Field(description="User query to process")
    context: Optional[dict] = Field(default=None, description="Additional context")


class AgentOutput(BaseModel):
    """Output from the agent"""
    answer: str = Field(description="Agent's answer")
    sources: List[str] = Field(description="Sources used")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    request_id: str = Field(description="Unique request identifier")


# Logging Setup (MUST include file logging with debug level)
def setup_agent_logger(name: str, log_dir: str = "logs") -> logging.Logger:
    """Setup rotating file logger with debug level"""
    import os
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    
    # Rotating file handler
    file_handler = RotatingFileHandler(
        f"{log_dir}/{name}.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    
    # JSON formatter for structured logging
    formatter = logging.Formatter(
        '{"timestamp":"%(asctime)s","level":"%(levelname)s","name":"%(name)s","message":%(message)s}',
        datefmt='%Y-%m-%dT%H:%M:%S%z'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger


# Custom Callback for Agent Logging
class AgentLoggingCallback(BaseCallbackHandler):
    """Logs all agent steps, tool calls, and LLM interactions"""
    
    def __init__(self, logger: logging.Logger, request_id: str):
        self.logger = logger
        self.request_id = request_id
        self.start_time = datetime.now()
    
    def on_agent_action(self, action, **kwargs):
        """Log agent action (tool selection)"""
        self.logger.debug(json.dumps({
            "request_id": self.request_id,
            "operation": "agent_action",
            "tool_name": action.tool,
            "tool_input": str(action.tool_input),
            "log": action.log
        }))
    
    def on_tool_start(self, serialized, input_str, **kwargs):
        """Log tool execution start"""
        self.logger.debug(json.dumps({
            "request_id": self.request_id,
            "operation": "tool_start",
            "tool_name": serialized.get("name"),
            "input": input_str
        }))
    
    def on_tool_end(self, output, **kwargs):
        """Log tool execution result"""
        self.logger.debug(json.dumps({
            "request_id": self.request_id,
            "operation": "tool_end",
            "output": str(output)[:500]  # Truncate long outputs
        }))
    
    def on_tool_error(self, error, **kwargs):
        """Log tool errors"""
        self.logger.error(json.dumps({
            "request_id": self.request_id,
            "operation": "tool_error",
            "error_type": type(error).__name__,
            "error_message": str(error)
        }))
    
    def on_llm_start(self, serialized, prompts, **kwargs):
        """Log LLM call start"""
        self.logger.debug(json.dumps({
            "request_id": self.request_id,
            "operation": "llm_start",
            "model": serialized.get("name", "unknown"),
            "prompts": prompts
        }))
    
    def on_agent_finish(self, finish, **kwargs):
        """Log agent completion"""
        duration = (datetime.now() - self.start_time).total_seconds()
        self.logger.info(json.dumps({
            "request_id": self.request_id,
            "operation": "agent_finish",
            "status": "success",
            "duration_ms": duration * 1000,
            "output": str(finish.return_values)[:500]
        }))


# Mock Tools (Replace with actual tools)
def mock_search_tool(query: str) -> str:
    """Mock search tool - replace with actual implementation"""
    return f"Mock search results for: {query}"


def mock_calculator_tool(expression: str) -> str:
    """Mock calculator - replace with actual implementation"""
    try:
        result = eval(expression)  # CAUTION: Unsafe in production!
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


# Agent Setup
def create_react_agent_with_logging(
    tools: List[Tool],
    model_name: str = "gpt-4",
    temperature: float = 0.0,
    logger_name: str = "react_agent"
) -> tuple:
    """Create ReAct agent with structured logging"""
    
    logger = setup_agent_logger(logger_name)
    
    # LLM setup
    llm = ChatOpenAI(model=model_name, temperature=temperature)
    
    # ReAct prompt template
    template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
"""
    
    prompt = PromptTemplate.from_template(template)
    
    # Create agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create executor with logging
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5,
        early_stopping_method="generate",
        handle_parsing_errors=True
    )
    
    return agent_executor, logger


# Main Execution Function
def run_agent(user_input: AgentInput) -> AgentOutput:
    """Run agent with structured input/output and logging"""
    
    request_id = str(uuid.uuid4())
    
    # Define tools
    tools = [
        Tool(
            name="Search",
            func=mock_search_tool,
            description="Useful for searching information"
        ),
        Tool(
            name="Calculator",
            func=mock_calculator_tool,
            description="Useful for mathematical calculations"
        )
    ]
    
    # Create agent
    agent_executor, logger = create_react_agent_with_logging(tools)
    
    # Create logging callback
    callback = AgentLoggingCallback(logger, request_id)
    
    logger.info(json.dumps({
        "request_id": request_id,
        "operation": "agent_start",
        "input": user_input.query,
        "context": user_input.context
    }))
    
    try:
        # Execute agent
        result = agent_executor.invoke(
            {"input": user_input.query},
            config={"callbacks": [callback]}
        )
        
        # Structure output
        output = AgentOutput(
            answer=result["output"],
            sources=["tool_1", "tool_2"],  # Extract from agent execution
            confidence=0.9,  # Compute based on agent behavior
            request_id=request_id
        )
        
        return output
        
    except Exception as e:
        logger.error(json.dumps({
            "request_id": request_id,
            "operation": "agent_error",
            "error_type": type(e).__name__,
            "error_message": str(e)
        }))
        raise


# Example Usage
if __name__ == "__main__":
    # MUST use structured input (Pydantic model)
    user_input = AgentInput(
        query="What is the capital of France?",
        context={"user_id": "test_user"}
    )
    
    # Run agent
    output = run_agent(user_input)
    
    print(f"Answer: {output.answer}")
    print(f"Request ID: {output.request_id}")
    print(f"Confidence: {output.confidence}")
