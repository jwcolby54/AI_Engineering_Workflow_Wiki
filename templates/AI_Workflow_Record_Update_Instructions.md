# AI Workflow Record - Update Instructions

These instructions define how a participating AI must update the Workflow Record during a session. The record is the system of record. The chat is not.

---

## The Core Rule

Write it down immediately. Do not wait until the end of the session to update the record. If a decision was made and it is not in the record, it did not happen in any durable sense.

Use timestamps at handoff points. Prefer `YYYY-MM-DD HH:MM TZ` using the Human's local timezone unless the project specifies another standard. At minimum, record the date; when multiple AI handoffs happen in one session, record the time.

---

## Critical Text Encoding Rule

All Workflow Record updates must use plain ASCII only. Do not use smart quotes,
curly apostrophes, em dashes, en dashes, Unicode arrows, math symbols,
box-drawing characters, emojis, checkmark/cross icons, non-breaking spaces, or
zero-width characters.

Use ASCII replacements: `-`, `'`, `"`, `->`, `<-`, `<->`, `>=`, `<=`, `!=`,
`~=`, `[OK]`, and `[NO]`.

Before saving the Workflow Record, normalize it to ASCII.

---

## OS File Locking Rule

Normal Workflow Record `.md` files are shared coordination artifacts. When two
or more agents may read or write the same record, the record must be opened with
an operating-system lock and closed immediately.

Required access pattern:

1. Check for a lock by trying to open the Workflow Record read-only with an
   exclusive OS lock.
2. If the locked read-only open fails, treat the file as busy. Do not write.
   Wait and retry later.
3. If the locked read-only open succeeds, read what is needed and close the file
   immediately.
4. To write, reopen the Workflow Record with write-capable exclusive access,
   re-read the current contents through that locked handle, apply exactly one
   update, flush the write, and close immediately.
5. Always close the file.

The Workflow Record must not be held open between agent reasoning steps, chat
updates, tests, source-file edits, long-running commands, or any other work
outside the single read or write operation.

On Windows, the intended implementation is `.NET FileShare.None` for the locked
open. The rule is cooperative: it works only if all participating agents follow
the same locked-open/close-immediately discipline.

---

## What To Update And When

### At every handoff or state change

- Update the Resume Snapshot near the top of the record.
- Keep `Current Phase`, `Current Round`, `Open Concerns`, `Frozen Scope`, `Gate Status`, `Next Actor`, and `Next Action` current.
- Use the snapshot links as the preferred pickup path for a cold AI. Do not use line-number links because line numbers change whenever the record is edited.

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
- Prompt the Human to commit project artifacts to git if not already done.

### When validation completes

- Update document Status header to `VALIDATED`.
- Note which validation criteria were met.
- Record the Human confirmation timestamp when available.
- Prompt the Human to commit and push all project artifacts to git.

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

## Active/History Two-File Records

When using the active/history model, the active record (.active.md) is the
authoritative current state. The history record (.history.md) holds completed
material that was pruned from the active record.

Read the active record first. Read the history record only when the active record's
"Read History Only If" section explicitly says archived context is required for your
next action.

---

## Prune Event Protocol

A Prune Event is the controlled operation that moves completed material from the
active record to the history record. It is a workflow operation, not a casual edit.
Every prune must be timestamped, attributed to an actor, and have a stated reason.

**Pre-deletion check (planning):**
Before beginning a prune, mentally verify that removing the target material will
still leave the active record able to answer all 10 cold-resume invariant questions.
This is a prediction check - do it before touching any file.

The 10 cold-resume invariant questions (active record must answer all without
reading history):
1. What are we trying to do?
2. What is the current status?
3. What is the next action?
4. Who acts next?
5. What scope is currently approved or under review?
6. What concerns are still open?
7. What Human decisions are currently binding?
8. What files/artifacts may be changed?
9. What must not be changed?
10. Which archived history sections may be relevant if deeper context is needed?

If the pre-deletion check shows any question would become unanswerable, do not
prune. Either keep the material in the active record or write a compact summary
in Zone 1 (Permanent Context) before pruning.

**Step-by-step prune protocol:**

1. Identify completed material in the active record.
2. Confirm the material is no longer required for the next action.
3. Confirm the material does not include any of the following:
   - open BLOCKING or MAJOR concerns
   - current Human binding decisions (unless already summarized in Zone 1)
   - current frozen scope
   - current gate status
   - current next actor or next action
   - current validation blockers
