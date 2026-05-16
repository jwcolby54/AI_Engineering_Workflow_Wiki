# Gate Model

## What the Implementation Gate Is

The implementation gate is a hard stop before implementation begins. No implementation may start until all three parties have explicitly approved.

| Party | Role at Gate |
|---|---|
| AI_1 (proposing AI) | Confirms proposal is implementation-ready |
| AI_2 (reviewing AI) | Confirms concerns are resolved and scope is sound |
| Human | Final authority - explicitly approves or blocks |

The gate exists because AI convergence is necessary but not sufficient. The Human may have constraints, priorities, or information that neither AI system has. The gate preserves the Human's authority to say "not yet" even when both AIs agree.

---

## Gate States

| Gate Status | Meaning |
|---|---|
| `BLOCKED_PENDING_REVIEW` | AIs have not yet converged |
| `BLOCKED_PENDING_HUMAN_APPROVAL` | Both AIs approved; Human has not acted |
| `APPROVED` | All three parties approved; implementation may begin |
| `BLOCKED_BY_HUMAN` | Human explicitly declined; implementation must not begin |

---

## What the Gate Checks

Before approving, each party should confirm:

- No `BLOCKING` concerns remain open
- `MAJOR` concerns are either resolved or have an explicit Human waiver
- Scope freeze is documented
- Validation requirements are defined (so you know what "done" means before starting)

---

## Deadlock Rule

If AI_1 and AI_2 disagree after three review rounds, the Human becomes the explicit casting authority. The Human's decision is recorded in the Workflow Record and the workflow advances based on that decision.

The deadlock rule exists because unbounded review loops are worse than an imperfect decision. Three rounds is enough to surface genuine disagreements. After that, human judgment is required.

---

## What Happens If Gate Is Bypassed

Bypassing the implementation gate without Human approval is a governance violation. If implementation was started prematurely, the correct action is:

1. Stop implementation
2. Record the premature start in the Workflow Record
3. Complete the gate process retroactively
4. Resume implementation only after Human approval

This is not bureaucratic punishment - it exists because post-hoc review of already-implemented changes is less effective than pre-implementation review.
