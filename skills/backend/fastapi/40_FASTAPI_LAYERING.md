# Skill: FASTAPI_LAYERING

## Purpose
Provide a consistent layered architecture for FastAPI backends that separates concerns, improves testability, and prevents mixing business logic directly in routes. Agents must follow this structure when generating FastAPI code.

## When to use
- Generating new FastAPI services
- Adding/refactoring endpoints
- Integrating business logic or persistence
- Designing scalable API systems

## Hard Rules (MUST)
1. **Keep routes thin.**  
   Endpoints must only handle:
   - Request validation
   - Authorization checks
   - Calling service layer
   - Response formatting  
   No complex business logic in route functions.:contentReference[oaicite:1]{index=1}

2. **Service layer for business logic.**  
   Business workflows and domain rules must be in a separate service module.  
   Routes must depend on services (injected or referenced).:contentReference[oaicite:2]{index=2}

3. **Pydantic schemas for data contracts.**  
   Request/response shapes must be defined using Pydantic types; routes use them for validation and serialization.:contentReference[oaicite:3]{index=3}

4. **No persistence in routes.**  
   Database or external system access must occur in repository/adapter layers, not in routes.:contentReference[oaicite:4]{index=4}

5. **Dependency injection for shared services.**  
   Use FastAPI’s DI (`Depends`) to inject services and shared resources.:contentReference[oaicite:5]{index=5}

## Soft Preferences (SHOULD)
- **Group by feature.**  
  Organize code by domain (users, items, auth) rather than by type alone.:contentReference[oaicite:6]{index=6}

- **Module boundaries.**  
  Endpoints, services, schemas, and data layers should be in distinct modules.:contentReference[oaicite:7]{index=7}

- **Config + settings module.**  
  Centralize app configuration (env, secrets, feature flags).:contentReference[oaicite:8]{index=8}

- **Error handling.**  
  Use centralized exception handlers or middleware for HTTP errors.

## Anti-patterns
- Business logic embedded in route handlers.:contentReference[oaicite:11]{index=11}  
- Routes that directly import database clients or ORMs.:contentReference[oaicite:12]{index=12}  
- Mixed concerns (validation + logic + persistence) in one function.

## Workflow
1. **Define Pydantic schemas.**  
   Create request/response models for validation.:contentReference[oaicite:15]{index=15}

2. **Implement services.**  
   Write async service functions encapsulating business logic.:contentReference[oaicite:16]{index=16}

3. **Write thin routes.**  
   Routes should:
   - Accept a schema
   - Call the service
   - Return a well-typed response.:contentReference[oaicite:17]{index=17}

4. **Separate persistence logic.**  
   Implement repository layer (DB access or external API clients).:contentReference[oaicite:18]{index=18}

5. **Inject dependencies.**  
   Use FastAPI `Depends` for services & shared resources.

## Output Checklist
- [ ] Routes define only I/O + DI  
- [ ] Pydantic schemas cover validation + serialization  
- [ ] Business logic lives in services layer  
- [ ] Persistence/location abstraction is separate  
- [ ] Services injected via DI  
- [ ] No forbidden patterns in routes

## Notes
This skill enforces a modular backend where responsibilities are explicit and testable. Adopted from modern FastAPI architecture best practices emphasizing separation of concerns and service layers.:contentReference[oaicite:21]{index=21}
