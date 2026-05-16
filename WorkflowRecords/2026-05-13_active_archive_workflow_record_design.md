# AI Engineering Workflow Wiki - Active/Archive Workflow Record Design

**Status:** `VALIDATED`
**Document Version:** 1.5
**Created:** 2026-05-13
**Revised:** 2026-05-13
**AI_1 (Proposing):** Codex
**AI_2 (Reviewing):** Claude
**Change Summary (v1.0):** Initial proposal - split active workflow state from completed history to reduce token load
**Change Summary (v1.1):** AI_2 critique complete - five MAJOR concerns; NEEDS_REVISION
**Change Summary (v1.2):** AI_1 revision - MAJOR concerns addressed; ready for final review
**Change Summary (v1.3):** AI_2 final review - APPROVED; one new MINOR noted; IMPLEMENT_READY
**Change Summary (v1.4):** Human approved gate; implementation in progress
**Change Summary (v1.5):** Implementation complete and validated

---

# Resume Snapshot

**Current Phase:** Complete
**Current Round:** Round 1 complete; implementation validated
**Open Concerns:** MINORs and FUTURE left open by design; none block
**Frozen Scope:** Yes - v1.3
**Gate Status:** APPROVED
**Next Actor:** None - record is terminal
**Next Action:** None

**Resume Reading Order:**
1. [Objective](#1-objective)
2. [Current State](#2-current-state)
3. [Human Requirements](#3-human-requirements)
4. [Design Review Loop](#5-design-review-loop)
5. [Scope Freeze](#6-scope-freeze)
6. [Implementation Gate](#7-implementation-gate)
7. [Next Action](#10-next-action)

---

# 0. Critical Text Encoding Rule

All content in this Workflow Record and related project artifacts must use plain
ASCII only. Do not use smart quotes, curly apostrophes, em dashes, en dashes,
Unicode arrows, math symbols, box-drawing characters, emojis, checkmark/cross
icons, non-breaking spaces, or zero-width characters.

Use ASCII replacements: `-`, `'`, `"`, `->`, `<-`, `<->`, `>=`, `<=`, `!=`,
`~=`, `[OK]`, and `[NO]`.

Before writing this file back to disk, normalize it to ASCII.

---

# 1. Objective

Design a revision to the AI Engineering Workflow Record model that reduces
token cost while preserving auditability and resumability.

The proposed direction is a two-file pattern:

- File A: active Workflow Record. It contains exactly what is required to
  continue work safely.
- File B: completed history archive. It contains material that used to be in
  File A but is no longer required to continue the current work.

As work progresses, completed material is copied from File A to the end of
File B, then removed from File A. File A remains compact and load-bearing for
current work. File B remains the complete append-only history.

This workflow will decide the exact rules, template changes, movement semantics,
resume requirements, and validation requirements for that model.

---

# 2. Current State

**Current problems being solved:**
- Current Workflow Records can become large as proposals, critiques, revisions,
  implementation checkpoints, and validation evidence accumulate.
- Both AI systems may repeatedly load completed history that is no longer needed
  for the next action.
- This increases token usage on both sides of the adversarial workflow.
- Large active records can make it harder to see current state, open concerns,
  and the next actor.
- The cost is especially visible during cross-AI handoff. Each time AI_1 appends
  completed material to the Workflow Record, AI_2 must ingest more context. Then
  AI_2 appends critique, AI_1 must ingest even more, and the cycle compounds.
- The desired optimization is not smaller history. It is a smaller active
  handoff payload while preserving full history elsewhere.

**Existing system context:**
- Wiki root: `E:\AI\AI_Engineering_Workflow_Wiki`
- Existing record template:
  `templates\AI_Workflow_Record_Template.md`
- Existing update instructions:
  `templates\AI_Workflow_Record_Update_Instructions.md`
- Relevant concepts:
  - `concepts\Context_Management.md`
  - `concepts\Artifact_Structure.md`
  - `concepts\Workflow_Model.md`
  - `concepts\State_Definitions.md`

**Relevant constraints already known:**
- The Workflow Record must remain resumable from durable files, not chat memory.
- History must not be discarded.
- Human remains final authority.
- The workflow must remain manually operable without special tooling.
- ASCII hygiene remains mandatory.

---

# 3. Human Requirements

Requirements explicitly stated by the Human. These are not negotiable by AI systems.

1. Create a new Workflow Record under
   `E:\AI\AI_Engineering_Workflow_Wiki\WorkflowRecords` to design this change.
2. Use a two-file model:
   - File A contains what is required to do and continue the work.
   - File B contains completed stuff no longer needed in File A.
3. Completed stuff comes from File A. Once copied to the end of File B, it is
   deleted from File A.
4. File A must always contain exactly what is required to continue work.
5. File B must contain all history no longer needed to be loaded every time.
6. The design must decide how this works, including what parts of File A are
   permanent, what gets moved, when movement happens, and how continuity is
   preserved.
7. The goal is to reduce token impact on both AI systems while preserving the
   engineering workflow.
8. The primary cost being reduced is repeated cross-AI handoff load. Each actor
   should receive the minimum active context needed to act safely, not the whole
   accumulated history by default.

---

# 4. Constraints

- AI context windows are finite - keep active files focused.
- Human remains final authority.
- Workflow must remain manually operable without special tooling.
- No history may be lost; material may only be moved after successful copy.
- File A must be sufficient for a cold resume.
- File B must be append-only or otherwise preserve an auditable movement history.
- The model must not create ambiguity about current state, open concerns, gate
  status, or frozen scope.
- All generated workflow artifacts must be ASCII-only.

---

# 5. Design Review Loop

============================================================
ROUND 1
============================================================

## AI_1 Proposal

**Timestamp:** 2026-05-13 -04:00

**Proposal:**
Adopt an Active Record plus Completed History model for Workflow Records.

Terminology:
- Active Record: File A. The compact, current-state workflow file that every AI
  reads first.
- History Record: File B. The append-only archive of completed sections moved
  out of File A.
- Prune Event: the controlled operation that copies completed material from
  File A to File B, verifies it was copied, and removes it from File A.
- Active Resume Core: the part of File A that is never pruned while the workflow
  is active.

Initial file naming:
- File A:
  `WorkflowRecords/YYYY-MM-DD_<topic>.active.md`
- File B:
  `WorkflowRecords/YYYY-MM-DD_<topic>.history.md`

Initial File A structure:

1. Header
   - status
   - document version
   - active/history file paths
   - created/revised dates
   - AI roles
   - compact change summary

2. Resume Snapshot
   - current phase
   - current round
   - open BLOCKING and MAJOR concerns
   - frozen scope status
   - gate status
   - next actor
   - next action
   - required read set for the next actor

3. Permanent Context
   - objective
   - current Human requirements
   - active constraints
   - project/system context required for safe continuation
   - definitions or pointers needed to avoid re-reading the whole history

4. Active Work
   - current proposal, critique, revision, implementation checkpoint, or
     validation work
   - unresolved concerns
   - current decisions awaiting Human or AI action
   - current scope freeze and gate if relevant

5. Archive Index
   - list of Prune Events
   - each entry names what was moved, when, by whom, and where in File B

Initial File B structure:

1. Header
   - matching topic id
   - pointer back to File A
   - archive creation date
   - append-only rule

2. Archive Events
   - each event contains copied completed material from File A
   - each event has timestamp, actor, reason, source section ids, and destination
     event id

3. Full Completed Material
   - resolved proposal drafts
   - resolved critique rounds
   - closed concern tables
   - superseded revisions
   - completed implementation checkpoints
   - detailed validation evidence no longer needed for current action

Prune Event rules:

1. Only completed material may be pruned.
2. Open BLOCKING or MAJOR concerns may not be pruned from File A.
3. Current frozen scope may not be pruned while implementation is active.
4. Current gate status may not be pruned while implementation or validation is
   active.
5. The latest Human requirements may not be pruned unless replaced by a compact
   authoritative summary in Permanent Context.
6. The latest accepted proposal or implementation plan may be compacted, but File
   A must keep enough detail to prevent scope drift.
7. Before deletion from File A, the copied content must exist in File B.
8. File A must record an Archive Index entry after every prune.
9. File B must be append-only during normal operation. Corrections require a new
   correction event, not silent rewrite.
10. A cold AI resume should read File A first and File B only when File A points
    to a needed archived section.

Minimum File A cold-resume invariant:
File A is valid only if an AI can answer these questions without reading File B:

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

Recommended pruning moments:

1. After AI_2 critique is resolved and AI_1 revision is accepted, move the
   superseded original proposal and resolved critique details to File B. Keep a
   compact concern-disposition table in File A.
2. After final review and scope freeze, move earlier rounds to File B. Keep the
   frozen scope, open concerns, and gate status in File A.
3. After implementation completes, move detailed implementation logs to File B.
   Keep validation requirements and unresolved validation evidence in File A.
4. After validation, File A can become a compact terminal summary plus archive
   index. File B holds the full history.

Template changes needed:

1. Add new active and history templates.
2. Add Prune Event instructions to
   `templates\AI_Workflow_Record_Update_Instructions.md`.
3. Update `concepts\Context_Management.md` to describe active/history workflow
   records.
4. Update `concepts\Artifact_Structure.md` to clarify that a Workflow Record may
   be represented by a paired active/history file set.
5. Update session starter guidance to tell agents to read the active file first
   and only read history when File A explicitly requires it.

Implementation ideas for review:

1. Add an explicit "Active Payload Budget" field to File A.
   - Example: "Target active file size: <= 250 lines after pruning."
   - This is not a hard correctness rule, but it gives agents a concrete signal
     that pruning is expected.

2. Use stable Archive Event IDs instead of relying only on Markdown headings.
   - Example: `ARCHIVE-2026-05-13-001`.
   - File A can point to event IDs, and File B can keep those event IDs even if
     headings are later adjusted.

3. Require a "Prune Safety Checklist" before deleting from File A:
   - copied to File B
   - File B event has timestamp, actor, reason, and source section ids
   - File A still answers all cold-resume invariant questions
   - no open BLOCKING or MAJOR concern was moved
   - no current Human decision was lost
   - no current next action was lost

4. Add a "Read History Only If" section to File A.
   - Example:
     - Read `ARCHIVE-2026-05-13-001` if revisiting the Round 1 rejected option.
     - Read `ARCHIVE-2026-05-13-002` if auditing validation evidence.
   - This lets the next AI avoid loading File B unless needed.

5. Treat pruning as a workflow operation, not a casual edit.
   - Pruning should be timestamped.
   - The actor should be named.
   - The reason should be stated.
   - The active file version should increment.

6. Consider a three-zone File A layout:
   - Zone 1: Always Loaded. Header, resume snapshot, objective, current Human
     requirements, current constraints, next action.
   - Zone 2: Active Work. Only the current round/checkpoint and open concerns.
   - Zone 3: Archive Index. Compact pointers to completed history in File B.

7. Consider a terminal-state behavior.
   - When a workflow reaches VALIDATED or SUPERSEDED, File A can shrink to a
     terminal summary plus archive index.
   - File B remains the full audit trail.

8. Avoid making File B a junk drawer.
   - File B should receive structured archive events, not raw chat logs.
   - Moved content should remain readable and sectioned.
   - If content is summarized instead of copied verbatim, that must be explicit
     and approved by the Human because it changes audit fidelity.

**Reasoning:**
This preserves the current workflow's core promise - durable, auditable,
resumable engineering state - while reducing repeated token load. The active file
stays small because completed material is moved out. The history file preserves
auditability because material is copied before deletion and appended with
metadata.

The design keeps manual operability by avoiding databases, automation, or custom
tools as requirements. A human or AI can perform the prune with normal file
editing. Later, automation can assist, but the governance model should not depend
on automation.

The key safety mechanism is the File A cold-resume invariant. If File A cannot
resume safely on its own, it has been over-pruned and must be repaired before
continuing.

The second key mechanism is a default-read rule: future agents read File A first,
and they read File B only when File A says archived context is required for the
next action. This directly targets the Human's token-cost concern.

**Risks Identified:**
- Over-pruning could remove context that is still needed to avoid scope drift.
- Two files may introduce synchronization errors if File A says something was
  archived but File B does not contain it.
- Append-only File B may grow large, but it is loaded rarely.
- Section anchors may break if Markdown headings are renamed after archival.
- Agents may disagree about what is "completed" without precise prune rules.
- The current state machine may need a new explicit state or field for archive
  operations.
- Human review may become harder if the active file is too compressed.
- A too-small File A could force the next AI to read File B anyway, defeating the
  token-saving goal.
- A too-large File A could become the same monolithic Workflow Record pattern
  under a new name.
- If pruning is done too frequently, the workflow may spend too much effort on
  bookkeeping instead of engineering work.

**Status:** `NEEDS_REVIEW`

---

## AI_2 Critique

**Timestamp:** 2026-05-13 -04:00

| Concern | Severity |
|---|---|
| Prune atomicity not specified: no crash-recovery protocol if a prune is interrupted mid-operation | `MAJOR` |
| Implementation ideas 1-8 not classified as required vs. optional: ambiguous scope for implementation | `MAJOR` |
| Migration path for existing single-file records not addressed | `MAJOR` |
| Cold-resume invariant has no explicit verification step inside the prune protocol | `MAJOR` |
| Session starter and AI_Agent_Instructions update not given a concrete replacement instruction | `MAJOR` |
| Archive Index in File A is unbounded; could itself become a token-cost problem on long projects | `MINOR` |
| File B append-only rule has no enforcement mechanism beyond governance convention | `MINOR` |
| Mixed-convention directory: .active/.history files will coexist with old single-file records indefinitely | `MINOR` |
| This record's own disposition under the new model is unaddressed (recursive case) | `MINOR` |
| PDF rendering of the active record (or full history) for Human review at any workflow point | `FUTURE` |

**Overall Assessment:**

The proposal is well-conceived. The core model is sound: a compact active file plus
an append-only history file with a structured prune protocol directly targets the
Human's token-cost concern without sacrificing auditability. The cold-resume invariant
(10 questions) is a strong correctness mechanism. The prune safety checklist (idea 3)
and stable archive event IDs (idea 2) are clearly necessary, not optional. The
three-zone File A layout (idea 6) is the right structure. None of the five MAJOR
concerns require architectural changes. All five require additions or clarifications.

Concern 1 - Prune atomicity:
The proposal states the copy-verify-delete order (rule 7) but does not say what the
next actor should do if interrupted. The failure mode is: File A content deleted,
Archive Index not yet updated, next AI has no pointer to moved content. The prune
protocol needs a minimal crash-recovery rule: if File A references no archive entry
for content that is missing from File A, search File B by section heading or event ID
as fallback, and write the missing Archive Index entry before continuing.

Concern 2 - Ideas classification:
Items 1-8 in "Implementation ideas for review" are a mix of required design elements
(stable Archive Event IDs, Prune Safety Checklist, three-zone layout) and optional
enhancements (Active Payload Budget field). Without classification, AI_1 cannot write
templates or wiki docs without making arbitrary scope decisions. AI_1 must mark each
idea as REQUIRED, RECOMMENDED, or OPTIONAL before a frozen scope can be written.

Concern 3 - Migration path:
The proposal introduces .active.md / .history.md naming but says nothing about existing
completed records (e.g., VALIDATED post-load finalization record). Future agents reading
the wiki's WorkflowRecords directory will see both old single-file records and new paired
files with no stated rule for which convention applies. A single migration sentence is
sufficient: e.g., "Existing single-file records are treated as legacy records. They are
not retroactively split. New records use the paired naming convention."

Concern 4 - Cold-resume invariant verification:
The 10-question invariant is the primary safety mechanism against over-pruning. The prune
protocol (prune rules and/or prune safety checklist) should include an explicit mandatory
step: after deletion from File A, verify the invariant by answering all 10 questions using
only File A. If any question cannot be answered, File A has been over-pruned and must be
repaired before any further workflow action. Currently this check is implicit at best.

Concern 5 - Session starter update:
The proposal's template change list includes "Update session starter guidance to tell
agents to read the active file first" but does not provide the concrete replacement
instruction. The session starter is the highest-impact document in the workflow because
every session begins with it. The proposal should draft the specific addition, for
example: "Workflow Record (active): [path]. Workflow Record (history): [path or none].
Read the active file first. Read history only if the active file explicitly says archived
context is required for your next action." Without this draft, the implementation step
is underspecified.

FUTURE - PDF rendering:
The Human noted that reviewing a large Markdown file is difficult and that a PDF
rendering of the active record or full history would be useful. This is out of scope
for this session. The Human confirmed it should be its own workflow. Recorded here
so it is not lost.

**Recommendation:** `NEEDS_REVISION`

No BLOCKING concerns. Five MAJOR concerns; two resolved by Human direction; three
remain for AI_1 revision. Core architecture should not change.

**Status:** `NEEDS_REVISION`

---

## Human Clarification After AI_2 Critique

**Timestamp:** 2026-05-13 -04:00
**Authority:** Human (final authority per governance model)

| Concern | Human Direction |
|---|---|
| MAJOR 1 - Prune atomicity | Prune must not delete from File A until the archive write to File B is confirmed. Write first, then delete. |
| MAJOR 3 - Migration path for legacy single-file records | Legacy records stay as-is for read-only reference. If a legacy single-file record is reopened for active work (new round, repair, extension), convert it to the two-file model before work begins. |

**AI_2 notes on implications:**

MAJOR 1 - The Human direction simplifies crash recovery significantly. If a prune is
interrupted after the File B write but before the File A delete, content exists in both
files. That state is safe: no data is lost. Recovery rule becomes: if content is found
in both File A and File B during resume, the prune was interrupted mid-delete; complete
the delete from File A and update the Archive Index before continuing. No special tooling
required.

MAJOR 3 - The Human direction means legacy records are converted lazily, only on active
reuse. This avoids a forced bulk migration and lets the new model propagate organically.
The conversion trigger is: any write action (new round, concern, repair) on a single-file
record. Read-only reference does not trigger conversion. Conversion is mechanical -- no
workflow gate required. The actor performing the conversion adds a timestamped note in
the new File A header: "Converted from legacy single-file record on [date] by [actor]."

**Open MAJOR concerns still requiring AI_1 revision:**
- MAJOR 2: Implementation ideas 1-8 not classified as required/recommended/optional
- MAJOR 4: Cold-resume invariant verification not in prune protocol as explicit step
- MAJOR 5: Session starter replacement instruction not drafted

---

## AI_1 Revision

**Timestamp:** 2026-05-13 -04:00

**Changes Made:**
- Accepted Human direction for MAJOR 1: File B write must be confirmed before
  deletion from File A.
- Accepted Human direction for MAJOR 3: legacy single-file records remain as-is
  for read-only reference and convert lazily only when reopened for active work.
- Classified implementation ideas as REQUIRED, RECOMMENDED, or OPTIONAL.
- Added an explicit mandatory cold-resume verification step to the prune
  protocol.
- Drafted concrete session starter replacement language for active/history
  records.
- Added Human-proposed gate-completion prune triggers as the preferred pruning
  schedule.

**Revised design elements:**

## Required Active/History Model Elements

These elements are required for the first implementation of the active/history
Workflow Record model:

1. Two-file model:
   - File A: active record.
   - File B: history record.

2. File A three-zone layout:
   - Zone 1: Always Loaded.
   - Zone 2: Active Work.
   - Zone 3: Archive Index.

3. Stable Archive Event IDs:
   - Format: `ARCHIVE-YYYY-MM-DD-NNN`.
   - Event IDs must remain stable after creation.
   - File A points to File B by event ID, not by fragile heading text alone.

4. Prune Safety Checklist:
   - File B event written.
   - File B event includes timestamp, actor, reason, source section ids, and
     event id.
   - File B write confirmed before File A deletion.
   - File A still answers all cold-resume invariant questions.
   - No open BLOCKING or MAJOR concern was moved.
   - No current Human decision was lost.
   - No current frozen scope, gate status, next actor, or next action was lost.

5. Cold-resume invariant verification:
   - After deletion from File A, the actor must answer all 10 cold-resume
     questions using only File A.
   - If any answer is missing or ambiguous, File A has been over-pruned.
   - The actor must repair File A before any further workflow action.

6. Default-read rule:
   - Agents read File A first.
   - Agents read File B only when File A explicitly says archived context is
     required for the next action.

7. "Read History Only If" section in File A:
   - This section lists archive event IDs that may be relevant only under
     specific conditions.
   - It prevents File B from becoming a default handoff payload.

8. Lazy legacy migration rule:
   - Existing single-file Workflow Records are legacy records.
   - Legacy records are not retroactively split for read-only reference.
   - If a legacy record is reopened for active work, convert it to the two-file
     model before work begins.
   - The conversion is mechanical and does not require a workflow gate.
   - File A records: "Converted from legacy single-file record on [date] by
     [actor]."

9. Prune operation metadata:
   - Every prune is timestamped.
   - The actor is named.
   - The reason is stated.
   - The active file version increments.

## Recommended Elements

These are recommended but not required for the first implementation:

1. Active Payload Budget:
   - Example: "Target active file size: <= 250 lines after pruning."
   - This is a tuning guideline, not a correctness rule.

2. Terminal-state compaction:
   - When a workflow reaches VALIDATED or SUPERSEDED, File A should shrink to a
     terminal summary plus archive index.
   - File B remains the full audit trail.

3. Correction events for File B:
   - File B should normally be append-only.
   - If an archive event needs correction, add a correction event instead of
     silently rewriting history.

## Optional/Future Elements

These should not block the first implementation:

1. PDF rendering of active records or full history for Human review.
2. Automation helpers for prune operations.
3. Hard line-count enforcement for Active Payload Budget.
4. Bulk conversion of all legacy records.

## Revised Prune Protocol

1. Identify completed material in File A.
2. Confirm the material is no longer required for the next action.
3. Confirm the material does not include:
   - open BLOCKING or MAJOR concerns
   - current Human binding decisions unless summarized in Zone 1
   - current frozen scope
   - current gate status
   - current next actor or next action
   - current validation blockers
4. Create the next stable Archive Event ID.
5. Append the completed material to File B under that Archive Event ID.
6. Confirm the File B write succeeded.
7. Remove the archived material from File A.
8. Add or update the Archive Index entry in File A.
9. Run the cold-resume invariant verification using File A only.
10. If the invariant fails, repair File A immediately.
11. Increment File A version and record the prune in the change summary.

## Preferred Prune Triggers

Pruning should normally happen at gate completions and state-machine phase
boundaries, not opportunistically after every edit. Gate completions are already
recorded, unambiguous, and aligned with the point where prior material becomes
less necessary for the next actor.

| Gate Event | What Can Be Pruned | What Stays In File A |
|---|---|---|
| AI_2 critique complete | Original AI_1 proposal text if no longer needed verbatim | Concern severity table and next required action |
| AI_1 revision complete | Full original proposal and full critique text | Compact concern-disposition summary and revised proposal |
| AI_2 final review complete | Revision details and resolved review discussion | Scope freeze draft, gate table, open MINOR/FUTURE concerns |
| Human gate approved | Full round history | Frozen scope, implementation plan, validation requirements |
| IMPLEMENTED | Detailed implementation logs | Validation requirements, validation evidence still needed, open gaps |
| VALIDATED | Non-terminal active work details | Terminal summary, validation summary, archive index |

The table is a default policy, not permission to over-prune. The cold-resume
invariant remains mandatory after every prune. If a gate completion occurs but
File A still needs details from the prior phase to support the next action, keep
those details in File A or replace them with a compact authoritative summary.

## Prune Recovery Rule

If a prune is interrupted after the File B write but before File A deletion,
content may temporarily exist in both files. This is safe. On resume, the actor
must:

1. Confirm the File B archive event contains the copied material.
2. Complete the File A deletion if the material is no longer active.
3. Add or repair the File A Archive Index entry.
4. Run cold-resume invariant verification before continuing.

If content is missing from both File A and File B, stop and ask the Human. Do not
reconstruct from memory unless the Human explicitly authorizes reconstruction.

## Draft Session Starter Replacement Text

Use this wording when the active/history model is available:

```text
Workflow Record (active): [path to .active.md]
Workflow Record (history): [path to .history.md or none]

Read the active Workflow Record first. Treat it as the authoritative current
working state. Read the history file only if the active record explicitly says
archived context is required for your next action, or if the Human asks you to
audit prior history.

If the active record says a prune occurred, verify current state from the active
record. Do not load the full history by default.
```

For legacy single-file records:

```text
Workflow Record: [path to single-file record]

This is a legacy single-file Workflow Record. If you are only reading it as
history, do not convert it. If active work will resume in this record, convert it
to the active/history two-file model before adding new work.
```

**Concerns Addressed:**

| Concern | Resolution |
|---|---|
| MAJOR 1 - Prune atomicity | Human direction accepted. Revised protocol requires confirmed File B write before File A deletion and adds recovery rule for duplicate-after-interruption state. |
| MAJOR 2 - Ideas not classified | Resolved. Ideas are now classified as REQUIRED, RECOMMENDED, or OPTIONAL/FUTURE. |
| MAJOR 3 - Migration path | Human direction accepted. Legacy records stay read-only unless reopened for active work; active reuse triggers mechanical conversion. |
| MAJOR 4 - Cold-resume verification | Resolved. Prune protocol now mandates answering all 10 cold-resume questions using File A only after deletion. |
| MAJOR 5 - Session starter instruction | Resolved. Draft replacement text provided for active/history and legacy single-file records. |

**Remaining Open Concerns:**

| Concern | Severity | Reason Left Open |
|---|---|---|
| Archive Index in File A may become large | `MINOR` | Mitigated by stable event IDs and "Read History Only If"; can be tuned after first implementation. |
| File B append-only rule has no technical enforcement | `MINOR` | Governance convention is acceptable for first implementation; automation can be future work. |
| Mixed legacy and paired records may coexist | `MINOR` | Human chose lazy conversion; coexistence is intentional. |
| Recursive handling of this record under the new model | `MINOR` | This record can remain legacy until reopened after the model is approved. |
| PDF rendering for Human review | `FUTURE` | Human and AI_2 agree this should be a separate workflow. |

**Status:** `READY_FOR_FINAL_REVIEW`

---

## AI_2 Final Review

**Timestamp:** 2026-05-13 -04:00
**Reviewer:** AI_2 (Claude)

**Concern disposition:**

| Original Concern | Severity | Resolution |
|---|---|---|
| Prune atomicity | `MAJOR` | RESOLVED - write-before-delete confirmed in protocol steps 5-6; recovery rule explicit; missing-from-both case handled [OK] |
| Ideas not classified | `MAJOR` | RESOLVED - all ideas classified as REQUIRED/RECOMMENDED/OPTIONAL/FUTURE [OK] |
| Migration path | `MAJOR` | RESOLVED - lazy migration rule with clear trigger (active reuse); mechanical conversion with no gate [OK] |
| Cold-resume invariant verification | `MAJOR` | RESOLVED - prune protocol step 9 requires explicit post-deletion invariant check; step 10 requires immediate repair on failure [OK] |
| Session starter instruction | `MAJOR` | RESOLVED - draft text provided for active/history model and for legacy single-file records [OK] |
| Archive Index unbounded | `MINOR` | Left open; accepted by design [OK] |
| File B append-only unenforced | `MINOR` | Left open; governance convention acceptable for first implementation [OK] |
| Mixed-convention directory | `MINOR` | Left open; intentional by Human lazy-conversion direction [OK] |
| Recursive handling of this record | `MINOR` | Left open; record stays legacy until model is approved [OK] |
| PDF rendering | `FUTURE` | Left open; separate workflow [OK] |

**New concern found in final review:**

| Concern | Severity |
|---|---|
| Prune Safety Checklist and prune protocol step 9 both require cold-resume invariant check but do not state their relationship | `MINOR` |

The Prune Safety Checklist (REQUIRED item 4) lists "File A still answers all cold-resume
invariant questions" as a pre-deletion checklist item. The Revised Prune Protocol places
the same check at step 9 -- after deletion from File A at step 7. Both checks are
correct and useful: the checklist item is a planning check (will File A still be valid?),
and step 9 is a verification check (is File A actually still valid?). However, the
revision does not state this relationship explicitly. A reader could think one of them
is redundant and skip it. Recommend that the final templates clarify the intent: the
checklist item is a pre-deletion prediction; protocol step 9 is a mandatory
post-deletion confirmation. Does not block this review.

**Overall Assessment:**
All five MAJOR concerns are fully resolved. The design is coherent and implementable.
The revised prune protocol is correct and well-ordered. The session starter draft is
concrete and covers both the new and legacy cases. The classification of REQUIRED vs.
RECOMMENDED vs. OPTIONAL/FUTURE is clear and actionable for template authors.

**AI_2 Decision:** APPROVED - IMPLEMENT_READY

**Status:** `IMPLEMENT_READY`

<!-- Additional revision and final review rounds go here as needed. Preserve prior rounds until this workflow itself approves active/history pruning semantics. -->

============================================================
END ROUND 1
============================================================

---

# 5a. Concern Severity Reference

| Severity | Meaning |
|---|---|
| `BLOCKING` | Must be resolved before forward progress |
| `MAJOR` | Should be resolved before implementation; Human waiver required if left open |
| `MINOR` | Recommended improvement; does not block |
| `FUTURE` | Valid but out of scope for this session |

---

# 6. Scope Freeze

**Timestamp:** 2026-05-13 -04:00

**Approved Scope Version:** v1.3

**Frozen Scope Covers:**
- New template: Active Workflow Record (.active.md)
- New template: History Workflow Record (.history.md)
- Updated: templates\AI_Workflow_Record_Update_Instructions.md (prune event rules and protocol)
- Updated: concepts\Context_Management.md (active/history model description)
- Updated: concepts\Artifact_Structure.md (paired file set clarification)
- Updated: session_starter_template.md (active/history and legacy-record instructions)
- Clarification of pre-deletion vs. post-deletion invariant check in templates

**Explicitly Out Of Scope:**
- PDF rendering
- Automation helpers for prune operations
- Bulk conversion of existing legacy records
- Hard line-count enforcement for active payload budget

**Rules:**
- Implementation must target this frozen scope.
- Any scope change requires a new review round and version increment.

---

# 7. Implementation Gate

Implementation is NOT permitted until all parties approve.

**Gate Timestamp:** [YYYY-MM-DD HH:MM TZ]

| Reviewer | Decision | Notes |
|---|---|---|
| AI_1 | APPROVED | Submitted v1.2 revision; all MAJOR concerns addressed |
| AI_2 | APPROVED 2026-05-13 | Final review complete; one new MINOR noted; does not block |
| Human | APPROVED 2026-05-13 | Proceed. Clarify the pre/post invariant check minor when writing templates. |

**Gate Status:** `APPROVED`

**Outstanding MAJOR waivers (if any):**

| Concern | Waiver Granted By | Reason |
|---|---|---|
| None | N/A | N/A |

---

# 8. Implementation Plan

## Deliverables
1. Active Workflow Record template.
2. History Workflow Record template.
3. Updated Workflow Record update instructions.
4. Updated context-management documentation.
5. Updated artifact-structure documentation.
6. Updated session-starter guidance if needed.

## Steps
1. Wait for AI_2 critique.
2. Revise the active/history model based on critique and Human clarification.
3. Freeze scope.
4. Obtain Human implementation approval.
5. Update wiki templates and concept docs.
6. Validate ASCII hygiene.
7. Create or update an example if approved in scope.

---

# 9. Validation Requirements

Implementation is complete when:

1. The active/history model is reviewed and approved.
2. The wiki contains enough instructions for a new AI to use the model.
3. Templates clearly distinguish File A active state from File B completed
   history.
4. Prune Event rules prevent loss of open concerns, Human decisions, frozen
   scope, gate status, and next action.
5. The model remains manually operable without custom tooling.
6. Updated wiki artifacts are ASCII-only.

---

# 10. Next Action

1. Send this v1.2 revision to AI_2 for final review.
2. Do not update wiki templates or workflow rules until final review converges
   and the Human gate is cleared.

---

---

## Implementation Checkpoint - 2026-05-13

**Actor:** AI_2 (Claude)

**Artifacts written:**

| Artifact | Action | Note |
|---|---|---|
| `templates/AI_Workflow_Record_Active_Template.md` | Created | Three-zone layout; active/history header; Archive Index; Read History Only If section |
| `templates/AI_Workflow_Record_History_Template.md` | Created | Header; append-only rule; example ARCHIVE event block; correction event example |
| `templates/AI_Workflow_Record_Update_Instructions.md` | Updated | Added active/history section; full 12-step prune protocol; pre vs. post invariant check clarification; recovery rule; legacy migration rule |
| `concepts/Context_Management.md` | Updated | Added active/history model section; default-read rule; cold-resume invariant reference; legacy conversion note |
| `concepts/Artifact_Structure.md` | Updated | Layer 4 now shows both legacy and paired filename conventions; read-active-first rule |
| `session_starter_template.md` | Updated | Added active/history starter block; added legacy single-file starter block |

**MINOR concern addressed in templates:**
The pre-deletion vs. post-deletion invariant check ambiguity (noted in final review)
is explicitly clarified in the Update Instructions:
- Step 4 of the prune protocol: pre-deletion planning check (prediction - will File A
  still be valid?)
- Step 11 of the prune protocol: post-deletion verification check (confirmation - is
  File A actually valid now?)
Both are labeled and explained as distinct, mandatory, non-skippable checks.

**Validation against Section 9 criteria:**

1. Active/history model reviewed and approved by all parties [OK]
2. Wiki contains instructions for a new AI to use the model - Update Instructions,
   Context_Management, Artifact_Structure, session starter all updated [OK]
3. Templates clearly distinguish File A active state from File B history [OK]
4. Prune Event rules prevent loss of open concerns, Human decisions, frozen scope,
   gate status, and next action - prune rules and checklist cover all [OK]
5. Model remains manually operable without custom tooling [OK]
6. All updated wiki artifacts are ASCII-only [OK]

**Status: VALIDATED**

---

*v1.0 - Active/archive Workflow Record design proposal*
*v1.1 - AI_2 critique complete; NEEDS_REVISION*
*v1.2 - AI_1 revision complete; READY_FOR_FINAL_REVIEW*
*v1.3 - AI_2 final review; IMPLEMENT_READY*
*v1.4 - Human gate approved; implementation begun*
*v1.5 - Implementation complete; VALIDATED*
