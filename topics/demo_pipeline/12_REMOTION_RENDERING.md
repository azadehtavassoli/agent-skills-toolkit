# Remotion Rendering Guidance

## Role
Remotion turns raw scenario output into polished demo outputs.

## Responsibilities
- load raw run artifacts
- load scenario metadata
- compose title cards, captions, highlights, and transitions
- produce multiple output profiles from the same run

## Minimum reusable components
- TitleCard
- CaptionOverlay
- ZoomHighlight
- DeviceFrame (optional)
- OutroCard

## Recommended profiles
- investor_16x9
- landing_short_16x9
- social_9x16
- optional yc_16x9

## Render rules
- renderer should not invent business facts
- render logic should remain profile-driven and parameterized
- scenario data should control what is highlighted and when
- keep styling reusable across scenarios

## Validation
At least one render smoke test should prove that a scenario run can be rendered into an output file successfully.
