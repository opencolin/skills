---
name: hackathon-in-a-box
description: Plan and run a developer hackathon, AI builder event, or sponsor-backed summit end-to-end. Produces run-of-show, judging rubric, sponsor deck outline, attendee comms, Discord/Slack channel structure, lead-scoring sheet, budget worksheet, and risk register. Use when a user wants to plan a hackathon, sponsor a builder event, run a developer event, write a judging rubric, draft event run-of-show, or critique an existing hackathon plan.
---

# Hackathon In A Box

Plan and operate a developer hackathon or AI builder event biased toward sponsor pipeline outcomes, not vanity attendance.

## Workflow

1. Gather inputs: sponsor(s) and what they sell, theme, target audience and approximate count, total budget, format (in-person / hybrid / virtual; 24h / 48h / 1-week async), and the sponsor's primary success metric (signups, integrations shipped, qualified leads, PR, hires).
2. Anchor every section to the success metric. If sponsor wants signups, weight the rubric, prizes, and comms toward signup-driving demos. Call this out explicitly.
3. Produce a single plan document covering the sections in Output Format below.
4. Use specific dates and times. Avoid placeholder ranges where a concrete number is more useful.
5. Take positions: cash > swag, working demos > slides, fewer high-value prizes > many small ones, sponsor workshops > sponsor logos, consent-based lead capture only.
6. Suggest venue and vendor *types* by city if known. Do not recommend specific named businesses unless verified.

## Output Format

Produce `hackathon-plan-<theme>.md`:

```markdown
# <Event Name> — Hackathon Plan

## North-Star Goal
<3–5 sentences tying everything to the sponsor's success metric.>

## Run of Show
| Time | Activity | Owner | Notes |
|---|---|---|---|
<T-30 days through T+14 days, hour-resolution on event days.>

## Judging Rubric
<4–6 dimensions weighted to 100 points, plus explicit anti-patterns to penalize: slide-only demos, no working code, off-theme, AI-slop pitches.>

## Sponsor Deck Outline
<10 slides max: why now, audience proof, tiered ask, what sponsor gets per tier, theme fit, logistics, past-event proof, team, risk + kill-switch, next steps.>

## Comms Templates
- Pre-event email sequence (T-21, T-7, T-1, day-of)
- Discord/Slack channel structure
- Bot prompts for team formation, check-ins, demo signup
- Post-event thank-you with leaderboard + consent CTA
- Sponsor recap email

## Lead Scoring Sheet
<CSV schema and a one-paragraph guide on filling it during demos.>
attendee_name, team, project_title, github_url, demo_video_url, technical_depth, theme_fit, contacted_consent, sponsor_priority_1_5, notes

## Budget Worksheet
| Category | $ | Notes |
|---|---:|---|
<Venue, AV, food per meal, prizes split, swag, staffing, contingency (>=10%).>

## Risk Register
| Risk | Mitigation |
|---|---|
<Top 5: attendance miss, sponsor pullout, API outage, judging dispute, no-show keynote.>
```

## Quality Bar

- Every section ties back to the sponsor's stated success metric.
- Run of show uses concrete times, not "morning" or "afternoon."
- Rubric weights add to exactly 100.
- Budget categories sum to the stated budget within 5%.
- Comms templates are copy-pasteable plain text, not vague guidance.
- No extractive lead capture. Consent-based only.
