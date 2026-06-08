# CLAUDE.md - Project Template

Instructions: Copy this file into the root of any project directory and rename it to `CLAUDE.md`.
Update the wiki path if yours differs from the default below.
Remove this instruction block before saving.

---

```markdown
# AI Engineering Workflow

This project uses the structured adversarial AI engineering workflow.

## Critical Text Encoding Rule

All project Markdown, workflow records, project wikis, AI-generated docs,
comments, prompts, and code written during Workflow work must use plain ASCII
only. Do not use smart quotes, curly apostrophes, em dashes, en dashes, Unicode
arrows, math symbols, box-drawing characters, emojis, checkmark/cross icons,
non-breaking spaces, or zero-width characters.

Use ASCII replacements: `-`, `'`, `"`, `->`, `<-`, `<->`, `>=`, `<=`, `!=`,
`~=`, `[OK]`, and `[NO]`.

## Wiki Location

The workflow wiki lives at:
[path to AI_Engineering_Workflow_Wiki]

## At The Start of Every Engineering Session

Before proposing, critiquing, or implementing anything:

1. Read [path to AI_Engineering_Workflow_Wiki]\index.md
2. Read [path to AI_Engineering_Workflow_Wiki]\governance\AI_Agent_Instructions.md
3. Read [path to AI_Engineering_Workflow_Wiki]\concepts\State_Definitions.md
4. Read [path to AI_Engineering_Workflow_Wiki]\concepts\Severity_Definitions.md

Then ask the human:
- Which role am I playing? (AI_1 proposing / AI_2 reviewing)
- Which Workflow Record are we working on, or is this a new session?

Do not begin engineering work until you have confirmed role and record location.

## Workflow Records For This Project

Workflow Records for this project live at:
[PROJECT_ROOT]\WorkflowRecords\

Filename convention:
YYYY-MM-DD_<topic>.md

Completion, validation, or supersession is recorded in the document header state. Do not move records to archive folders unless the human explicitly establishes a project-specific archival policy.

## Template Location

To start a new Workflow Record:
[path to AI_Engineering_Workflow_Wiki]\docs\AI_Workflow_Record_Template.md
```
