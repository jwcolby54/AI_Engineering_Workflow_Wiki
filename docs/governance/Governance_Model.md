# Governance Model

## Structure

The workflow uses three-party structured adversarial review.

| Party | Role |
|---|---|
| Human | Defines requirements, holds final authority, resolves deadlocks, controls implementation gate |
| AI_1 (proposing AI) | Drafts proposals, revises based on critique, updates Workflow Record |
| AI_2 (reviewing AI) | Critiques proposals, assigns severity to concerns, provides final review |

The roles of AI_1 and AI_2 may be filled by Claude or ChatGPT. The assignment may vary by session. What matters is that the two AIs are operating from independent perspectives - not that a specific model always fills a specific role.

---

## Why Three Parties

Two-party review (Human + one AI) is insufficient because it lacks independent scrutiny. The Human brings domain authority and final judgment but may miss technical edge cases. A single AI brings analytical capability but has blind spots it cannot see by definition. A second AI operating independently creates adversarial pressure that surfaces what either party alone would miss.

The governance model is designed around the assumption that no single participant - human or AI - is reliable enough to own the full review process alone.

---

## Separation of Phases

Governance requires that design, critique, revision, approval, and implementation remain distinct phases with explicit transitions between them. Blurring these phases is the most common failure mode:

- Implementation that begins during design, before architecture is settled
- Critique that silently rewrites the proposal instead of challenging it
- Approval that is implied rather than recorded

The Workflow Record structure enforces this separation by requiring explicit state transitions and named rounds.

---

## Scope of Authority

| Decision Type | Authority |
|---|---|
| Proposal content | AI_1 |
| Concern identification and severity | AI_2 |
| Concern resolution approach | AI_1, subject to AI_2 review |
| Scope waiver for unresolved MAJOR concern | Human only |
| Implementation gate approval | All three parties |
| Deadlock resolution after Round 3 | Human only |
| Scope change after freeze | Requires new review round |

No AI system may self-approve deployment. No AI system may override Human decisions. No AI system may silently redefine architecture or expand scope.

---

## Future Participants

The workflow is designed to accommodate additional AI reviewers in future sessions. A third AI may participate as an additional reviewer, with its concerns recorded using the same severity taxonomy. The governance structure does not change - Human authority and the three-phase review model remain constant regardless of how many AI systems participate.
