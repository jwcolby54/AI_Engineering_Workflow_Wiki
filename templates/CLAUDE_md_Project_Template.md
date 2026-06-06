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

Do not begin engineering work until you have confirmed role and record location.

## Post-Clear Minimal Resume Rule

After the required wiki bootstrap above, if the first human message in a fresh
session is an absolute path to a Workflow Record ending in `.active.md`, treat
it as a minimal resume request for the current topic:

- Read that active record first.
- Treat prior chat context as unavailable.
- Do not read the paired history record unless the active record's
  "Read History Only If" section explicitly instructs you to do so.
- Do not load starter files or other workflow artifacts unless the human
  explicitly asks for a full bootstrap or the active record requires it.

## Workflow Records For This Project

Workflow Records for this project live at:
[PROJECT_ROOT]\WorkflowRecords\

Filename convention:
YYYY-MM-DD_<topic>.active.md
YYYY-MM-DD_<topic>.history.md

Optional session-starter companion:
<topic>.md

Completion, validation, or supersession is recorded in the document header state. Do not move records to archive folders unless the human explicitly establishes a project-specific archival policy.

## Template Location

To start a new Workflow Record:
E:\AI\AI_Engineering_Workflow_Wiki\templates\AI_Workflow_Record_Active_Template.md
E:\AI\AI_Engineering_Workflow_Wiki\templates\AI_Workflow_Record_History_Template.md
```
