# AGENTS.md — Project Template

Instructions: Copy this file into the root of any project directory and rename it to `AGENTS.md`.
Update the wiki path if yours differs from the default below.
Remove this instruction block before saving.

Codex reads AGENTS.md automatically at session start, including nested AGENTS.md files
in subdirectories and a global user-level ~/.codex/AGENTS.md if configured.

---

```markdown
# AI Engineering Workflow — Agent Bootstrap

This project uses the structured adversarial AI engineering workflow.
Read this file before doing anything else.

## Wiki Location

The workflow wiki lives at:
E:\AI\AI_Engineering_Workflow_Wiki\

## At The Start of Every Engineering Session

Before proposing, critiquing, or implementing anything:

1. Read E:\AI\AI_Engineering_Workflow_Wiki\index.md
2. Read E:\AI\AI_Engineering_Workflow_Wiki\governance\AI_Agent_Instructions.md
3. Read E:\AI\AI_Engineering_Workflow_Wiki\concepts\State_Definitions.md
4. Read E:\AI\AI_Engineering_Workflow_Wiki\concepts\Severity_Definitions.md

Then ask the human:
- Which role am I playing? (AI_1 proposing / AI_2 reviewing)
- Which Workflow Record are we working on, or is this a new session?

Do not begin engineering work until role and record location are confirmed.

## System Architecture

| Layer            | Purpose                          | Location |
|---|---|---|
| Wiki             | Durable knowledge and governance | E:\AI\AI_Engineering_Workflow_Wiki\ |
| AGENTS.md        | Runtime behavioral bootstrap     | [PROJECT_ROOT]\AGENTS.md |
| Workflow Records | Active engineering state         | [PROJECT_ROOT]\WorkflowRecords\ |
| Source Artifacts | Ground truth implementation      | [PROJECT_ROOT]\[source dirs] |

## Workflow Records For This Project

Workflow Records for this project live in a flat dated folder:
[PROJECT_ROOT]\WorkflowRecords\

Filename convention:
YYYY-MM-DD_<topic>.md

Completion, validation, or supersession is recorded in the document header state. Do not move records to archive folders unless the human explicitly establishes a project-specific archival policy.

## Template Location

To start a new Workflow Record:
E:\AI\AI_Engineering_Workflow_Wiki\templates\AI_Workflow_Record_Template.md

## Required Behaviors

- Read the wiki before starting. Do not rely on training knowledge of this workflow.
- Update the Workflow Record during the session, not at the end.
- Do not begin implementation without a cleared implementation gate.
- Do not silently modify frozen scope.
- Preserve all prior rounds in the Workflow Record — never overwrite history.
```

