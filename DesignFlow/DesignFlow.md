# DesignFlow

DesignFlow is a portable AI design scaffold for turning an unclear idea into a
clear design artifact before implementation begins.

It is meant to be simple enough that a developer can place this file in a
directory, point an agentic AI at it, and say:

```text
Read DesignFlow.md. Help me start a DesignFlow for the thing I want to design.
Do not implement yet. First help me discover and record the design.
```

## What This Is

DesignFlow is a structured design conversation.

It helps the human and AI:

- discover the real problem
- name the audience and use case
- collect source material and constraints
- explore possible approaches
- make tradeoffs visible
- converge on a design that can be handed to an implementation workflow, a
  human developer, another AI agent, or future documentation work

The main output is a DesignFlow instance document: a written record of the
design as it becomes known.

The instance should record both human input and AI input. Label them clearly so
future readers can tell who contributed what.

## What This Is Not

DesignFlow is not an implementation workflow.

It does not require:

- AI_1 / AI_2 roles
- approval gates
- severity labels
- adversarial review
- frozen scope enforcement
- project governance

Those may be useful later, but they belong to a build workflow, not to the
initial design conversation.

DesignFlow answers: "What are we trying to design, and what should it become?"

Workflow answers: "How do we safely build, review, validate, and ship it?"

## File Model

A directory using DesignFlow usually contains:

- `DesignFlow.md` - this reusable skill file
- one or more DesignFlow instance file pairs, such as:
  - `Access_Export_Skill_Active.md`
  - `Access_Export_Skill_History.md`

The active file is the current working design state. The history file preserves
older session notes, longer discussion summaries, alternatives, and archived
material that should not be reloaded every time.

If an older unsuffixed DesignFlow file is retained after a split, it must be a
short redirect stub only. Do not keep it as a second live source of truth.

If the human does not name a location or file prefix, ask before creating it.

## Agent Startup

When the human asks to start or continue a DesignFlow, the AI should:

1. Read this file.
2. Ask only for missing setup information needed to begin.
3. For a new DesignFlow, create a named `_Active.md` file from the DesignFlow
   Active Template and a paired `_History.md` file from the DesignFlow History
   Template.
4. For an existing DesignFlow, read the `_Active.md` file first.
5. Read the paired `_History.md` file only when the active file says history is
   needed, when the human asks for it, or when the current task clearly depends
   on older detail.
6. Use the active file as the living record for the current session.
7. Capture the human's substantive input in the active file during the same
   working session.
8. Capture the AI's substantive input in the active file during the same
   working session.
9. Do not mirror each new decision into both files. Use the active file as the
   only normal read/write target during active work.
10. Move older or bulky notes to the history file only when the active file
    becomes too large to resume quickly, when a session ends, or when the
    human explicitly asks for a history sync.
11. After any prune, ensure the active file still stands on its own for normal
    continuation. If routine work would require reading History, the prune went
    too far and Active must be repaired.
12. Keep design work in DesignFlow until the human explicitly asks to implement,
    hand off, or freeze the design.

Useful opening questions:

- What are we designing?
- Who is the audience or user?
- What useful thing should exist when this is done?
- Where should the DesignFlow active/history pair live?
- What source material should the AI read first?
- What is out of scope for this design?
- What would make the result successful?
- Do you want the DesignFlow to preserve full conversation transcripts, or
  concise summaries of the important turns? Summaries are usually better.

Do not turn these into a questionnaire if the human has already supplied the
answers in conversation. Capture what is known and ask only for what is missing.

## Creating A New DesignFlow Pair

When starting a new DesignFlow, the AI should create a paired active and history
file from the templates in this document.

Default naming pattern:

```text
Topic_Active.md
Topic_History.md
```

Examples:

```text
Access_Export_Skill_Active.md
Access_Export_Skill_History.md

Presentation_Outline_Active.md
Presentation_Outline_History.md

Customer_Onboarding_Redesign_Active.md
Customer_Onboarding_Redesign_History.md
```

Use the Human's topic name as the filename root with spaces replaced by
underscores. Preserve case unless the Human gives a different convention.

If the human gives a different naming convention or storage location, use that.
If the location or topic name is unclear, ask before creating the file.

After creating the pair, the AI should immediately begin using the active file
as the session record. Do not continue the design only in chat.

## Active And History Files

DesignFlow uses an active/history split so the current design can be resumed
quickly without rereading the entire conversation.

The split works only if the active file remains sufficient by itself for normal
work. History is archive material, not a second live companion log.

### Active File

The `_Active.md` file is the short, current source of truth.

It should contain:

