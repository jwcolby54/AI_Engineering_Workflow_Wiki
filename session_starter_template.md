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
