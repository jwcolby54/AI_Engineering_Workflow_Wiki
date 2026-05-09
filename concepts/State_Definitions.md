# State Definitions

Workflow state is recorded explicitly in the Workflow Record header and updated at each phase transition. States are machine-readable by design.

---

## Valid States

| State | Meaning |
|---|---|
| `NEEDS_REVIEW` | A proposal exists and is awaiting critique from the second AI |
| `NEEDS_REVISION` | Critique identified concerns requiring changes before re-review |
| `READY_FOR_FINAL_REVIEW` | Revision is complete; awaiting final critique pass |
| `IMPLEMENT_READY` | Both AIs have converged; awaiting Human gate approval |
| `BLOCKED_PENDING_HUMAN_APPROVAL` | All AI approvals are in; Human has not yet approved |
| `IMPLEMENTED` | Implementation is complete |
| `VALIDATED` | Validation criteria have been met |
| `SUPERSEDED` | This record has been replaced by a newer version or archived |

---

## Valid Transitions

| From | To | Condition |
|---|---|---|
| `NEEDS_REVIEW` | `NEEDS_REVISION` | Critique found BLOCKING or MAJOR concerns |
| `NEEDS_REVIEW` | `IMPLEMENT_READY` | Critique found no BLOCKING or MAJOR concerns |
| `NEEDS_REVISION` | `READY_FOR_FINAL_REVIEW` | AI_1 has revised and addressed concerns |
| `READY_FOR_FINAL_REVIEW` | `IMPLEMENT_READY` | Final critique confirms concerns resolved |
| `READY_FOR_FINAL_REVIEW` | `NEEDS_REVISION` | Final critique found remaining BLOCKING concerns |
| `IMPLEMENT_READY` | `BLOCKED_PENDING_HUMAN_APPROVAL` | Both AIs approved; Human has not yet acted |
| `BLOCKED_PENDING_HUMAN_APPROVAL` | `IMPLEMENTED` | Human approved; implementation completed |
| `IMPLEMENTED` | `VALIDATED` | Validation criteria met |
| `VALIDATED` | `SUPERSEDED` | Record archived or replaced |

---

## Rules

- No state may be skipped without explicit Human override, recorded in the Workflow Record
- Backward transitions (e.g., `IMPLEMENT_READY` → `NEEDS_REVISION`) require a new named review round
- `SUPERSEDED` is terminal — records in this state are archived permanently and never modified
- The current state must always be visible in the Workflow Record header
