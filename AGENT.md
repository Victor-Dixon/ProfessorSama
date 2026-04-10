# Agent Coordination Guide

This repository operates in a multi-agent workflow. Each run must leave clear evidence and a useful handoff.

## North Stars
- `PRD.md`: product direction and phase boundaries.
- SSOT files:
  - Tutor logic: `chris_tutor_bot/tutor.py`
  - API behavior: `chris_tutor_bot/api.py`
  - Dashboard ask flow: `dashboard.html`

## Current Project Status (as of 2026-04-10)
- Dashboard Ask flow is wired to local Flask API (`POST /ask` with `{question}`).
- `/ask` now supports question-only requests and backward-compatible optional answer fields.
- CI exists for compile checks, API behavior tests (mocked), and Python LOC policy.
- No deployment pipeline is implemented yet; CI is verification-only for this phase.

## Required Run Checklist
1. Read `PRD.md` and this file before coding.
2. Confirm whether any touched file is the SSOT for the behavior you change.
3. Keep Python files under 400 LOC.
4. Run and report evidence-based checks (commands + outcomes).
5. Update docs when behavior or status changes.

## Testing Truthfulness Policy
- Do not claim manual or end-to-end testing that was not performed.
- Mark mocked tests clearly as mocked.
- Distinguish local checks from CI checks.

## Prompt for the Next Agent
Use this prompt at the start of your run:

"Read `AGENT.md` and `PRD.md`. Confirm SSOT files for your change. Make the smallest viable update, run evidence-based checks, and update project status/handoff notes so the next agent can continue without missing context."
