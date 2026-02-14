# Skill: SECURITY_AND_PROMPT_INJECTION

## Purpose
Enforce security best practices and prompt injection defenses in agentic systems. Agents generate code that is resilient to semantic attacks and unsafe tool usage. :contentReference[oaicite:0]{index=0}

## When to use
- User input used in prompts
- Tool calls involving external systems
- Passing untrusted data into agents
- Generation of parsers and runners

## Hard Rules (MUST)
1. **Never trust unvalidated input.**
2. **Separate prompt generation from input.**
3. **Constrain agent roles and capabilities.**
4. **Define allow-lists for external actions and outputs.**
5. **Enforce least privilege on tools.**
6. **Sanitize all external data before reuse.** :contentReference[oaicite:1]{index=1}

## Soft Preferences (SHOULD)
- Prefer contextual whitelisting over broad blacklists.
- Prefer explicit schema validation for agent outputs.
- Prefer dual-pass auditing for high-risk operations.

## Anti-patterns
- Using raw user input in system prompts.
- Mixing trusted and untrusted sources in the same prompt context.
- Blindly executing agent outputs without validation.

## Workflow
1. Classify inputs as trusted or untrusted.
2. Apply sanitization filters.
3. Generate constrained prompt templates.
4. Validate generated outputs against schema.
5. Log and monitor unusual behaviours.

## Output Checklist
- [ ] No direct use of untrusted input
- [ ] Sanitize before use
- [ ] External actions bounded by allow-list
- [ ] Prompts contain clear role/permission statements

## Notes
Use OWASP Gen-AI security patterns, including input/output filtering and strict role behavior. :contentReference[oaicite:2]{index=2}
