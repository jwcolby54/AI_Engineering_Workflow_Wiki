# [Project Name] - [Topic] Workflow Record

**Status:** `NEEDS_REVIEW`
**Document Version:** 1.0
**Created:** [DATE]
**Revised:** [DATE]
**AI_1 (Proposing):** [Claude / ChatGPT / Codex / other]
**AI_2 (Reviewing):** [Claude / ChatGPT / Codex / other]
**Change Summary (v1.0):** Initial draft

---

# Resume Snapshot

**Current Phase:** [Proposal / Critique / Revision / Final Review / Scope Freeze / Gate / Implementation / Validation]
**Current Round:** [Round 1]
**Open Concerns:** [None / summary of unresolved BLOCKING or MAJOR concerns]
**Frozen Scope:** [No / Yes - see [Scope Freeze](#6-scope-freeze)]
**Gate Status:** [BLOCKED_PENDING_REVIEW / CLEARED / other - see [Implementation Gate](#7-implementation-gate)]
**Next Actor:** [AI_1 / AI_2 / Human]
**Next Action:** [One sentence]

**Resume Reading Order:**
1. [Objective](#1-objective)
2. [Human Requirements](#3-human-requirements)
3. [Design Review Loop](#5-design-review-loop)
4. [Scope Freeze](#6-scope-freeze)
5. [Implementation Gate](#7-implementation-gate)
6. [Next Action](#10-next-action)

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

[What engineering decision or design is being worked out in this session? Be specific enough that both AIs can evaluate proposals against it.]

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

- AI context windows are finite - keep sessions focused.
- Human remains final authority.
- Workflow must remain manually operable without special tooling.
- [Add project-specific constraints here.]

---

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

[Optional. Record Human direction given after critique and before AI_1 revision. Use this when the Human selects between options, clarifies priorities, grants a waiver, or gives authoritative guidance that AI_1 must incorporate.]

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

---

<!-- If additional rounds are needed, copy the ROUND block above and increment the number. Do not delete prior rounds. -->

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

**Approved Scope Version:** [VERSION - match Document Version above]

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

*v1.0 - [One-line session description]*
