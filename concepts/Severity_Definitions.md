# Severity Definitions

Severity levels exist to prevent endless review loops. Without them, a trivial naming suggestion carries the same weight as a structural flaw, and convergence never happens.

---

## Levels

| Severity | Meaning |
|---|---|
| `BLOCKING` | Architectural or correctness flaw. Must be resolved before any forward progress. |
| `MAJOR` | Significant problem that should be resolved before implementation. Human may grant an explicit waiver if unresolved. |
| `MINOR` | Recommended improvement. Does not block progress. May remain open. |
| `FUTURE` | Valid idea that is out of scope for the current session. Recorded for future consideration. Does not affect current approval. |

---

## Rules

- No `BLOCKING` concern may remain open at the implementation gate
- An unresolved `MAJOR` concern requires an explicit Human waiver recorded in the Workflow Record
- `MINOR` and `FUTURE` concerns may remain open without impact on gate approval
- Severity is assigned by the reviewing AI, not the proposing AI
- Severity downgrades (e.g., `BLOCKING` -> `MAJOR`) require explicit justification recorded in the next round

---

## Why This Four-Level Model

The model is intentionally simple:
- Simple enough to apply manually without tooling
- Distinct enough that the categories do not collapse into each other
- Machine-readable for future automation
- Conservative enough that `BLOCKING` means something

A five- or six-level model creates ambiguity between adjacent levels. Two levels create false binaries. Four levels match the actual decision space: must fix, should fix, nice to fix, file for later.
