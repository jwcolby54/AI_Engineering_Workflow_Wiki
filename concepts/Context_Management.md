# Context Management

## The Core Problem

Chats are ephemeral. A 50-message design session contains reasoning, rationale, critiques, revisions, and decisions - none of which survives the session unless it is explicitly externalized. Even within a session, long chats degrade quality: earlier context becomes diluted, token costs compound, and focus diffuses.

This is not a complaint about AI systems. It is a structural fact about how they work. The workflow is designed around this constraint.

---

## The Solution: Externalized Context

Every piece of reasoning that matters is written into the Workflow Record immediately, not at the end of the session. The Workflow Record is the running external memory of the session.

At any point, the session should be resumable from the Workflow Record alone, without re-reading the chat.

---

## How to Keep the Workflow Record Current

The participating AI updates the Workflow Record:
- After each proposal
- After each critique (with severity table)
- After each revision
- After each gate decision
- When scope freeze is established

See [AI Workflow Record Update Instructions](../templates/AI_Workflow_Record_Update_Instructions.md) for the full behavioral spec.

---

## Starting a New Session

When returning to a project after a gap, the process is:

1. Load the wiki (this document set) to understand the workflow rules
2. Load the current Workflow Record for the topic being continued
3. Read the current state and last completed round
4. Continue from that point

No re-reading of prior chat required. No reconstruction from memory.

---

## Active/History Two-File Records

Workflow Records can grow large as proposals, critiques, revisions, implementation
checkpoints, and validation evidence accumulate. Both AI systems then repeatedly
load completed history that is no longer needed for the next action.

The active/history model addresses this by splitting the Workflow Record into two
paired files:

- Active Record (.active.md): compact current-state file. Contains exactly what is
  required to continue work safely. Every AI reads this first.
- History Record (.history.md): append-only archive of completed material pruned
  from the active record. Loaded only when the active record explicitly says it is
  needed.

As work progresses, completed material is moved from the active record to the
history record via a Prune Event. The active record stays compact. The history
record preserves the full audit trail.

**Default-read rule:** agents read the active record first. Agents read the history
record only when the active record's "Read History Only If" section says archived
context is required for the next action.

**Cold-resume invariant:** the active record is valid only if an AI can resume
safely from it without reading history. See the Prune Event protocol in
`templates/AI_Workflow_Record_Update_Instructions.md` for the full invariant.

**Legacy records:** existing single-file records (YYYY-MM-DD_<topic>.md) are not
retroactively split. They remain as-is for read-only reference. If reopened for
active work, convert to the two-file model before adding new content. See the
legacy conversion rule in the Update Instructions.

---

## Starting a New Topic

When a new engineering topic begins, a new Workflow Record is created from the [template](../templates/AI_Workflow_Record_Template.md). The prior Workflow Record for the old topic is left in place - it is the permanent record of that decision.

---

## Context Portability Between AI Systems

When handing off between AI systems (e.g., from a Claude session to a ChatGPT session), the handoff artifact is the Workflow Record, not a chat export. See the [AI Handoff Template](../templates/AI_Handoff_Template.md).

The Workflow Record contains everything the new AI system needs to participate in the review process at the correct point in the workflow.

---

## What Not To Put In the Workflow Record

The Workflow Record is not a chat log. It should not contain:
- Exploratory questions that were abandoned
- Thinking-out-loud that did not produce a decision
- Redundant restatements of prior content

Every section of the Workflow Record should be load-bearing. If removing it would lose information, keep it. If it is repetition or noise, it does not belong there.