- current objective
- current audience
- current desired output
- current constraints
- current decisions
- current open questions
- current draft shape
- latest human and AI inputs
- a short session log
- a "Read History Only If" section
- a pointer to the paired history file

Keep the active file compact. It should be enough for an AI to resume the design
without reading the history file during ordinary continuation.

### History File

The `_History.md` file is the durable archive.

It should contain:

- older session notes
- longer summaries
- superseded ideas
- alternatives considered
- transcript excerpts if transcript mode was selected
- prior final snapshots if the design was revised
- decisions that were replaced, with the reason if known

History preserves the path of thought. Active preserves the current state of
thought.

Do not treat History as a second live working file that is updated on every
decision. History grows when older material is pruned out of Active.

### When To Move Material To History

Move material from active to history when:

- the active file is becoming too long to reload comfortably
- a session has ended and its detailed notes are no longer needed for immediate
  work
- an idea was useful but has been superseded
- transcript excerpts are useful to preserve but distract from the current
  design

When moving material, leave a short summary and a pointer in active.

Append the older material to the end of History, then cut it out of Active.
If an AI would need to read History routinely to continue ordinary work, the
prune was too aggressive and Active must be repaired.

### Read History Only If

Every active file should include a section named `Read History Only If`.

Use it to tell future AI agents when the history file matters.

Example:

```markdown
## Read History Only If

- The human asks why a decision was made.
- The human asks to revisit rejected alternatives.
- The current task needs details from the June 12 brainstorming session.
- The active file appears inconsistent or incomplete.
```

If none of those conditions apply, the AI should read only the active file.

## Agent Rules

Use these rules while running a DesignFlow.

- Stay in design mode until the human leaves design mode.
- Do not implement code, generate final production artifacts, or perform
  irreversible actions unless the human explicitly asks.
- Record substantive human input. Do not leave important decisions only in chat.
- Record substantive AI input as well. Do not leave important AI proposals,
  assumptions, cautions, or synthesis only in chat.
- Label captured input by source, such as `Human Input`, `AI Input`, or with
  participant names if a small team is involved.
- Honor the chosen capture mode: concise summaries by default, full transcript
  excerpts only if the human asks for them.
- Mark assumptions clearly.
- Keep open questions visible.
- Separate ideas from decisions.
- Preserve alternatives that were seriously considered.
- Prefer concrete examples over abstract process language.
- Keep the DesignFlow instance readable by a busy developer.
- If a design becomes large, summarize and link to supporting files instead of
  turning the instance into a junk drawer.
- If the human changes direction, record the turn instead of pretending the old
  direction never existed.

## Lifecycle

DesignFlow has a light lifecycle. These are modes of thought, not gates.

### 1. Orient

Name the thing being designed.

Clarify:

- audience
- purpose
- desired output
- known constraints
- available source material
- what is not being solved

### 2. Gather

Read or collect the material that should shape the design.

Examples:

- existing code
- screenshots
- documents
- database schemas
- user stories
- rough notes
- prior AI chats
- domain references

Record what was read and what it implies.

### 3. Explore

Generate possible structures, approaches, and tradeoffs.

This is the messy middle. The AI should help create options without forcing
premature agreement.

Use "Design Board" notes for candidate ideas.

### 4. Bounce

React to the ideas.

Capture:

- what feels useful
- what feels wrong
- what is too large
- what is missing
- what should be simplified
- what should be saved for later

Bounce notes are allowed to be informal. They exist to keep the human's taste
and judgment visible.

### 5. Converge

Turn the best ideas into a coherent design.

Record:

- decisions
- contracts
- boundaries
- expected inputs and outputs
- success criteria
- important non-goals

### 6. Freeze

Create a final snapshot that is stable enough to hand off.

Freeze does not mean perfect. It means the design is clear enough that the next
agent, developer, or workflow can act without rediscovering the same ground.

### 7. Hand Off

The DesignFlow may hand off to:

- an implementation workflow
- a documentation task
- a prototype
- a presentation
- a reusable skill
- another DesignFlow

The handoff should say what to do next and what not to disturb.

## Capture Style

DesignFlow should be readable after the live conversation is over.

Use brief Q/A capture when starting or clarifying the design:

```text
Q: What are we trying to design?
A: A system to document an Access database by exporting the useful objects and
   using the exported material to produce developer-facing documentation.
```

Use labeled summary notes for longer exchanges:

```text
Human Input - 2026-06-12 10:15
The audience is senior Access consultants. The design should produce something
useful to them, not a toy demo.

AI Input - 2026-06-12 10:18
Recommended framing: use DesignFlow to design an Access export skill, then use
that skill to produce a real database documentation artifact.
```