4. Run the pre-deletion check (see above). If any cold-resume question fails,
   do not prune until the active record is updated to preserve the answer.
5. Generate the next stable Archive Event ID:
   format ARCHIVE-YYYY-MM-DD-NNN (NNN = 001, 002, ... in sequence per day).
6. Append the completed material to the history record under that Archive Event ID.
   Include: timestamp, actor, reason, source section IDs, content type (verbatim
   or Human-approved summary), then the copied content.
7. Confirm the history record write succeeded before touching the active record.
8. Remove the archived material from the active record.
9. Add or update the Archive Index entry in the active record (Zone 3) pointing to
   the new Archive Event ID.
10. Update the "Read History Only If" section if the archived material may be
    needed under specific future conditions.
11. Run the post-deletion verification: answer all 10 cold-resume questions using
    only the active record. This is a confirmation check - different from the
    pre-deletion prediction. If any question cannot be answered, the active record
    has been over-pruned. Repair it immediately before any further workflow action.
12. Increment the active record version and record the prune in the change summary.

Note on pre-deletion vs. post-deletion invariant checks:
Step 4 is a planning check done BEFORE deletion. It asks: "Will the active record
still be valid after this prune?" Step 11 is a verification check done AFTER
deletion. It asks: "Is the active record actually valid now?" Both checks are
required. The pre-deletion check prevents mistakes; the post-deletion check catches
them. Do not skip either.

**Prune recovery rule:**

If a prune is interrupted after the history record write (step 6) but before the
active record deletion (step 8), the content exists in both files. This is safe -
no data is lost. On resume:

1. Confirm the history record archive event contains the complete copied material.
2. Complete the active record deletion (step 8).
3. Add or repair the Archive Index entry (step 9).
4. Run the post-deletion verification (step 11) before continuing.

If content is missing from BOTH the active record and the history record, stop.
Ask the Human before attempting any reconstruction. Do not reconstruct from memory
unless the Human explicitly authorizes it.

**What may not be pruned:**
- Open BLOCKING or MAJOR concerns
- Current Human binding decisions not yet summarized in Zone 1
- Current frozen scope while implementation is active
- Current gate status while implementation or validation is active
- Current next actor or next action
- The Resume Snapshot, Objective, Human Requirements, or Constraints (Zone 1)

**What may be pruned (examples):**
- Superseded proposal drafts after scope freeze
- Resolved critique rounds after revision is accepted
- Closed concern tables
- Completed implementation logs after validation
- Detailed validation evidence no longer needed for current action

---

## Recommended Prune Triggers

Gate completions are the natural prune trigger. Each gate event marks a phase
boundary where prior content becomes completed. Prune at gate completions rather
than relying on AI judgment about when material is "done enough."

Prune is expected but not mandatory at each trigger. If the active record is still
small, skip the prune -- the goal is a compact active file, not mechanical bookkeeping.

| Gate Event | What to Prune | What to Keep in File A |
|---|---|---|
| AI_2 critique complete (NEEDS_REVISION issued) | Original AI_1 proposal text | Concern severity table; open concerns |
| AI_1 revision complete (READY_FOR_FINAL_REVIEW) | Full original proposal + full critique round | Compact concern-disposition summary |
| AI_2 final review complete (IMPLEMENT_READY) | Revision details; superseded concern tables | Frozen scope; gate table; open MINORs |
| Human gate approved (implementation begins) | Full round history | Scope freeze; implementation plan; validation requirements |
| IMPLEMENTED | Detailed implementation logs | Validation requirements; any unresolved gaps |
| VALIDATED | All remaining work detail | Terminal summary; archive index |

Using gate events as triggers means the prune decision is unambiguous: the gate
cleared, so the material that led to that gate is now completed history. No judgment
call required about whether a round is "complete enough."

---

## Legacy Single-File Records

Records that use the original single-file convention (YYYY-MM-DD_<topic>.md) are
legacy records. They are not retroactively split for read-only reference.

If a legacy single-file record is reopened for active work (new round, repair,
extension), convert it to the active/history two-file model before adding new work.
Conversion is mechanical and does not require a workflow gate. The actor adds a
timestamped note in the new active record header:

"Converted from legacy single-file record on [date] by [actor]."

The original single-file record content becomes the initial content of the active
record. The history record is created empty and ready to receive pruned material
as work progresses.

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
