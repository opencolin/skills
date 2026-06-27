---
name: event-radar
description: Turn a Luma/Lu.ma event URL or a city + date range into a scored, deduped lead list for AI/developer events. Use when a user wants to ingest event attendees, diff against a CRM or CSV, score leads by company stage and AI relevance, or quarantine low-confidence matches before importing to a CRM. Triggers include pull guest list, score event leads, find AI events in a city, dedupe attendees, or who from this event should I follow up with.
---

# Event Radar

Convert event attendee data into a scored, deduped, CRM-ready lead list with confidence quarantine.

## Workflow

1. Confirm inputs: source (Luma URL, pasted CSV, or city + date range), goal segment (e.g. "AI agent founders"), optional existing CRM/list to diff against, confidence threshold (default 0.7), output format.
2. Ingest attendees:
   - Luma/Lu.ma URL: open the event, extract name, headline/title, company, profile URL. If the guest list is host-only, ask the user to export from the host dashboard or paste a CSV.
   - CSV: parse into the normalized schema below.
   - City + date range: list candidate events first, have the user pick one or more, then pull attendees per event.
3. Normalize into `name, title, company, profile_url, source_url, raw`.
4. Enrich each attendee with cheap, public signals: company stage / funding, GitHub handle if discoverable from name + company, one-line "why they matter." Cache enrichment to avoid duplicate lookups.
5. Score 0.0–1.0 against the goal segment using weighted signals:
   - Title fit (0.40)
   - Company AI-relevance (0.30)
   - Company stage match (0.15)
   - Recent shipping signal in last 90 days (0.15)
6. Below threshold → quarantine with a specific reason ("no company found", "title ambiguous", "stage unknown"). Never auto-import quarantined rows.
7. If a CRM/list was provided, label each attendee `net_new`, `existing`, or `existing_stale` (no touch in 90+ days). Default import set: `net_new` + `existing_stale`.
8. Produce three artifacts and share them.

## Output Format

Produce three files:

- `<event>-import.csv` — top-scored, ready for CRM import
- `<event>-quarantine.csv` — needs human review; include a `reason` column
- `<event>-summary.md`:

```markdown
# <Event Name> — Event Radar Summary

## Snapshot
- Source: <url or path>
- Pulled: <count>
- Goal segment: <segment>
- Threshold: <value>

## Score Histogram
- High (>=threshold): <count>
- Quarantined: <count>
- Filtered out: <count>

## Top 10
| Name | Title | Company | Score | Why |
|---|---|---|---:|---|

## Diff vs CRM
- Net new: <count>
- Existing stale: <count>
- Existing fresh (skipped): <count>

## Recommended Follow-up Window
<48–72h with specific channel suggestion>
```

## Quality Bar

- Never store more than name, public title, company, and a public profile URL. Do not enrich personal emails or phone numbers.
- Cap automation at one event per minute; back off on 429.
- Confidence quarantine is non-negotiable. Do not auto-import quarantined rows even if asked.
- Every enriched field in the summary links to the source it came from.
- If the guest list is gated, ask for an export instead of trying to bypass access controls.
