# Seeding and Demo Mode Guidance

## Preferred default
Use seeded state plus explicit demo-mode hooks, not live third-party auth, for normal demo execution.

## Seed responsibilities
- create or reset demo workspace state
- create deterministic users
- preload messages/documents/memory items
- simulate connected-state where appropriate
- keep fixtures auditable and easy to refresh

## Demo mode rules
- must be clearly guarded by config
- must be off by default in production paths
- must not weaken normal workspace isolation rules
- should be easy to reset or disable

## Good demo-state patterns
- pre-authorized demo workspace
- seeded connector inventory
- fixed timestamps
- stable sample content
- predictable response surfaces

## Anti-patterns
- hidden production-only bypasses
- scattered hardcoded demo branches across the app
- requiring live auth for every recorded run
