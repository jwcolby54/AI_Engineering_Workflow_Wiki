# DesignFlow Template

## What Is a DesignFlow

A DesignFlow is a structured brainstorming and synthesis scaffold. Use it when
the goal is to think through a concept, define structure, and converge on a
document or design artifact before building or writing anything.

A DesignFlow is not an AI Engineering Workflow Record. It has no gates, no
phases, and no approval chain. It is lighter than that.

A DesignFlow typically involves the Human and one or both AIs working through
a topic together. It moves from orientation (what are we making and why) through
decisions (what are the rules and tradeoffs) to closure (frozen outline and key
decisions). When Frozen it becomes a durable design input for downstream work.

## Operating Rule - Human Inputs Must Be Captured

When the Human provides ideas, constraints, instructions, examples, or design
preferences in either AI's context area, prompt, or chat, those inputs should
be inserted into the active DesignFlow document as durable design context.

Do not leave important Human design direction stranded only in transient AI
context. Summarize it in the relevant DesignFlow sections such as Objective,
Scope, Constraints, Inputs and Evidence, Contract Decisions, Open Questions, or
Drafting Notes.

## Operating Rule - Active File Is the Context Anchor

The active DesignFlow file exists to be the durable, low-noise resume artifact.
When resuming work in a long-lived AI thread:

- Treat the active DesignFlow file plus the current prompt as the primary
  working context.
- Do not rely on earlier chat discussion unless the active file explicitly
  points back to it.
- Do not reload or re-summarize the full thread by default.
- Pull older deliberation only from the paired history file, and only when a
  specific unresolved question requires it.

If the Human wants a same-thread "soft clear," the correct instruction is:
"Ignore earlier thread discussion and use only this active DesignFlow file plus
the current prompt."

## Operating Rule - History Is Archive, Not A Live Twin

After a DesignFlow is split into Active and History files:

- During ordinary design work, read and write the Active file only.
- Do not mirror each new decision into the History file during the same working
  flow.
- Do not routinely read both files "just to be safe." If that becomes normal,
  the split has failed.
- The History file exists for archived material that has been pruned out of the
  Active file, not as a second live companion log.

Write to the History file only at a real prune/archive point, such as:

- the Active file has become too large to resume quickly
- a session has ended and older detail is no longer needed in Active
- the Human explicitly asks for a history sync

After pruning, the Active file must still be sufficient on its own for normal
work. If an AI would need to read History routinely to continue, the Active file
has been over-pruned and must be repaired before work continues.

## Operating Rule - Split Naming And Authority

When a DesignFlow grows large enough to split into current-state and history
files, the naming convention is:

- `<Topic>_Active.md` -- current implementation-facing truth
- `<Topic>_History.md` -- full deliberation and superseded material

Do not leave the old unsuffixed file as a second live DesignFlow document.
If an unsuffixed file must remain for compatibility with old references, reduce
it to a short redirect stub pointing to the Active and History files.

After a split:

- read the Active file first
- read the History file only when the Active file or Human says it is needed
- treat the Active file as the only authoritative current-state source

## Operating Rule - AI Setup Checklist

When an AI is delegated to create a new DesignFlow instance and the Human has
not already answered the following, ask explicitly before creating the file:

1. Instance name: what is the topic? (used for the filename)
2. Storage location: where should the instance file live in the project?
3. Workflow Record link: is this DesignFlow feeding an existing Workflow Record?
   If yes, note the record path in section 5 (Inputs and Evidence).

Do not invent answers to these questions. They determine file naming and
cross-reference wiring that the Human must own.

## Document Metadata

- Topic:
- Target artifact:
- Author:
- Date started:
- Last updated:
- Status: Draft / In Progress / Frozen
- Template master: E:\AI\AI_Engineering_Workflow_Wiki\docs\DesignFlow_Template.md

Note: keep the Template master line in every instance pointing to the canonical
path. To update the standard, edit the template master. To work on a design
session, edit the instance only.

## 1. Objective

What are we trying to produce, and why does it matter?

- Desired output:
- Primary purpose:
- Definition of success:

## 2. Audience

Who will read or use the target artifact?

- Primary audience:
- Secondary audience:
- Reader assumptions:

## 3. Scope

What is in scope for this DesignFlow?

- In scope:
- Out of scope:
- Non-goals:

## 4. Constraints

What rules or environmental constraints shape the design?

- Technical constraints:
- Documentation constraints:
- Process constraints:

## 5. Inputs and Evidence

What source material should inform the design?

| Source | Type | Why it matters | Notes |
|---|---|---|---|
|  |  |  |  |

## 6. Problem Framing

What problem does the artifact solve for the reader?

- Current pain:
- Current ambiguity:
- Risk if left unclear:

## 7. Candidate Structure

What sections or major components might the artifact need?

| Section | Purpose | Required | Notes |
|---|---|---|---|
|  |  | Yes/No |  |

## 8. Core Concepts

List the key ideas the artifact must define clearly.

| Concept | Working definition | Open questions |
|---|---|---|
|  |  |  |

## 9. Contract Decisions

Use this section when the artifact defines rules, boundaries, contracts, or
responsibility lines.

| Area | Candidate rule or contract | Rationale | Confidence |
|---|---|---|---|
|  |  |  | Low / Medium / High |

## 10. Alternatives Considered

Capture meaningful alternatives before converging.

| Option | Pros | Cons | Keep / Reject / Maybe |
|---|---|---|---|
|  |  |  |  |

## 11. Open Questions

Questions that still need answers before the artifact can be frozen.

| ID | Question | Owner | Resolution path |
|---|---|---|---|
| Q-001 |  |  |  |

## 12. Proposed Outline

Draft the current best outline for the target artifact.

1. 
2. 
3. 

## 13. Drafting Notes

Write short synthesis notes here as the DesignFlow progresses.

- 

## 14. Freeze Criteria

When can this DesignFlow be considered complete?

- The target artifact has a stable outline.
- Core terms and contracts are defined clearly enough to draft.
- Open questions that affect structure are resolved or explicitly parked.
- The document can be handed off as a frozen design input if needed.

## 15. Final Output Snapshot

When the DesignFlow is complete, summarize the frozen decisions here.

- Final artifact path:
- Final structure:
- Key decisions:
- Deferred questions:

## 16. Participant Notes

Use this section to preserve "who thought what" at a meaningful level.

This is not a full transcript. It is a compact attribution section for the key
ideas, objections, decisions, and rationale contributed by each participant.

Recommended usage:

- Prefer summary notes over a running timestamped log unless the DesignFlow
  specifically needs chronology.
- Record the durable signal, not every turn of discussion.
- Use this section when attribution, disagreement, or Human override matters.
- The AI or Human currently writing this section may decide what level of
  summary is appropriate, using reasonable judgment.
- Leave unused participant subsections as `-` rather than treating them as
  missing required content.

### Human

- 

### AI_1 (Claude)

- 

### AI_2 (Codex)

- 
