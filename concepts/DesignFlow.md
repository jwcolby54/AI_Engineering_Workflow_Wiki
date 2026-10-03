# DesignFlow

## What It Is

A DesignFlow is a lightweight AI design conversation -- a mode for exploring
options, brainstorming approaches, and producing design proposals without
triggering the full Workflow Record machinery.

It is the right starting point when:
- The Human wants two AIs to discuss design options before committing to a
  formal review cycle.
- The shape of the problem is not yet clear enough to write a crisp Objective.
- The goal is exploration and convergence, not gated implementation.

A DesignFlow may produce:
- A design proposal document
- A Codex (AI_2) starter block for review
- A structured discussion record
- A Workflow Record (if the content warrants it and the Human says so)

When a DesignFlow is substantive enough to need a split record, the standard
pair is:
- `<Topic>_Active.md` -- current implementation-facing truth
- `<Topic>_History.md` -- full deliberation, superseded ideas, and rationale

If an older unsuffixed DesignFlow file is retained after the split, it must be
only a short redirect stub pointing to the Active and History files. It is not
an alternate source of truth.

It does not automatically trigger active/history Workflow Record creation or
the implementation gate.

---

## What It Is Not

A DesignFlow is not a workflow session.

| DesignFlow | Workflow Session |
|---|---|
| Triggered by "DesignFlow", "let's design", "design discussion" | Triggered by "start workflow session", "start session" |
| No mandatory Workflow Record | Active + history record created on trigger |
| No implementation gate required | Gate must clear before implementation |
| Exploratory; may not freeze scope | Scope freeze is required before implementation |
| Can use Workflow Record format if helpful | Workflow Record is the required artifact |

---

## How To Recognize a DesignFlow Request

The Human says things like:
- "Let's run a DesignFlow with Codex"
- "DesignFlow on X"
- "Let's design X before we start"
- "I want to explore options for X"

If the Human does NOT use a workflow session trigger phrase (see
[Workflow Model](Workflow_Model.md)) and is asking about design or approach,
treat it as a DesignFlow.

---

## What An AI Should Do In a DesignFlow

### As AI_1 (Claude / proposing AI)

1. Produce a design proposal in plain text or in a lightweight document.
2. Include reasoning and risks, but do not invoke the full Workflow Record
   state machinery (NEEDS_REVIEW, BLOCKING/MAJOR/MINOR/FUTURE labels are
   still useful, but the gate and scope-freeze sections are optional).
3. Produce a Codex starter block if the Human wants AI_2 review.
4. If the conversation grows into a formal design that warrants gated
   implementation, offer to escalate: write an active/history record pair
   and ask the Human to confirm before creating files.

### As AI_2 (Codex / reviewing AI)

1. Read the design proposal the Human provides.
2. Critique with severity-ranked concerns if the design is substantive.
3. Do not demand a Workflow Record or implementation gate -- this is a
   design conversation, not a gated session.
4. If BLOCKING concerns exist, say so clearly and explain what must change.

---

## Escalation Path

A DesignFlow can escalate to a full workflow session at any time.

Human says: "start workflow session" or "let's formalize this"

At that point, the AI creates:
1. WorkflowRecords/YYYY-MM-DD_<name>.active.md
2. WorkflowRecords/YYYY-MM-DD_<name>.history.md
3. WorkflowRecords/<name>.md (Codex starter)

The DesignFlow output becomes the AI_1 proposal in Round 1 of the new record.

---

## Using a Workflow Record Format for a DesignFlow

Some DesignFlow conversations are substantive enough that the Workflow Record
structure is useful even without the gate machinery. This is permitted.

When this happens:
- Label the record as a DesignFlow record (not a full workflow record) in the
  header.
- The implementation gate section is optional.
- Scope freeze is optional.
- A single document may suffice while the design is still small.
- Once the design is split, use exactly one authoritative pair:
  `<Topic>_Active.md` and `<Topic>_History.md`.
- Do not keep the unsuffixed original as a second live DesignFlow document.
  If it remains for compatibility, reduce it to a redirect stub only.
- During ordinary work, the Active file is the only normal read/write target.
  The History file is archive material, updated only when older detail is
  pruned out of Active because Active has become too large or the Human
  explicitly asks for a history sync.
- If an AI is routinely reading both files during active work, the split is not
  functioning correctly.
- Severity labels (BLOCKING/MAJOR/MINOR/FUTURE) remain useful for structuring
  the critique.

The record does not authorize implementation on its own. Escalation to a
workflow session is required before implementation can begin.

---

## Related

- [Workflow Model](Workflow_Model.md) -- the full proposal/critique/gate cycle
- [State Definitions](State_Definitions.md) -- workflow states and transitions
- [Gate Model](Gate_Model.md) -- when implementation is authorized
- [AI Agent Instructions](../governance/AI_Agent_Instructions.md) -- agent behavior rules
