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

### DevRel Operator Pack

| Skill | Description |
|---|---|
| [`event-page-generator`](event-page-generator/SKILL.md) | Turn a rough event idea into a publish-ready page with titles, hook, agenda, logistics, CTA, and a reminder sequence. |
| [`hackathon-in-a-box`](hackathon-in-a-box/SKILL.md) | Generate a full hackathon operating plan: run-of-show, judging rubric, prize and sponsor tiers, judge brief, comms, and logistics. |
| [`developer-email-writer`](developer-email-writer/SKILL.md) | Write trust-first email and newsletter copy for a developer audience, with subject variants and a deliverability checklist. |
| [`devrel-content-multiplier`](devrel-content-multiplier/SKILL.md) | Turn one talk, demo, repo, or launch into a thread, a LinkedIn post, a newsletter blurb, and a short blog post. |
| [`sponsor-outreach-kit`](sponsor-outreach-kit/SKILL.md) | Turn an event into a sponsorship package: audience snapshot, one-pager, tiered menu with pricing, and a cold outreach sequence. |
| [`integration-quickstart-generator`](integration-quickstart-generator/SKILL.md) | Generate a developer-ready quickstart and starter README for any tool, API, or SDK, optimized for time-to-first-success. |

## Contributing

This repo is meant to be friendly to both humans and coding agents.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), copy the template in [`templates/skill`](templates/skill), then run:

```bash
python3 scripts/validate_skills.py
```

## License

Apache 2.0. See [LICENSE](LICENSE).