Full transcripts are sometimes useful for legal, research, or audit reasons,
but they usually make the DesignFlow harder to read. Prefer summaries unless
the human explicitly chooses transcript mode.

## Shared Team Use

A small team can use DesignFlow against a common file on a network share, but
plain Markdown has no built-in merge or locking.

Recommended shared-use rules:

- Use a shared folder that everyone can read.
- Allow only one AI or human editor to write the active file at a time.
- Add participant names to captured input.
- Add timestamps to meaningful entries.
- Before writing, the AI should re-read the current active file so it does not
  overwrite another participant's recent updates.
- If multiple people need to write at once, use separate participant note files
  and periodically merge them into the main DesignFlow instance.

For serious multi-person work, put the DesignFlow directory under version
control or use a document system with edit history.

## DesignFlow Active Template

Use this template for a new DesignFlow instance. Keep sections short at first
and expand them only when useful.

```markdown
# DesignFlow: [Topic]

## Metadata

- Status: Draft
- Created: YYYY-MM-DD
- Updated: YYYY-MM-DD
- Human:
- AI agent:
- Participants:
- Capture mode: Summary
- Started:
- Last updated:
- Active file:
- History file:
- Related files:

## Read History Only If

- The human asks why a decision was made.
- The human asks to revisit rejected alternatives.
- The current task depends on older session detail not summarized here.
- This active file appears inconsistent or incomplete.

## Objective

What are we designing?

## Audience

Who is this for, and what do they need from it?

## Desired Output

What should exist when this DesignFlow is finished?

## Source Material

What files, documents, examples, conversations, or systems should shape the
design?

## Constraints

What limits, rules, risks, preferences, or presentation constraints matter?

## Out Of Scope

What are we intentionally not solving here?

## Session Log

Brief chronological notes about important conversation turns. Use Q/A for short
clarifications and labeled summary notes for longer exchanges.

## Human Inputs

Substantive human comments, preferences, corrections, and decisions captured
from the conversation.

## AI Inputs

Substantive AI proposals, summaries, assumptions, cautions, and design synthesis
captured from the conversation.

## Problem Framing

What problem are we really trying to solve?

## Design Board

Candidate ideas, structures, components, workflows, or approaches.

## Bounce Notes

Reactions to the Design Board. What feels right, wrong, missing, too large, or
worth keeping?

## Decisions

Design choices that have converged enough to rely on.

## Contracts

Inputs, outputs, names, file locations, interfaces, promises, or boundaries the
future work should respect.

## Alternatives Considered

Options that were considered but not chosen, with the reason if known.

## Open Questions

Questions that remain unresolved.

## Draft Shape

The emerging outline, architecture, prompt, skill, document, talk, or artifact.

## Freeze Criteria

What must be true before this design is ready to hand off?

## Final Snapshot

Stable summary of the finished design. Fill this in when freezing.

## Handoff Notes

What the next developer, AI agent, workflow, or documentation task should do
next.
```

## DesignFlow History Template

Use this template for the paired history file.

```markdown
# DesignFlow History: [Topic]

## Metadata

- Created: YYYY-MM-DD
- Updated: YYYY-MM-DD
- Active file:
- Capture mode:
- Participants:

## History Purpose

This file preserves older DesignFlow notes so the active file can stay compact.
Read this file only when the active file or the human says it is needed.

## Session Archive

Older session summaries, transcript excerpts, and detailed notes.

## Superseded Ideas

Ideas that were useful but are no longer part of the current design.

## Alternatives Archive

Alternatives considered in earlier sessions, with reasons if known.

## Decision History

Decisions that were changed, replaced, or clarified over time.

## Prior Snapshots

Earlier snapshots of the design, if useful to preserve.
```

## Continuation Prompt

Use this prompt when returning to an existing DesignFlow:

```text
Read DesignFlow.md and then read [active file]. Continue the DesignFlow from the
current state. Read the paired history file only if the active file says it is
needed or if I ask for it. First summarize what is settled, what is still open,
and what you recommend doing next. Do not implement unless I explicitly ask.
```

## Freeze Prompt

Use this prompt when the design feels ready:

```text
Read DesignFlow.md and the current DesignFlow instance. Help me freeze the
design. Update the Final Snapshot and Handoff Notes so another developer or AI
agent can act from the document without needing this chat.
```

## Implementation Handoff Prompt

Use this prompt when handing a frozen DesignFlow to an implementation agent:

```text
Read DesignFlow.md and the frozen DesignFlow instance. Treat the Final Snapshot,
Decisions, Contracts, Constraints, and Handoff Notes as the design source of
truth. Implement only the requested next step. If the design is ambiguous, ask
before inventing behavior.
```
