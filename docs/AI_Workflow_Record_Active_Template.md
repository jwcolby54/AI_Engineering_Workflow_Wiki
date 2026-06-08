# [Project Name] - [Topic] Active Workflow Record

**Status:** `NEEDS_REVIEW`
**Document Version:** 1.0
**Active Record:** `WorkflowRecords/YYYY-MM-DD_<topic>.active.md`
**History Record:** `WorkflowRecords/YYYY-MM-DD_<topic>.history.md`
**Created:** [DATE]
**Revised:** [DATE]
**AI_1 (Proposing):** [Claude / Codex / other]
**AI_2 (Reviewing):** [Claude / Codex / other]
**Change Summary (v1.0):** Initial draft

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

# 0a. Workflow File OS Locking Rule

This Workflow Record is a shared coordination file. If more than one agent may
read or write it, every access must use the workflow OS locking discipline:

1. Check for a lock by trying to open this file read-only with an exclusive OS
   lock.
2. If the locked read-only open fails, treat the file as busy. Do not write.
3. If the locked read-only open succeeds, read what is needed and close the file
   immediately.
4. To write, reopen this file with write-capable exclusive access, re-read the
   current contents through that locked handle, apply one update, flush, and
   close immediately.
5. Always close the file.

Never hold this file open across reasoning, chat narration, tests, source-file
edits, or long-running commands. On Windows, use `.NET FileShare.None` when
tooling allows it.

---

# 0b. Mandatory Review Before Code Changes

Do not implement, patch, refactor, or deploy code directly from chat narration.
Before any code change, the proposing AI must write a recommendation in this
Active Record, the reviewing AI must critique it with severity labels, and the
Human must provide direction or gate approval as required by workflow state.

Minimum required sequence before implementation:
1. AI_1 proposal is written in Zone 2.
2. AI_2 critique is written with severity-labeled concerns.
3. AI_1 revision is written (if required) and AI_2 final recommendation is recorded.
4. Gate state and reviewer decisions are updated in Implementation Gate.
5. Only then may implementation begin.

If urgent operational mitigation is required (for example, active outage
containment), record the mitigation and rationale in this Active Record
immediately, then open a new review round for permanent corrective action.

---

# 0c. Cold-Start Resume Rule

If this active record is provided as the first artifact in a fresh session or
after a context clear:

- Treat this file as the authoritative current workflow state.
- Read this file first.
- Do not read the paired history record unless the "Read History Only If"
  section explicitly instructs you to do so.
- Do not load a starter file or other workflow artifacts for resume unless the
  Human explicitly asks for a full bootstrap or this active record requires it.
- After any prune event, print the absolute path to this active record as the
  Human's paste-ready resume artifact.

---

# 0d. Context Trim Trigger

If the Human says `trim context`, `prune active`, or `trim context and print
resume path`, perform the workflow prune procedure for this active record.

Required final output after the prune:

```text
Read the following file:
[ABSOLUTE_PATH_TO_THIS_ACTIVE_RECORD]
```

Do not print the paired history record path as the resume artifact unless the
Human explicitly asks for the history record.

---

# ============================================================
# ZONE 1 - ALWAYS LOADED
# Never prune this zone while the workflow is active.
# ============================================================

# Resume Snapshot

**Current Phase:** [Proposal / Critique / Revision / Final Review / Gate / Implementation / Validation]
**Current Round:** [Round 1]
**Open Concerns:** [None / summary of unresolved BLOCKING or MAJOR concerns]
**Frozen Scope:** [No / Yes - v1.x]
**Gate Status:** [BLOCKED_PENDING_REVIEW / BLOCKED_PENDING_HUMAN_APPROVAL / APPROVED]
**Next Actor:** [AI_1 / AI_2 / Human]
**Next Action:** [One sentence describing exactly what to do next]

