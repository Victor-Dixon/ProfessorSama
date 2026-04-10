# Product Requirements Document (PRD)

## Product
MathMentor: a middle-school math tutoring product with two interfaces:
1. Discord bot for rapid access.
2. Dashboard web UI for retention and student visibility.

## Problem
Parents and students need quick, understandable math help with transparent progress signals.

## Target Users
- Middle school students (primary end user)
- Parents/guardians (buyer)

## Phase Goals (Current)
- Connect dashboard Ask box to local tutor backend.
- Keep tutoring logic in one SSOT (`chris_tutor_bot/tutor.py`).
- Maintain stable local development and basic CI checks.

## Non-Goals (Current)
- Full production deployment automation
- Billing integration
- Image-based OCR homework input

## Functional Requirements
- `POST /ask` accepts a minimal payload `{ "question": "..." }`.
- `POST /ask` remains backward-compatible with optional `user_answer` and `correct_answer`.
- Dashboard Ask box shows loading state, then tutor explanation in-page.
- `/health` endpoint returns operational status.

## Quality Requirements
- Python source files in `chris_tutor_bot/` remain under 400 LOC each.
- CI validates compile, endpoint behavior (mocked), and LOC policy.
- Documentation reflects what is tested vs not tested.

## SSOT Rules
- Tutoring prompt and explanation behavior: `chris_tutor_bot/tutor.py`.
- API contract and endpoint behavior: `chris_tutor_bot/api.py`.
- Dashboard Ask UI flow: `dashboard.html`.

## Success Criteria for this Phase
- Dashboard can query local `/ask` successfully.
- Automated checks pass in CI.
- Project docs communicate validated state and next steps for agents.
