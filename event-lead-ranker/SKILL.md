---
name: event-lead-ranker
description: "Rank, screen, and act on event attendees as per-sponsor sales leads. Use this whenever the user has a guest/registration/attendee CSV (Luma, Eventbrite, etc.) for an event with sponsors or co-hosts and wants to: score and rank attendees per sponsor, decide who to APPROVE to hit a headcount target, find the WORST going guests to bump, web-verify/deep-screen the top leads (catch fake-company founders ranked #1), build a sortable leads dashboard, produce per-sponsor Top-N lists, or export HubSpot/Salesforce CRM files. Trigger even when the user doesn't name this skill, e.g. 'rank these leads', 'score the attendees for our sponsors', 'who should we approve', 'get us to 200 going', 'review the going list / worst leads', 'top 25 for each sponsor', 'deep screen the leads', 'build a leads dashboard', or any follow-up on an existing leads-ranked analysis. Distinct from broad attendee enrichment: this is the opinionated, repeatable scoring + approval workflow."
---

# Event Lead Ranker

Turn an event guest CSV into per-sponsor-scored, web-verified, ranked leads — and run the day-to-day
approval/review workflow. Rule-based scoring covers everyone fast; targeted web deep-screening fixes the top tier.

PII note: guest data holds emails/phones + internal sales judgments. **Keep everything local** unless the user
explicitly asks to deploy/share; if deploying a dashboard, gate it server-side (never a client-side password).

## 0. Setup (once per event)

Copy and edit the config — it holds everything event/sponsor-specific so the scripts stay generic:

```bash
SKILL=~/.claude/skills/event-lead-ranker
cp $SKILL/config.example.json ./config.json   # then edit:
```
Edit `config.json` (see `references/METHODOLOGY.md` for the full schema):
- **sponsors**: each sponsor's `name`, `icp`, and `fit` keyword tiers (`"3"`=strong, `"2"`=medium, `"1"`=weak signal in title+company). This is what makes a Fed data scientist score 9 for an MLOps platform but 3 for a copilot UI vendor.
- **sponsor_domains / sponsor_name_tokens**: emails/companies that mark someone as sponsor STAFF (score 0).
- **competitors** (per sponsor), **vc_domains**, **bigco**, **frontier_labs**, **devtool_ai**, **freemail**.
- **csv_columns**: map the CSV's column names to name/email/company/title/linkedin/status/ticket.
- **engaged_statuses** + **status_map**: which statuses count as engaged, and how they map to going/pending.

If the user gives sponsors + one-line ICPs, you can generate the `sponsors` block and competitor lists yourself —
use your knowledge of each vendor's competitive landscape (e.g. GPU clouds for an inference vendor).

## 1. Score everyone (rule-based, instant)

```bash
python $SKILL/scripts/score_leads.py --config config.json --out .
```
Scores **only engaged guests** (approved + pending; passive "invited" are noise). Writes
`leads-ranked.{json,csv,xlsx}` — one 1–9 score column per sponsor, plus type, multiplier, competitor_of, flags,
and a `best`/total ranking. Auto-flags employees (→0), competitors (→that sponsor=1), investors (→flat 6),
multipliers, students, bigco. Re-run any time a new CSV lands (it auto-picks the latest from `config.csv_glob`).

## 2. Deep-screen the top tier (web verification — do this; it catches fakes)

Rule-based scoring rewards anyone who *claims* "Founder @ AI infra startup" — several of those companies don't
exist. **Always web-verify the top leads before publishing or pitching.** Full protocol + the exact agent prompt:
**read `references/METHODOLOGY.md` → "Deep-screen protocol"**. In short:

1. Compute the union of each sponsor's top-N **unverified** leads; split into batch files `/tmp/batchN.txt`.
2. Fan out research subagents (one per batch) — each web-verifies its leads and writes `/tmp/screenN.jsonl`
   lines: `{slug, verdict(V/P/U), role, notable, flag, influence}`. Be skeptical: catch fake/micro companies,
   inflated titles, wrong-employer claims, competitors, and rate real influence for community/devrel people.
3. Merge + apply score caps (fake→3, micro/wrong→4, inflated→6, U→4) and surface new high-influence multipliers:
```bash
python $SKILL/scripts/merge_screen.py --config config.json --screen-dir /tmp --dir .
```

## 3. Dashboard + per-sponsor Top-N

```bash
python $SKILL/scripts/build_dashboard.py --config config.json --dir . --top 25
```
Writes `leads-dashboard.html` (live search, per-sponsor sort, filter chips incl Verified/Flagged/High-influence,
HubSpot+Salesforce CSV export of the *current filtered view*), `TOP-LEADS.md` (Top-N per sponsor — excludes staff,
that-sponsor competitors, investors — plus a multipliers/amplifiers list sorted by verified influence), and
`leads-top-by-sponsor.xlsx` (one tab per sponsor).

## 4. Approval workflow — who to let in

```bash
python $SKILL/scripts/approve_batch.py --config config.json --dir . --target 200   # or --count 68
```
Ranks the PENDING pool by TOTAL score across all sponsors and writes `approval-batch.csv` (the best N to approve
to hit the target "going" headcount). Sponsor staff are excluded from the count and listed separately (approve
them too — they're the co-hosts' team). Hand the emails to the user to approve in Luma (no API here).

## 5. Worst-leads review — who to bump

```bash
python $SKILL/scripts/worst_going.py --config config.json --dir . --n 40
```
Ranks the GOING pool worst-first → `worst-going-review.xlsx` (email in column A for easy copy-paste), with a
color-coded recommendation column. **Excludes sponsor staff** (never bump your co-hosts' team) and **keeps
multipliers** (low buyer-score but they amplify); flags students/competitors/inflated as bump candidates.

## Key learnings (why the workflow is shaped this way)
- **Only score "engaged" statuses.** A Luma list is mostly passive "invited" who never filled the form — pure
  noise. Engaged = approved + pending (+ waitlist).
- **Email domain is the main signal.** Most guests leave company/title blank, so the domain (company vs freemail,
  competitor, VC, .edu, bigco) carries the scoring. The form fields refine it when present.
- **Web-verify the top tier — it routinely catches fake-company "founders" ranked #1.** This is the single
  highest-value step; without it the top of every list is partly fiction.
- **Different score per sponsor.** Never one global score — the whole point is a Fed data scientist is a 9 for one
  sponsor and a 3 for another. That lives in the per-sponsor `fit` keyword tiers.
- **Keep multipliers, don't cut them.** Community/DevRel/creators score low as *buyers* but high as *amplifiers* —
  surface them separately; never auto-bump them for low score.
- **Exclude sponsor staff from bump lists** and **approve them separately** — they're the co-hosts' own team.

## Outputs cheat-sheet
`leads-ranked.{json,csv,xlsx}` (all engaged, scored) · `TOP-LEADS.md` + `leads-top-by-sponsor.xlsx` (Top-N per
sponsor + multipliers) · `leads-dashboard.html` (interactive, CRM export) · `approval-batch.csv` (who to approve)
· `worst-going-review.xlsx` (who to bump). The `leads-ranked.json` is the source of truth all later scripts read.