**Resume Reading Order:**
1. Resume Snapshot (this section)
2. [Objective](#1-objective)
3. [Human Requirements](#3-human-requirements)
4. [Active Work](#active-work)
5. [Read History Only If](#read-history-only-if) (check before loading history)

---

# 1. Objective

[What engineering decision or design is being worked out? Be specific enough that
both AIs can evaluate proposals against it without reading the history record.]

---

# 2. Current State

**Current problems being solved:**
-

**Existing system context:**
-

**Relevant constraints already known:**
-

---

# 3. Human Requirements

Requirements explicitly stated by the Human. These are not negotiable by AI systems.

1.
2.
3.

---

# 4. Constraints

- AI context windows are finite - keep this active file focused.
- Human remains final authority.
- Workflow must remain manually operable without special tooling.
- No history may be lost; material may only be moved after confirmed write to File B.
- [Add project-specific constraints here.]

---

# ============================================================
# ZONE 2 - ACTIVE WORK
# Contains only the current round and open concerns.
# Completed rounds are pruned to the history record.
# ============================================================

# 5. Design Review Loop

============================================================
ROUND 1
============================================================

## AI_1 Proposal

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

**Proposal:**
[Describe the proposed solution.]

**Reasoning:**
[Why this approach? What problems does it solve?]

**Risks Identified:**
-

**Status:** `NEEDS_REVIEW`

---

## AI_2 Critique

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

| Concern | Severity |
|---|---|
| [concern description] | `BLOCKING` / `MAJOR` / `MINOR` / `FUTURE` |

**Overall Assessment:**
[Summary of critique.]

**Recommendation:** `NEEDS_REVISION` / `IMPLEMENT_READY`

**Status:** `NEEDS_REVISION`

---

## Human Clarification After AI_2 Critique

**Timestamp:** [YYYY-MM-DD HH:MM TZ]
**Authority:** Human (final authority per governance model)

[Optional. Record Human direction given after critique and before AI_1 revision.]

| Concern | Human Direction |
|---|---|
| [concern] | [direction] |

---

## AI_1 Revision

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

**Changes Made:**
-

**Concerns Addressed:**

| Concern | Resolution |
|---|---|
| [concern] | [how it was resolved] |

**Remaining Open Concerns:**

| Concern | Severity | Reason Left Open |
|---|---|---|
| [concern] | `MINOR` / `FUTURE` / waived `MAJOR` | [reason] |

**Status:** `READY_FOR_FINAL_REVIEW`

---

## AI_2 Final Review

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

**Resolved Concerns Confirmed:**
-

**Remaining Concerns:**

| Concern | Severity |
|---|---|
| [concern] | `MINOR` / `FUTURE` |

**Final Recommendation:** `IMPLEMENT_READY` / `NEEDS_REVISION`

============================================================
END ROUND 1
============================================================

<!-- When Round 1 is complete and scope is frozen, prune this round to the history
     record. Keep a compact concern-disposition table here in Zone 2 if needed for
     scope drift protection. See Prune Event instructions in
     docs/AI_Workflow_Record_Update_Instructions.md. -->

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

**Timestamp:** [YYYY-MM-DD HH:MM TZ]

**Approved Scope Version:** [VERSION]

**Frozen Scope Covers:**
-

**Explicitly Out Of Scope:**
-

**Rules:**
- Implementation must target this frozen scope.
- Any scope change requires a new review round and version increment.

---

# 7. Implementation Gate

Implementation is NOT permitted until all parties approve.

**Gate Timestamp:** [YYYY-MM-DD HH:MM TZ]

| Reviewer | Decision | Notes |
|---|---|---|
| AI_1 | PENDING | |
| AI_2 | PENDING | |
| Human | PENDING | |

**Gate Status:** `BLOCKED_PENDING_REVIEW`

**Outstanding MAJOR waivers (if any):**

| Concern | Waiver Granted By | Reason |
|---|---|---|
| None | N/A | N/A |

---

# 8. Implementation Plan

## Deliverables
1.

## Steps
1.

---

# 9. Validation Requirements

Implementation is complete when:

1.
2.
3.

---

# 10. Next Action

1.

---

# ============================================================
# ZONE 3 - ARCHIVE INDEX
# Compact pointers to completed history in the history record.
# Grows as rounds are pruned. Read history only when directed below.
# ============================================================

# Archive Index

| Event ID | Timestamp | Actor | What Was Moved |
|---|---|---|---|
| [none yet] | | | |

---

# Read History Only If

[List specific conditions under which the next actor should read the history record.
Be specific. Default is: do NOT read history unless listed here.]

- Read `ARCHIVE-[ID]` if [specific condition - e.g., "revisiting the Round 1 rejected option"].

---

*v1.0 - [One-line session description]*
