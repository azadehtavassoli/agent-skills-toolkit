# Playwright Runner Guidance

## Role
Playwright is the scenario operator, not the final presentation layer.

## Runner responsibilities
- load and validate scenario
- apply seed/bootstrap step if configured
- launch browser with fixed viewport
- execute typed actions
- wait for stable UI conditions
- capture screenshots/video/events
- write run manifest and timeline metadata

## Action design
Prefer a small typed action library:
- login
- navigate
- click
- type
- waitForSelector
- waitForText
- screenshot
- pause
- assertVisible
- assertText

## Stability rules
- use stable test selectors
- avoid brittle CSS selectors
- prefer explicit waits over arbitrary sleeps
- keep typing delay and pauses configurable in scenario
- make viewport, locale, and auth state explicit

## Recording rules
Capture at least:
- video or screencast
- step screenshots for hero moments
- run manifest
- timeline metadata

## End-to-end validation
A runner implementation is not complete until a real sample scenario is executed successfully from start to finish.
