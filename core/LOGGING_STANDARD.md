Here is your content formatted as a clean, copy-paste-ready Markdown file:
# LOGGING STANDARD (UV + STRUCTLOG)

## 1. Tech Stack & Environment

* **Manager:** Use `uv` for dependency management.

  ```bash
  uv add structlog
  ```

* **Engine:** Use `structlog` exclusively.
  Avoid the standard `logging` library where possible.

* **Format:** Key-Value (`logfmt`) only.
  🚫 **PROHIBITED:** JSON-lines format.

---

## 2. Mandatory Fields (Logfmt Keys)

Every log entry **must** contain:

* `timestamp` — ISO-8601 UTC
* `level` — `info`, `debug`, `error`, `warning`
* `run_id` — Unique trace ID for the current execution
* `event` — Brief `snake_case` description of the action

---

## 3. Mandatory Contexts

### Tool Calls

Must log:

* `tool_name`
* `status`
* `duration_ms`

### Reasoning

Must log:

```text
reasoning="..."
```

For:

* LLM routing decisions
* Logic branch decisions

### Errors

Must log:

* `error_type`
* `error_message`

---

## 4. Security & Redaction

### Processor Requirement

Implement a `structlog` processor to redact the following keys:

* `password`
* `token`
* `api_key`
* `secret`
* `access_token`

### Redaction Rule

Masked values must appear as:

```text
********
```

---

## 5. File & Rotation Policy (Python Implementation)

Use `logging.handlers.RotatingFileHandler` integrated into the `structlog` pipeline.

### Configuration

* **Max Size:** `10MB`

  ```
  10 * 1024 * 1024 bytes
  ```

* **Backups:** `5` files

* **Naming Convention:**

  ```
  <topic>_<component>_<date>.log
  ```

## Implementation Reference (For Copilot)
When asked to create a logger, use this pattern:

/templates/logger_template.py