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

## Role Assignment For This Project

In this project, role assignments are fixed:

- Claude (this AI) is always AI_1 -- the proposing / design AI.
- Codex is always AI_2 -- the reviewing AI.

Do not ask the Human which role to play. The role is Claude = AI_1.

---

## Session Startup Modes

At the start of every session determine which mode applies before doing
anything else.

### Mode A - New Workflow Topic

Triggered ONLY when the Human says one of these phrases (case-insensitive):
  "start workflow session" / "start session" / "new workflow session"

When triggered, read the wiki bootstrap files listed in AI_Agent_Instructions.md,
then create three files:
1. WorkflowRecords/YYYY-MM-DD_<name>.active.md
2. WorkflowRecords/YYYY-MM-DD_<name>.history.md
3. WorkflowRecords/<name>.md  (Codex starter, no date prefix)

YYYY-MM-DD is today's date. <name> is the Human's session name verbatim
with spaces replaced by underscores.

### Mode B - Continuing Existing Work

Use this mode when the Human does NOT say a Mode A trigger phrase.

Look for the record by session name, then by most-recent modification date.
Report current phase, gate status, open concerns, and next action before
doing any new work. Do NOT create new Workflow Record files.

### DesignFlow Is Not A Workflow Session

DesignFlow work is not, by itself, a workflow session. If the Human asks to
create, inspect, revise, or continue a DesignFlow, do not require a Workflow
Record unless the Human also explicitly starts a workflow session.

A DesignFlow is a design conversation between AIs (and the Human) to explore
options before committing to a formal review cycle. It may produce a document
or a Codex starter block, but it does not trigger active/history record
creation or the implementation gate machinery unless the Human escalates it.

See [path to AI_Engineering_Workflow_Wiki]\concepts\DesignFlow.md for details.

### Naming Rule

The session name given by the Human is the ONLY source for file names.
Do NOT abbreviate, interpret, or invent a topic name. Use exact words, spaces
replaced by underscores, case preserved.

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
[path to AI_Engineering_Workflow_Wiki]\docs\AI_Workflow_Record_Active_Template.md
[path to AI_Engineering_Workflow_Wiki]\docs\AI_Workflow_Record_History_Template.md
```
