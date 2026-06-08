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
- Template master: [path to canonical DesignFlow template]

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
