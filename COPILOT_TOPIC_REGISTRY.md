# COPILOT TOPIC REGISTRY

Topic: Agent
Path: topics/agent/
Frameworks:
  - langchain (topics/agent/frameworks/langchain)
  - google-adk (topics/agent/frameworks/google-adk)
Requires:
  - core/GLOBAL_RULES.md
  - core/LOGGING_STANDARD.md
  - core/TESTING_STANDARD.md
  - core/STRUCTURED_OUTPUT_STANDARD.md

Topic: RAG
Path: topics/rag/
Frameworks:
  - shared baseline (topics/rag/shared)
Requires:
  - core/GLOBAL_RULES.md
  - core/LOGGING_STANDARD.md
  - core/TESTING_STANDARD.md
  - core/STRUCTURED_OUTPUT_STANDARD.md

Topic: FastAPI
Path: topics/fastapi/
Frameworks:
  - fastapi templates (topics/fastapi/templates)
Requires:
  - core/GLOBAL_RULES.md
  - core/LOGGING_STANDARD.md
  - core/TESTING_STANDARD.md
  - core/STRUCTURED_OUTPUT_STANDARD.md

Topic: UI
Path: topics/ui/
Frameworks:
  - streamlit (topics/ui/frameworks/streamlit)
  - gradio (topics/ui/frameworks/gradio)
Requires:
  - core/GLOBAL_RULES.md
  - core/LOGGING_STANDARD.md
  - core/TESTING_STANDARD.md
  - core/STRUCTURED_OUTPUT_STANDARD.md
