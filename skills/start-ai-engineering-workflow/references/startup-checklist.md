# AI Engineering Workflow Startup Checklist

Use this checklist when starting, resuming, or handing off a workflow session.

## 1. Establish Paths

- Wiki root: default to `E:\AI\AI_Engineering_Workflow_Wiki`.
- Project root: the repository or folder where engineering work will happen.
- Workflow Records folder: default to `[PROJECT_ROOT]\WorkflowRecords`.
- Active Workflow Record: an existing `.md` file or a new dated file.

## 1a. Enforce ASCII-Only Text

- All Workflow artifacts must use plain ASCII only.
- Do not use smart quotes, curly apostrophes, em dashes, en dashes, Unicode arrows, math symbols, box-drawing characters, emojis, checkmark/cross icons, non-breaking spaces, or zero-width characters.
- Use ASCII replacements: `-`, `'`, `"`, `->`, `<-`, `<->`, `>=`, `<=`, `!=`, `~=`, `[OK]`, and `[NO]`.
- Normalize files to ASCII before writing them back to disk.

## 2. Establish Roles

- `AI_1 proposing`: drafts proposals, revises after critique, records reasoning.
- `AI_2 reviewing`: critiques honestly, assigns severity, confirms readiness.
- Human: final authority for requirements, waivers, scope freeze, and gate approval.

If role is unclear, ask before continuing.

## 3. Start A New Record

1. Copy `templates\AI_Workflow_Record_Template.md`.
2. Save it as `WorkflowRecords\YYYY-MM-DD_<topic>.md`.
3. Fill header fields:
   - Status: `NEEDS_REVIEW`
   - Created/Revised: current date
   - AI_1 and AI_2 names if known
   - Change Summary
4. Fill the Resume Snapshot with the current phase, current round, next actor, and next action.
5. Fill Objective, Current State, Human Requirements, Constraints, and Next Action.
6. Do not fill implementation gate approval until review and scope freeze happen.

## 4. Resume An Existing Record

Read the full record and report:

- Resume Snapshot fields and links
- Header status and document version
- Current round and latest completed section
- Open `BLOCKING` or `MAJOR` concerns
- Scope freeze status
- Implementation gate status
- Who acts next
- Exact next action

Do not continue from chat memory alone.

## 5. Bring In AI_2

Give the reviewing AI:

- Wiki path
- Active Workflow Record path
- Role: `AI_2 reviewing`
- Instruction to critique with `BLOCKING`, `MAJOR`, `MINOR`, `FUTURE`
- Reminder to update the Workflow Record, not just chat

## 6. Handoff Between AIs

Use `templates\AI_Handoff_Template.md` when the receiving AI should resume cold. The handoff should name:

- What has been done
- Current phase and round
- Open concerns
- Frozen scope, if any
- What the receiving AI must not do
- Next action

## 7. Implementation Gate

Implementation may begin only when the Workflow Record shows:

- Scope is frozen
- AI_1 decision is approved
- AI_2 decision is approved or human has explicitly waived remaining `MAJOR` concerns
- Human decision is approved
- Gate Status is cleared
