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

### DevRel & Events

| Skill | Description |
|---|---|
| [`ambassador-program-builder`](ambassador-program-builder/SKILL.md) | Build a complete ambassador program — tiers, benefits, application flow, onboarding, and tracking — for developer communities, DevRel programs, or AI/web3 ecosystems. |
| [`community-launch-kit`](community-launch-kit/SKILL.md) | Generate a Discord/Slack/Telegram server structure, welcome message, onboarding flow, and 30-day content calendar for a new developer community. |
| [`devrel-email-sequence`](devrel-email-sequence/SKILL.md) | Generate a 3–5 email developer relations sequence with subject lines, preview text, and full body copy for Beehiiv, Mailchimp, or HubSpot. |
| [`devrel-strategy-doc`](devrel-strategy-doc/SKILL.md) | Generate a complete DevRel strategy document with OKRs, 90-day plan, channel strategy, and budget framework for pitching or running a DevRel program. |
| [`event-brief-generator`](event-brief-generator/SKILL.md) | Generate a Luma-ready event description, email blast copy, and LinkedIn + X/Twitter social copy from minimal event inputs. |
| [`hackathon-rubric-builder`](hackathon-rubric-builder/SKILL.md) | Build a complete hackathon judging rubric, per-category scoring guide, and judge briefing doc for AI, web3, or general developer hackathons. |
| [`speaker-outreach-dm`](speaker-outreach-dm/SKILL.md) | Generate 3 personalized cold outreach messages to recruit speakers or panelists for developer events across iMessage, LinkedIn, Twitter/X, or email. |
| [`sponsor-pitch-deck`](sponsor-pitch-deck/SKILL.md) | Generate a sponsor one-pager with tiered pricing, audience value props, and a cold outreach email for a developer event, community, or hackathon. |

## Contributing

This repo is meant to be friendly to both humans and coding agents.

Start with [CONTRIBUTING.md](CONTRIBUTING.md), copy the template in [`templates/skill`](templates/skill), then run:

```bash
python3 scripts/validate_skills.py
```

## License

Apache 2.0. See [LICENSE](LICENSE).
