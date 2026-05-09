# AI Workflow Record - Update Instructions

These instructions define how a participating AI must update the Workflow Record during a session. The record is the system of record. The chat is not.

---

## The Core Rule

Write it down immediately. Do not wait until the end of the session to update the record. If a decision was made and it is not in the record, it did not happen in any durable sense.

Use timestamps at handoff points. Prefer `YYYY-MM-DD HH:MM TZ` using the Human's local timezone unless the project specifies another standard. At minimum, record the date; when multiple AI handoffs happen in one session, record the time.

---

## What To Update And When

### When you produce a proposal (AI_1)

- Add a new Round section, or use Round 1 if first.
- Add a timestamp for the proposal.
- Record the proposal, reasoning, and risks identified.
- Set status to `NEEDS_REVIEW`.
- Update document header: Status, Revised date, and Change Summary.

### When you produce a critique (AI_2)

- Add your critique under the current Round.
- Add a timestamp for the critique.
- Fill in the concern severity table. Every concern gets a severity level.
- State your recommendation.
- Update status to `NEEDS_REVISION` or note advancement.

### When the Human clarifies after critique

- Add the Human clarification under the current Round.
- Add a timestamp for the clarification.
- Record the Human's direction without rewriting prior critique.
- Keep the workflow state aligned with the current phase.

### When you produce a revision (AI_1)

- Add the revision section under the current Round.
- Add a timestamp for the revision.
- List what changed.
- For each concern from the critique, show how it was addressed or why it was not.
- Update status to `READY_FOR_FINAL_REVIEW`.

### When you produce a final review (AI_2)

- Add a timestamp for the final review.
- Confirm which concerns were resolved.
- List any remaining concerns with severity.
- State final recommendation: `IMPLEMENT_READY` or `NEEDS_REVISION`.

### When scope is frozen

- Complete the Scope Freeze section.
- Add a timestamp for scope freeze.
- List what is in scope and what is explicitly out of scope.
- Set version number.

### When gate decisions are made

- Update the Implementation Gate table.
- Add a timestamp for the gate decision.
- Record each party's decision and any notes.
- Update Gate Status field.
- If Human granted a `MAJOR` waiver, record it in the waiver table.

### When implementation completes

- Update document Status header to `IMPLEMENTED`.
- Update Revised date and Change Summary.
- Record what changed, what checks were run, and any validation gaps.

### When validation completes

- Update document Status header to `VALIDATED`.
- Note which validation criteria were met.
- Record the Human confirmation timestamp when available.

---

## What You Must Never Do

**Never silently rewrite prior rounds.**
Prior proposals, critiques, and revisions are permanent history. If a prior concern was wrong or a prior proposal was superseded, the record shows that. Add new content; do not delete old content.

**Never advance state without recording the transition.**
If the state changes from `NEEDS_REVISION` to `READY_FOR_FINAL_REVIEW`, the record must show why: a revision section must exist.

**Never implement without gate approval.**
The document gate status must show approval from AI_1, AI_2, and Human before implementation begins.

**Never embed scope changes silently.**
If you realize the scope needs to change during implementation, stop. Record the issue as a concern, start a new round, and get approval. Do not adjust implementation to compensate.

---

## Record Quality Standards

The Workflow Record will be read by:
- Future AI systems resuming the session cold
- The Human after a time gap
- Potentially, future automation tools parsing the structure

Write accordingly:
- Structured, not narrative
- Compact: every line earns its place
- Machine-readable states and severity levels using exact strings
- Dates updated whenever the document changes
- Timestamps recorded at AI handoffs, Human clarification, scope freeze, gate approval, implementation, and validation

---

## Starting A New Round

If a new round is needed, copy this block and increment the number:

```text
============================================================
ROUND [N+1]
============================================================

## AI_1 Revision (or Proposal)

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

...

## AI_2 Critique (or Final Review)

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

...

============================================================
END ROUND [N+1]
============================================================
```

Do not delete Round N. Both rounds remain in the document.
