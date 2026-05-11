---
name: start-ai-engineering-workflow
description: Start, resume, or hand off an AI Engineering Workflow session using the local AI_Engineering_Workflow_Wiki. Use when the human wants to use the AI Engineering Workflow model, create a Workflow Record, install AGENTS.md or CLAUDE.md project bootstraps, assign AI_1 or AI_2 roles, prepare a second-AI review, resume from an existing record, or produce a paste-in session starter for another AI.
---

# Start AI Engineering Workflow

## Core Rule

Treat the wiki as the operating spec and the Workflow Record as the live state. Do not rely on memory of the workflow.

Default wiki path on this machine:

```text
E:\AI\AI_Engineering_Workflow_Wiki
```

Before proposing, reviewing, revising, or implementing, read:

1. `index.md`
2. `governance/AI_Agent_Instructions.md`
3. `concepts/State_Definitions.md`
4. `concepts/Severity_Definitions.md`
5. The active Workflow Record, if one exists

## Decide The Startup Mode

Use one of these paths:

- **New session**: create a Workflow Record from `templates/AI_Workflow_Record_Template.md`, save it under the target project's `WorkflowRecords/`, then record the objective and initial state.
- **Resume session**: read the existing Workflow Record, identify current status, gate status, latest round, next actor, and next action before doing new work.
- **Second-AI review**: give the reviewing AI the wiki path, active Workflow Record path, and role `AI_2 reviewing`; require severity-ranked critique.
- **Handoff**: use `templates/AI_Handoff_Template.md` when moving between AI platforms or when the receiving AI needs a compact resume packet.
- **Project bootstrap**: install `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code in the project root using the wiki templates.

## Quick Scaffold

Prefer the helper script when starting a project or record:

```powershell
python E:\AI\AI_Engineering_Workflow_Wiki\skills\start-ai-engineering-workflow\scripts\workflow_bootstrap.py `
  --project-root "C:\path\to\project" `
  --topic "short topic" `
  --role AI_1 `
  --install-bootstrap both
```

Useful options:

- `--workflow-record "C:\path\to\record.md"` to resume or target a specific record.
- `--reviewer-role AI_2` to emit a second-AI starter block.
- `--no-create-record` to generate starters without creating files.
- `--wiki-root "X:\path\to\AI_Engineering_Workflow_Wiki"` if the wiki moved.

The script prints paste-ready starter text for the active AI and, when requested, for the second AI.

## Manual Startup

If not using the script, load `references/startup-checklist.md` and follow it.

Minimum paste-in starter:

```text
This engineering session follows the AI Engineering Workflow model.

Wiki:            E:\AI\AI_Engineering_Workflow_Wiki
Read first:      index.md, then governance/AI_Agent_Instructions.md
Workflow Record: [full path to active .md] / [new session]
My role:         [AI_1 proposing / AI_2 reviewing]

Requirements:
- Read the wiki before proceeding. Do not rely on training knowledge of this workflow.
- Update the Workflow Record as reasoning evolves, not at the end.
- Use adversarial review semantics and severity levels (BLOCKING/MAJOR/MINOR/FUTURE).
- Respect frozen scope. Do not implement before the gate is cleared.
- Human remains final authority.
```

## Operating Discipline

- Ask the human for the role and record path if they are missing.
- Do not implement before the Workflow Record shows scope freeze and a cleared implementation gate.
- Preserve record history; append new rounds and updates instead of rewriting prior rounds.
- Keep critique adversarial and explicit. Use exact severity strings: `BLOCKING`, `MAJOR`, `MINOR`, `FUTURE`.
- Record human decisions as authoritative guidance.
- If scope changes, stop and start a new review round.

