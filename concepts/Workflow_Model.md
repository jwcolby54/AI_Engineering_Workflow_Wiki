# Workflow Model

## The Full Cycle

A complete workflow session moves through these phases in order:

```text
1. Objective Definition
2. Proposal
3. Critique
4. Human Clarification (optional)
5. Revision
6. Final Review
7. Scope Freeze
8. Implementation Gate (Human approval)
9. Implementation
10. Validation
```

Phases may not be skipped without explicit Human override. Backward movement requires a new named review round.

Each handoff point should be timestamped in the Workflow Record. Timestamps make the record easier to audit and show the actual coordination cost of the process.

---

## Phase Detail

### 1. Objective Definition

The Human defines the goal. This goes into Section 1 of the Workflow Record. It must be specific enough that both AIs can evaluate proposals against it.

### 2. Proposal

AI_1 drafts an initial proposal and records it in the Workflow Record under Round 1. The proposal must include:
- what is being proposed
- the reasoning behind it
- risks identified

State at end of phase: `NEEDS_REVIEW`

### 3. Critique

AI_2 reviews the proposal and records concerns in a severity-ranked table. Each concern gets a severity level: `BLOCKING`, `MAJOR`, `MINOR`, or `FUTURE`. AI_2 provides a recommendation.

If no `BLOCKING` or `MAJOR` concerns exist, the proposal may advance directly to scope freeze.

State at end of phase: `NEEDS_REVISION` or `IMPLEMENT_READY`

### 4. Human Clarification (Optional)

After critique and before revision, the Human may clarify priorities, choose between options, waive a `MAJOR` concern, or give authoritative direction on ambiguous issues. This is not a separate implementation phase. It is a way to make the revision more precise without starting a new round prematurely.

Human clarification must be recorded in the Workflow Record before AI_1 revises. The Human remains final authority.

State remains: `NEEDS_REVISION`

### 5. Revision

AI_1 addresses the concerns and records what changed. The revision is explicit: prior content is preserved, not overwritten.

State at end of phase: `READY_FOR_FINAL_REVIEW`

### 6. Final Review

AI_2 reviews again, confirms resolved concerns, and surfaces any remaining issues. If concerns remain:
- `BLOCKING` must be resolved; the loop repeats
- `MAJOR` may proceed only with explicit Human waiver
- `MINOR` and `FUTURE` may remain open

Maximum 3 rounds before Human deadlock resolution is mandatory.

State at end of phase: `IMPLEMENT_READY` or back to `NEEDS_REVISION`

### 7. Scope Freeze

Once both AIs agree, scope is frozen explicitly in the Workflow Record. The frozen scope defines exactly what implementation targets. Any change after freeze requires a new review round and a version increment.

### 8. Implementation Gate

All three parties approve before implementation begins:

| Party | Required |
|---|---|
| AI_1 | Yes |
| AI_2 | Yes |
| Human | Yes - final authority |

Gate status is recorded explicitly. `BLOCKED_PENDING_HUMAN_APPROVAL` means implementation must not begin.

### 9. Implementation

Implementation targets the frozen scope. If scope drift is discovered during implementation, work stops and a new review round begins.

State at end of phase: `IMPLEMENTED`

### 10. Validation

Validation criteria were defined in the Workflow Record before implementation. Validation confirms the implementation satisfies them.

State at end of phase: `VALIDATED`

---

## One Workflow Record Per Topic

Each distinct engineering topic gets its own Workflow Record. A Workflow Record is not a chat log. It is the durable session artifact for the decision under review.

When a design is complete and validated, the record is archived or left in place with terminal state recorded in the header. It is never deleted. It becomes the permanent rationale trace for that decision.

---

## Round Naming Convention

Rounds are numbered sequentially: Round 1, Round 2, Round 3. If the Human resolves a deadlock, that round is labeled: `Round 3 - Human Deadlock Resolution`.
