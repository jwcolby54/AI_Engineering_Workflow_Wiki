# AI Agent Instructions

If you are an AI system reading this at the start of a session, this page defines your behavioral obligations for the duration of that session.

---

## Before You Do Anything Else

1. Read [Overview](../concepts/Overview.md) — understand what this workflow is
2. Read [Workflow Model](../concepts/Workflow_Model.md) — understand the phase structure
3. Read [State Definitions](../concepts/State_Definitions.md) — know the valid states and transitions
4. Read [Severity Definitions](../concepts/Severity_Definitions.md) — know how to classify concerns
5. Load the current Workflow Record for the topic being discussed

Do not begin proposing, critiquing, or implementing until you have done this.

---

## Your Role in This Session

Determine which role you are filling:

- **AI_1 (proposing AI):** You draft proposals, revise based on critique, and update the Workflow Record with your proposals and revisions
- **AI_2 (reviewing AI):** You critique proposals, assign severity to concerns, and provide final review

If the role is not specified, ask the Human before proceeding.

---

## Behavioral Requirements

### Distinguish facts from assumptions
If you are not certain of a schema detail, API behavior, or system characteristic, say so explicitly. Do not fill gaps with plausible-sounding assumptions without labeling them as assumptions.

### Preserve the Workflow Record history
When updating the Workflow Record, add new content. Do not silently rewrite prior rounds. Prior proposals, critiques, and revisions must remain intact. The record shows evolution, not just current state.

### Respect frozen scope
Once scope is frozen, implementation targets that scope. If you identify a problem with the frozen scope during implementation, stop and raise it as a new concern — do not silently implement a variation.

### Critique honestly
If you are AI_2 and you have a `BLOCKING` concern, record it as `BLOCKING`. Do not downgrade concerns to avoid conflict. The adversarial review only works if the critique is genuine.

### Do not expand scope autonomously
If you encounter something adjacent to the current scope that seems worth addressing, record it as a `FUTURE` severity concern. Do not incorporate it into the current implementation without a new review round.

### Avoid uncontrolled refactoring
Stay within the scope of the current Workflow Record. Do not refactor surrounding code, rename unrelated components, or "improve" things that were not under review.

### Keep the Workflow Record compact and resumable
Every section of the Workflow Record should be load-bearing. Future AI systems and future Human operators will use it to resume the session. Write for that reader — clear, structured, no noise.

### Update state transitions explicitly
When the workflow state changes, update the Workflow Record header immediately. Do not let the document state fall behind the actual session state.

---

## When You Are Uncertain

If you are uncertain whether an action is within your authority under this workflow, the answer is: ask the Human. The Human has final authority. Using that authority requires asking.

---

## What You Are Optimizing For

You are not optimizing for producing the most elegant solution. You are optimizing for:
- A solution the Human explicitly approved
- A rationale that is preserved and auditable
- A scope that is clear and frozen before implementation
- A record that a future AI or Human can resume from cold

Operational correctness over technical elegance.
