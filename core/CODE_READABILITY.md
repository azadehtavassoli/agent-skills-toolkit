# CODE READABILITY STANDARD

## Scope
- Applies to all new and modified code in this repository and downstream projects that reuse these core standards.

## Mandatory Readability Requirements
- Every module MUST include a module-level docstring describing purpose and public surface.
- Every function and method MUST include a docstring. No exceptions.
- Docstrings MUST follow Google-style structure and include `Args:` and `Returns:`; include `Raises:` when applicable.
- Inline comments MUST explain intent and non-obvious logic; they MUST prioritize why over what.
- Comment spam on self-explanatory lines is prohibited.
- Touch rule: if a function is edited and lacks a docstring, the same PR MUST add the missing docstring.

## Docstring Contract (Google Style)
- Function and method docstrings SHOULD start with a concise one-line summary.
- Docstrings SHOULD include short behavior context when summary alone is insufficient.
- `Args:` entries MUST document every argument in `name (type): description` style.
- `Returns:` MUST describe return type and value semantics.
- `Raises:` MUST be included when the function intentionally raises exceptions.

## Comment Density Guidance
- Complex logic: add high-signal comments every 2–5 lines to explain intent, tradeoffs, or algorithmic constraints.
- Standard flows: add comments per logical block (setup, core action, teardown/return).
- Trivial one-liners: avoid comments unless intent is non-obvious.

## Inline Comment Examples
# checking the results to see if it matches the request
check_result = agent.check_result(raw_results)

# creating context to be used for logging
context = {"source_id": source_id, "chunk_count": len(chunks)}

## Review Expectations
- Comments SHOULD document invariants, assumptions, and boundary behavior.
- Comments SHOULD NOT restate obvious code behavior.
- TODO notes without an issue/ticket reference SHOULD NOT be merged.

## PR Definition of Done (Readability)
- Module docstrings are present for all added/modified modules.
- Function and method docstrings are present and complete for all added/modified code.
- Complex logic includes high-signal comments per the density guidance.
- No noisy or redundant comments are introduced.
- Touch rule is satisfied for every edited function missing a prior docstring.

## Enforcement
- Reviewers and CI MUST enforce this standard on all pull requests.
