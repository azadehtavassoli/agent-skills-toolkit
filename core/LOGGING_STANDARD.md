# Logging Standard

## Required logging behavior
1. Debug logs MUST be written to a file.
2. Every operational wrapper MUST log:
   - request metadata (excluding secrets/content bodies)
   - mode toggles
   - conversion start and completion events
3. Logs MUST use UTF-8 encoding.
4. File logging MUST support parent directory creation.

## Minimum adapter contract
- Provide a function to create a logger that writes to a file handler.
- Use `logging.DEBUG` level for debug traces.
