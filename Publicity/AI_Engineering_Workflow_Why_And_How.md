# AI Engineering Workflow

**Where AI chats become project records.**

## Why AI Work Needs A Durable Record

AI can help you think faster than any tool most of us have ever used.

It can help shape an idea, challenge assumptions, draft a plan, inspect code, propose architecture, write public copy, and find problems you did not know to look for. But there is a catch: the useful work often lives inside a chat transcript.

That feels fine while the conversation is active. It feels much worse later.

You come back to a long thread and try to remember which version of the idea was best. You scroll past abandoned branches, half-decisions, useful objections, stale assumptions, and paragraphs that felt brilliant at the time but are now hard to place. If you used more than one AI tool, the problem gets worse: the human becomes the copy/paste bridge between systems.

AI Engineering Workflow exists to solve that problem.

It turns AI-assisted work into a durable project record: what was proposed, what was challenged, what changed, what was approved, and what should happen next.

The point is not to make AI autonomous. The point is to make AI collaboration legible.

---

## The Core Idea

AI Engineering Workflow is a manual-first process for one human operator working with two agentic AI tools.

The known working combination is Claude.Code plus Codex. Other agentic tools may work, but they are not yet proven in this project.

The workflow uses a shared Markdown record as the source of truth. Chat is the workspace. The Workflow Record is the durable state.

At a high level:

1. The Human defines the objective.
2. AI_1 proposes.
3. AI_2 critiques with severity levels.
4. The Human clarifies priorities and remains final authority.
5. AI_1 revises.
6. AI_2 reviews again.
7. Scope freezes.
8. The Human approves the gate.
9. Implementation or drafting proceeds.
10. Validation is recorded.

This is familiar engineering discipline applied to AI-assisted work: proposal, critique, revision, approval, execution, validation.

---

## What Problem It Solves

The workflow was created because ordinary AI chat has several failure modes:

- Good ideas get buried in long transcripts.
- Decisions blur together with speculation.
- Critiques get softened or lost during handoff.
- Scope changes silently.
- A later session cannot tell what was approved.
- One AI tool cannot reliably inherit the state of another.
- The human becomes the only durable transport layer between systems.

AI Engineering Workflow moves the important state out of chat and into structured Markdown.

That simple shift changes the work.

Instead of asking, "What did we decide somewhere in that thread?" the record says what was proposed, what objections were raised, what changed, what is frozen, and what remains open.

---

## Why Two Agentic AIs

The current workflow assumes two agentic AI tools because the proposal and critique roles are intentionally separated.

AI_1 is responsible for proposing or revising.

AI_2 is responsible for reviewing, challenging, and assigning severity.

The separation matters because single-model self-review can share the same assumptions as the original answer. A second agentic tool is not magic, and it does not guarantee correctness, but it creates useful friction. It makes disagreement cheaper. It gives the Human a clearer review surface.

The Human still decides.

The AIs are reasoning systems inside a governed process. They are not the authority.

---

## The Workflow Record

The Workflow Record is the center of the system.

It is a Markdown file that captures:

- objective
- current state
- human requirements
- constraints
- AI_1 proposal
- AI_2 critique
- human clarification
- AI_1 revision
- AI_2 final review
- concern severity
- scope freeze
- implementation gate
- validation requirements
- next action

The rule is simple:

If a decision is not in the Workflow Record, it did not happen in any durable sense.

This makes the record useful to the Human, to future AI sessions, and to any reviewer trying to understand how a decision was reached.

---

## Severity Levels

Review findings use four severity levels:

| Severity | Meaning |
|---|---|
| `BLOCKING` | Must be resolved before forward progress. |
| `MAJOR` | Should be resolved before implementation; Human waiver required if left open. |
| `MINOR` | Recommended improvement; does not block. |
| `FUTURE` | Valid but out of scope for this session. |

This prevents all feedback from feeling equal.

Some objections should stop the work. Some should improve it. Some should be recorded without derailing the current scope.

---

## Scope Freeze And Approval Gates

One of the most important parts of the workflow is the scope freeze.

AI tools are very good at expanding scope. They add useful-looking features, alternate framings, extra cases, and implementation details. Sometimes that is helpful. Sometimes it causes drift.

The scope freeze records what is in scope and what is explicitly out of scope before implementation or drafting begins.

The implementation gate then records approval from:

- AI_1
- AI_2
- Human

The Human approval is the one that matters most.

AI can recommend. AI can critique. AI can revise. But the Human decides whether the work is ready to proceed.

---

## What This Is Not

AI Engineering Workflow is not:

- a prompt collection
- a fully automated agent framework
- a replacement for human judgment
- a claim that AI output is automatically correct
- a claim that this has been proven at team scale

It is a practical operating pattern for making AI-assisted work easier to review, resume, and trust.

---

## A Simple Example

Without the workflow:

You brainstorm with an AI tool for an hour. The conversation is productive. Later, you try to recover the useful parts from the transcript. You remember there was a good objection somewhere, a better version of the thesis, and maybe a decision about scope, but now it is all mixed together.

With the workflow:

The proposal goes into the record. The critique goes into the record. The Human's clarification goes into the record. The revision goes into the record. The approved scope and next action are explicit.

The conversation still happens, but the work no longer disappears into the conversation.

---

## Why It Matters

AI-assisted work is moving from quick answers toward real projects.

Real projects need memory, review, state, and approval. They need a way to know what has been decided and what has not. They need a way to resume after a tool switch, a context reset, or a day away.

AI Engineering Workflow gives that process a simple form:

plain Markdown, explicit roles, adversarial review, scope freeze, approval gates, and durable records.

It is not heavy machinery. It is a way to stop treating chat as the project record.

---

## Current Status

The workflow is public and documented here:

https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki

It is currently tested as a solo-human workflow using two agentic AI tools. The working combination is Claude.Code plus Codex.

The next frontier is broader use: other tool combinations, richer examples, and eventually multiple humans participating in a single governed session.
