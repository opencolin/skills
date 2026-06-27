# opencolin/skills

A public collection of agent skills by Colin and collaborating coding agents.

Skills are small, reusable folders that teach an AI agent how to perform a specific workflow. Each skill lives in its own top-level directory and includes a required `SKILL.md` file plus optional metadata, references, scripts, and assets.

## Install

Install every skill in this repository:

```bash
npx skills add opencolin/skills
```

Or clone and copy selected skills into Codex:

```bash
git clone https://github.com/opencolin/skills.git
mkdir -p ~/.codex/skills
cp -R ./agent-opportunity-audit ~/.codex/skills/
```

Restart Codex after installing new skills.

## Skills

### AI Operator Field Kit

| Skill | Description |
|---|---|
| [`agent-opportunity-audit`](agent-opportunity-audit/SKILL.md) | Audit a business, team, role, workflow, or tool stack to identify practical AI assistant and AI agent opportunities. |
| [`business-workflow-decoder`](business-workflow-decoder/SKILL.md) | Turn messy descriptions of business operations into clear, reusable workflows. |
| [`sop-from-screen-recording`](sop-from-screen-recording/SKILL.md) | Convert screen recordings, Loom transcripts, walkthrough notes, voice notes, rough demos, or process explanations into polished SOPs. |
| [`offer-sharpening-agent`](offer-sharpening-agent/SKILL.md) | Clarify and strengthen service, consulting, agency, coaching, creator, or productized-service offers. |
| [`client-delivery-copilot`](client-delivery-copilot/SKILL.md) | Turn client briefs, kickoff notes, proposals, discovery calls, scope notes, or messy project context into delivery plans and handoffs. |
| [`content-engine-builder`](content-engine-builder/SKILL.md) | Repurpose source material into a practical content engine for founders, consultants, creators, agencies, and service businesses. |
| [`meeting-to-momentum`](meeting-to-momentum/SKILL.md) | Convert meeting notes, transcripts, calls, or rough discussion notes into decisions, action items, owners, deadlines, and follow-ups. |
| [`ai-skill-writer`](ai-skill-writer/SKILL.md) | Turn recurring tasks, SOPs, workflows, prompts, business processes, or expert know-how into reusable AI skills. |

### Coral

| Skill | Description |
|---|---|
| [`coral`](coral/SKILL.md) | Query live sources through Coral MCP. |
| [`coral-create-source-spec`](coral-create-source-spec/SKILL.md) | Create or update a Coral source spec YAML for a custom HTTP API or local dataset. |
| [`coral-review-source-spec`](coral-review-source-spec/SKILL.md) | Review new or updated Coral source manifests and source PRs. |

### Operator Pack

| Skill | Description |
|---|---|
| [`event-radar`](event-radar/SKILL.md) | Rank which events to attend and who to pitch there, with a schedule and outreach starters. |
| [`event-leads`](event-leads/SKILL.md) | Turn a registration CSV into verified, per-sponsor-scored, influence-ranked leads with curated builder/judge lists. |
| [`agentic-engineering`](agentic-engineering/SKILL.md) | Working reference for building reliable autonomous coding agents and AI-native systems. |
| [`tavily-research`](tavily-research/SKILL.md) | Router for live web research via the Tavily MCP toolkit (search, extract, crawl, deep-research, fact-check, and more). |
| [`revops-agent-factory`](revops-agent-factory/SKILL.md) | Read-only-first RevOps/sales/marketing agents across Salesforce, HubSpot, and Gong, with an enforced write gate. |
| [`transcript-to-podcast`](transcript-to-podcast/SKILL.md) | Turn any transcript or document into a realistic multi-voice podcast script with a comedy dial. |
| [`deck-upgrader`](deck-upgrader/SKILL.md) | Upgrade a flat deck or outline into an interactive, brand-themed web slideshow spec. |
| [`demo-pitch-polish`](demo-pitch-polish/SKILL.md) | Turn a raw product demo into a punchy pitch: titles, hook, 60-second script, thumbnail, and blurb. |
| [`plugbench-runner`](plugbench-runner/SKILL.md) | Benchmark coding agents against open models and emit a ranked leaderboard with a recommendation. |
| [`api-key-hygiene`](api-key-hygiene/SKILL.md) | Audit a repo or environment for exposed secrets and produce a masked findings report and remediation plan. |
| [`devrel-strategy-builder`](devrel-strategy-builder/SKILL.md) | Produce an outside-in DevRel strategy and a leave-behind one-pager for a company or product. |
| [`community-space-ops`](community-space-ops/SKILL.md) | Plan and run a community or events space: programming, member comms, house ops, scheduling, and economics. |

## Contributing

This repo is meant to be friendly to both humans and coding agents.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), copy the template in [`templates/skill`](templates/skill), then run:

```bash
python3 scripts/validate_skills.py
```

## License

Apache 2.0. See [LICENSE](LICENSE).
