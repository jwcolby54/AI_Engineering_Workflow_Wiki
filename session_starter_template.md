# Session Starter Template

The session starter is the universal, vendor-neutral bootstrap. It works on any AI platform, in any session, regardless of whether a `CLAUDE.md` or `AGENTS.md` file exists.

This is the first thing the Human pastes into the AI chat. It is the activation step for the workflow.

Prefer the compact form. Use the full form for cold-start sessions, new collaborators, or long-gap resumes.

---

## Compact Form

Paste this into the AI chat and fill in the bracketed fields.

```text
This engineering session follows the AI Engineering Workflow model.

Wiki:            [path to AI_Engineering_Workflow_Wiki]
Read first:      index.md, then governance/AI_Agent_Instructions.md
Workflow Record: [full path to active .md] / [new session]
My role:         [AI_1 proposing / AI_2 reviewing]

Requirements:
- Read the wiki before proceeding. Do not rely on training knowledge of this workflow.
- Update the Workflow Record as reasoning evolves, not at the end.
- Use adversarial review semantics and severity levels (BLOCKING/MAJOR/MINOR/FUTURE).
- Respect frozen scope. Do not implement before the gate is cleared.
- Human remains final authority.
- Use plain ASCII only in all Workflow artifacts. No Unicode punctuation, arrows, math symbols, box drawing, emojis, non-breaking spaces, or zero-width characters.
- Use OS file locks for shared Workflow Record `.md` files: open locked, read or write one update, flush if writing, and always close immediately.
```

---

## Full Form

Use this for cold-start sessions, new AI collaborators, or sessions without a bootstrap file.

```text
This engineering session follows the AI Engineering Workflow model.

Wiki:
[path to AI_Engineering_Workflow_Wiki]

Read in this order before doing anything else:
1. index.md
2. governance/AI_Agent_Instructions.md
3. concepts/State_Definitions.md
4. concepts/Severity_Definitions.md

Confirm you have read the wiki before proceeding.

Session details:
Role:             [AI_1 proposing / AI_2 reviewing]
Project:          [project name]
Topic:            [engineering decision or design under review]
Workflow Record:  [full path to active .md] / [new session]

If this is a new session:
- Create a Workflow Record from templates/AI_Workflow_Record_Template.md.
- Save it to the requested WorkflowRecords location.
- Record the objective and initial proposal before requesting review.

If this is a continuing session:
- Read the Workflow Record.
- Identify the current state, gate status, and last completed round.
- Tell me where we left off before asking what to do next.

Required behaviors:
- Preserve architecture. Do not silently refactor or expand scope.
- Avoid hallucinated implementation details. Flag assumptions explicitly.
- Use adversarial review semantics. Critique honestly and do not soften BLOCKING concerns.
- Update workflow artifacts as reasoning evolves. The record is the system of record.
- Respect frozen scope and severity semantics.
- Human remains final authority.
- Use plain ASCII only in all Workflow artifacts. No Unicode punctuation, arrows, math symbols, box drawing, emojis, non-breaking spaces, or zero-width characters.
- Use OS file locks for shared Workflow Record `.md` files: open locked, read or write one update, flush if writing, and always close immediately.
```

---

## Active/History Two-File Records

When the Workflow Record uses the active/history paired convention, replace the
single `Workflow Record:` line with the following in either the compact or full form:

```text
Workflow Record (active):  [full path to .active.md]
Workflow Record (history): [full path to .history.md or "none - not yet created"]

Read the active record first. Treat it as the authoritative current working state.
Read the history record only if the active record's "Read History Only If" section
explicitly says archived context is required for your next action, or if the Human
asks you to audit prior history.

If the active record shows a prune occurred, verify current state from the active
record. Do not load the full history by default.
```

---

## Legacy Single-File Records

When the Workflow Record is a legacy single-file record (YYYY-MM-DD_<topic>.md),
use the existing `Workflow Record:` line as normal. Add this note to either form:

```text
Workflow Record: [full path to single-file .md]

This is a legacy single-file Workflow Record. If you are reading it as history
or reference only, do not convert it. If active work will resume in this record
(new round, repair, extension), convert it to the active/history two-file model
before adding new content. Conversion is mechanical - no workflow gate required.
See templates/AI_Workflow_Record_Update_Instructions.md for the conversion rule.
```

---

## When To Use Each

| Situation | Use |
|---|---|
| Normal session, bootstrap file exists (`CLAUDE.md` / `AGENTS.md`) | Compact form |
| Normal session, no bootstrap file | Compact form |
| First session with a new AI collaborator | Full form |
| Resuming after a long gap | Full form |
| Handing off between AI platforms mid-session | Full form plus `templates/AI_Handoff_Template.md` |

---

## Agent Bootstrap File Reference

Platform-specific files can auto-load at session start. They complement the session starter but do not replace it. They are convenience, not guarantee.

| Agent System | Auto-load File | Template Location |
|---|---|---|
| Claude Code | `CLAUDE.md` in project root | `templates/CLAUDE_md_Project_Template.md` |
| OpenAI Codex | `AGENTS.md` in project root | `templates/AGENTS_md_Project_Template.md` |
| ChatGPT Desktop | No dominant convention yet | Use the session starter paste |

Bootstrap files should be compact pointers to the wiki, not copies of it. If platform behavior changes, the session starter still works.

---

## Path Examples

Update the `Wiki:` line and path references for your machine.

Common paths:
- Windows: `C:\Users\[name]\AI\AI_Engineering_Workflow_Wiki\`
- macOS/Linux: `/home/[name]/AI/AI_Engineering_Workflow_Wiki/`
- Project-local docs: `[project root]/AI_Engineering_Workflow_Wiki/`
