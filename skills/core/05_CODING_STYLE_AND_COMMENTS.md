# Skill: CODING_STYLE_AND_COMMENTS

## Purpose
Ensure generated code uses consistent naming, clear structure, and meaningful comments that explain intent rather than duplicate logic. Agents must produce easily readable, maintainable, and professional quality code.

## When to use
- Every time code is generated or refactored
- When adding new functions, classes, modules
- Before writing tests and documentation

## Hard Rules (MUST)
1. **Use descriptive identifiers.**
   - Variable, function, class names convey purpose and intent. :contentReference[oaicite:9]{index=9}
2. **Follow consistent naming conventions per language.**
   - e.g., snake_case for Python functions/vars, PascalCase for classes, camelCase for JS functions. :contentReference[oaicite:10]{index=10}
3. **Never duplicate code logic in comments.**
   - Comments must explain *why* or context, not restate *what* the code is doing. :contentReference[oaicite:11]{index=11}
4. **All public APIs must include doc comments.**
   - Includes description of parameters, return values, side effects. :contentReference[oaicite:12]{index=12}
5. **Comments must be accurate and up to date.**
   - Outdated or misleading comments are worse than none. :contentReference[oaicite:13]{index=13}

## Soft Preferences (SHOULD)
- Prefer shorter functions with clear names over long, multi-purpose ones. :contentReference[oaicite:14]{index=14}
- Use consistent indentation and formatting guided by known style standards (e.g., PEP8 for Python). :contentReference[oaicite:15]{index=15}
- Group code logically (imports first, then constants, then functions). :contentReference[oaicite:16]{index=16}

## Anti-patterns
- Single-letter names unless in a well-understood context (e.g., loop indices). :contentReference[oaicite:17]{index=17}  
- Inline comments that echo code behavior without context. :contentReference[oaicite:18]{index=18}  
- Block comments unrelated to the surrounding code. :contentReference[oaicite:19]{index=19}

## Workflow
1. **Name first, code second.**
   - Choose clear identifier names before writing logic. :contentReference[oaicite:20]{index=20}
2. **Annotate intent.**
   - Write comments explaining why design decisions were made. :contentReference[oaicite:21]{index=21}
3. **Review formatting.**
   - Apply consistent indentation/spacing rules. :contentReference[oaicite:22]{index=22}
4. **Generate doc-level comments.**
   - Add doc comments for modules, classes, public methods. :contentReference[oaicite:23]{index=23}

## Output Checklist
- [ ] All names descriptive and consistent
- [ ] All public APIs documented
- [ ] Comments provide intent/context, not duplicate code
- [ ] Formatting consistent and lint-passes cleanly
- [ ] Organized imports & module structure

## Notes
This skill enforces style and readability. For language-specific conventions, fallback to official style guides (e.g., PEP8 for Python). :contentReference[oaicite:24]{index=24}
