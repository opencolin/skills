# Methodology & reference

Read this when you need the deep-screen agent prompt, the config schema, or how scoring works internally.

## Table of contents
1. Scoring model (how the 1–9 per-sponsor scores are produced)
2. Deep-screen protocol (the exact subagent fan-out + agent prompt)
3. Flag → score-cap table
4. config.json schema
5. Gotchas

---

## 1. Scoring model

Per engaged guest, for each sponsor: `clamp(2 + seniority + engagement + fit(sponsor) − edu_penalty, 1, 9)`.
- **seniority** (from title): founder/exec 3 · vp/head/director/principal 2.5 · staff/lead 2 · senior 1.5 · ic 1.2 · student 0.3.
- **engagement**: +0.6 baseline (engaged guests filled the form) · +0.6 more if VIP ticket.
- **fit(sponsor)**: `3×(any strong kw) + 2×(any medium kw) + 1×(any weak kw)` against `title + " " + company`, using that sponsor's `fit` tiers in config. This is the per-sponsor differentiator.
- **edu_penalty**: −1.5 if .edu / university (students aren't buyers).
- **company-type adjustments**: bigco → boost per `bigco_boost`; frontier lab → `frontier_penalty`; AI dev-tool → +1 to `devtool_boost` sponsors.

**Overrides (in this order):**
- **multiplier** (devrel/community/content/creator in title, or community company) → flag, keep scores.
- **investor** (VC domain or "ventures/capital" company) → all sponsors = flat 6 (partnership leverage, not consumption); apply any `vc_conflict` overrides (e.g. a hyperscaler's fund → 1 for the rival cloud).
- **competitor** (per-sponsor competitor domain/name) → that sponsor's score = 1; TYPE=Competitor (fine for the *other* sponsors).
- **employee** (sponsor domain or company == sponsor) → all scores 0, do-not-pitch. Overrides everything.

Ranking = `best` score desc, then sum across sponsors, then name. For approval/worst-leads the metric is the **sum across all sponsors** (good across the board beats one-trick).

## 2. Deep-screen protocol

Rule-based scoring trusts the registration text, so fake/inflated claims float to the top. Verify the top tier.

**Step A — pick targets.** From `leads-ranked.json`, take the union of each sponsor's top-N **eligible & unverified** leads (`verified` empty), plus all multipliers and competitors (high-stakes labels). Split into ~12–15 per batch file:
```python
# /tmp/batchK.txt lines:  SLUG ||| NAME ||| TITLE ||| COMPANY ||| LINKEDIN_URL
```

**Step B — fan out one research subagent per batch.** Each reads its batch file and writes `/tmp/screen<K>.jsonl`. Use this prompt (adjust the competitor framing to the event's sponsors):

> You are deep-screening event registrants for a sponsor lead list. Read `/tmp/batch<K>.txt` — each line is `SLUG ||| NAME ||| TITLE ||| COMPANY ||| LINKEDIN_URL`. For each person, use web search to verify identity, company, and role. **Be skeptical** — people inflate titles, claim founder status of tiny/nonexistent companies, or claim big-company employment. **Name collisions are the #1 error source**; only credit a claim if the LinkedIn slug, a company site, or a bio corroborates. Never assert what you can't confirm. Write `/tmp/screen<K>.jsonl` — exactly ONE JSON object per input lead, one per line:
> `{"slug": "...", "verdict": "V|P|U", "role": "<verified role @ company or 'unconfirmed'>", "notable": "<one fact <=15 words or '-'>", "flag": "none|fake-company|inflated-title|wrong-company|wrong-bigco|micro-company|competitor-confirmed", "influence": "high|med|low|na"}`
> verdict: V=identity+company verified · P=person found, claims plausible but unconfirmed · U=unverifiable. flag: fake-company=company has no web footprint · micro-company=real but solo/tiny shell · inflated-title=overstated vs reality · wrong-company/wrong-bigco=claimed employer not corroborated · competitor-confirmed=works at a competitor of one of the sponsors. influence: only for community/devrel/content/founder people — "high" only if genuinely notable. Produce exactly one line per input lead (use verdict U if unscreenable). Reply with only the count of lines written.

Spawn the batches in parallel. If a research subagent run fails on a spend/credit limit, do fewer batches or screen the very top ~20 inline with web search instead.

**Step C — merge.** `merge_screen.py` reads all `/tmp/screen*.jsonl`, sets verified/role/notable/flag/influence, caps scores by flag, promotes high-influence people to multipliers, and re-ranks.

## 3. Flag → score-cap table
| flag | cap applied to every sponsor score | meaning |
|---|---|---|
| fake-company | 3 | company has no real web footprint |
| micro-company / wrong-company | 4 | solo shell, or claimed employer unconfirmed |
| wrong-bigco | 5 | claimed big-co employer not corroborated |
| inflated-title | 6 | title overstated vs reality |
| (verdict U) | 4 | unverifiable / no anchor |
| competitor-confirmed | — | flag only; rule-based already handles known competitor domains |

## 4. config.json schema
- `csv_glob` — glob for auto-picking the latest CSV (e.g. `~/Downloads/My Event*Guests*.csv`).
- `engaged_statuses` — statuses that count (e.g. approved, pending_approval, waitlist).
- `status_map` — raw status → display status (approved→going, pending_approval→pending).
- `csv_columns` — map of name/email/company/title/linkedin/status/ticket → the CSV's actual column headers.
- `sponsors[]` — `{name, icp, fit:{"3":[...],"2":[...],"1":[...]}}`. The `fit` tiers are keyword substrings matched against `title + " " + company`.
- `sponsor_domains`, `sponsor_name_tokens` — employee detection.
- `bigco_boost`, `frontier_penalty` — `{sponsorName: delta}`; `devtool_boost` — `[sponsorName,...]`.
- `competitors` — `{sponsorName: {domains:[...], names:[...]}}`.
- `vc_domains`, `vc_conflict` (`{fundDomain:{sponsorName:score}}`), `bigco`, `frontier_labs`, `devtool_ai`, `freemail`.
- `multiplier_keywords` — `{title:[...], company:[...]}`.
- `ui.accent` — hex (no `#`) for spreadsheet/dashboard headers.

## 5. Gotchas
- Parse CSVs with `utf-8-sig` (Luma exports carry a BOM) — the scripts do this; if you read manually, match it.
- Names are often spelled inconsistently / blank; **dedupe by email** (the scripts do).
- LinkedIn follower counts aren't scrapable at scale — "influence" comes from the deep-screen agent's judgement, not a follower API. If the CSV has X/GitHub handles, you can add a follower-fetch pass, but most don't.
- macOS may block `~/Downloads` for shell tools (TCC) — if `open()` errors with "operation not permitted", ask the user to move the CSV into the working folder.
- Re-running `score_leads.py` overwrites verification (it's a fresh rule-based pass) — re-apply `merge_screen.py` after, or keep the prior `/tmp/screen*.jsonl` so the merge re-applies.
