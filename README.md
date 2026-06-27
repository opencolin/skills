# opencolin/skills

A public collection of agent skills by Colin and collaborating coding agents.

Skills are small, reusable folders that teach an AI agent how to perform a specific workflow. Each skill lives in its own top-level directory and includes a required `SKILL.md` file plus optional metadata, references, scripts, and assets.

Landing page: [opencolin.github.io/skills](https://opencolin.github.io/skills/)

## Install

Install every skill in this repository:

```bash
npx skills add opencolin/skills
```

Or clone and copy selected skills into Codex:

```bash
git clone https://github.com/opencolin/skills.git
cd skills
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

### DevRel & Events

| Skill | Description |
|---|---|
| [`ambassador-program-builder`](ambassador-program-builder/SKILL.md) | Build a complete ambassador program for developer communities, DevRel programs, or AI/web3 ecosystems. |
| [`community-launch-kit`](community-launch-kit/SKILL.md) | Generate a server structure, welcome message, onboarding flow, and 30-day content calendar for a developer community. |
| [`devrel-email-sequence`](devrel-email-sequence/SKILL.md) | Generate a 3-5 email developer relations sequence with subject lines, preview text, and full body copy. |
| [`devrel-strategy-doc`](devrel-strategy-doc/SKILL.md) | Generate a DevRel strategy document with OKRs, 90-day plan, channel strategy, and budget framework. |
| [`event-brief-generator`](event-brief-generator/SKILL.md) | Generate a Luma-ready event description, email blast copy, and LinkedIn plus X/Twitter social copy. |
| [`hackathon-rubric-builder`](hackathon-rubric-builder/SKILL.md) | Build a hackathon judging rubric, per-category scoring guide, and judge briefing doc. |
| [`speaker-outreach-dm`](speaker-outreach-dm/SKILL.md) | Generate personalized outreach messages to recruit speakers or panelists for developer events. |
| [`sponsor-pitch-deck`](sponsor-pitch-deck/SKILL.md) | Generate a sponsor one-pager with tiered pricing, audience value props, and a cold outreach email. |

### Event-Led GTM And AI Systems

| Skill | Description |
|---|---|
| [`hackathon-in-a-box`](hackathon-in-a-box/SKILL.md) | Plan and run a developer hackathon or AI builder event end-to-end with sponsor-aligned outcomes. |
| [`devrel-as-a-service-proposal`](devrel-as-a-service-proposal/SKILL.md) | Draft a fractional DevRel SOW with activation-funnel KPIs, tiered pricing, and kill-switches. |
| [`agentic-engineering-audit`](agentic-engineering-audit/SKILL.md) | Score an AI agent across nine pillars and prescribe three highest-ROI fixes. |
| [`founder-stage-diagnosis`](founder-stage-diagnosis/SKILL.md) | Diagnose true startup stage and produce a focused weekly action list for AI-native founders. |
| [`voice-agent-spec`](voice-agent-spec/SKILL.md) | Spec a production voice agent end-to-end with latency budget, eval harness, and runnable starter. |
| [`inference-stack-picker`](inference-stack-picker/SKILL.md) | Pick an LLM inference stack with cost-per-million math and a migration ladder. |

### DevRel Operator Pack

| Skill | Description |
|---|---|
| [`event-page-generator`](event-page-generator/SKILL.md) | Turn a rough event idea into a publish-ready page with titles, hook, agenda, logistics, CTA, and reminder sequence. |
| [`developer-email-writer`](developer-email-writer/SKILL.md) | Write trust-first email and newsletter copy for a developer audience, with subject variants and a deliverability checklist. |
| [`devrel-content-multiplier`](devrel-content-multiplier/SKILL.md) | Turn one talk, demo, repo, or launch into a thread, LinkedIn post, newsletter blurb, and short blog post. |
| [`sponsor-outreach-kit`](sponsor-outreach-kit/SKILL.md) | Turn an event into a sponsorship package with audience snapshot, one-pager, tiered menu, and cold outreach sequence. |
| [`integration-quickstart-generator`](integration-quickstart-generator/SKILL.md) | Generate a developer-ready quickstart and starter README for any tool, API, or SDK. |

### Operator Pack

| Skill | Description |
|---|---|
| [`event-radar`](event-radar/SKILL.md) | Rank events worth attending and score event leads for follow-up. |
| [`event-leads`](event-leads/SKILL.md) | Turn a registration CSV into verified, per-sponsor-scored, influence-ranked leads. |
| [`agentic-engineering`](agentic-engineering/SKILL.md) | Working reference for building reliable autonomous coding agents and AI-native systems. |
| [`tavily-research`](tavily-research/SKILL.md) | Router for live web research via the Tavily MCP toolkit. |
| [`revops-agent-factory`](revops-agent-factory/SKILL.md) | Read-only-first RevOps, sales, and marketing agents with an enforced write gate. |
| [`transcript-to-podcast`](transcript-to-podcast/SKILL.md) | Turn any transcript or document into a realistic multi-voice podcast script. |
| [`deck-upgrader`](deck-upgrader/SKILL.md) | Upgrade a flat deck or outline into an interactive, brand-themed web slideshow spec. |
| [`demo-pitch-polish`](demo-pitch-polish/SKILL.md) | Turn a raw product demo into a punchy pitch: titles, hook, 60-second script, thumbnail, and blurb. |
| [`plugbench-runner`](plugbench-runner/SKILL.md) | Benchmark coding agents against open models and emit a ranked leaderboard. |
| [`api-key-hygiene`](api-key-hygiene/SKILL.md) | Audit a repo or environment for exposed secrets and produce a masked remediation plan. |
| [`devrel-strategy-builder`](devrel-strategy-builder/SKILL.md) | Produce an outside-in DevRel strategy and leave-behind one-pager. |
| [`community-space-ops`](community-space-ops/SKILL.md) | Plan and run a community or events space: programming, member comms, ops, scheduling, and economics. |

### Coral

| Skill | Description |
|---|---|
| [`coral`](coral/SKILL.md) | Query live sources through Coral MCP. |
| [`coral-create-source-spec`](coral-create-source-spec/SKILL.md) | Create or update a Coral source spec YAML for a custom HTTP API or local dataset. |
| [`coral-review-source-spec`](coral-review-source-spec/SKILL.md) | Review new or updated Coral source manifests and source PRs. |

## Contributing

This repo is meant to be friendly to both humans and coding agents.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), copy the template in [`templates/skill`](templates/skill), then run:

```bash
python3 scripts/validate_skills.py
```

## License

Apache 2.0. See [LICENSE](LICENSE).
