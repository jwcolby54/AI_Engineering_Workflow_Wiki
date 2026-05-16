# Overview

## What This Workflow Is

This is not "multiple AIs helping write software."

It is a collaborative AI-assisted systems engineering governance model. The distinguishing feature is adversarial review: one AI proposes, a second AI critiques from an independent perspective, and the result is revised until both systems converge. The human operator holds final authority throughout.

The workflow produces structured Markdown artifacts - not chat logs - as its durable output. Those artifacts persist across sessions, across model changes, and across time gaps.

## Why It Exists

The immediate problem is context loss. Design decisions made in a long chat disappear when the chat ends. Rationale evaporates. The same architectural questions get re-litigated in the next session because nothing was preserved. Token costs compound as chats grow.

The deeper problem is that AI systems have different failure modes. Claude and ChatGPT do not make identical mistakes. Running a proposal through both systems under structured adversarial review catches problems that either system alone would miss.

The workflow formalizes what was already happening informally and makes it repeatable, resumable, and eventually automatable.

## The Core Loop

```
Human defines goal
-> AI_1 proposes solution
-> AI_2 critiques with severity-ranked concerns
-> AI_1 revises
-> AI_2 reviews again
-> Convergence (or Human deadlock resolution)
-> Scope freeze
-> Human approves at implementation gate
-> Implementation
-> Validation
```

Each step is recorded in a Workflow Record document that travels with the project. The wiki you are reading now defines the rules for that document and this process.

## What Makes This Different From Ordinary Chat

| Ordinary Chat | This Workflow |
|---|---|
| Reasoning lost when chat ends | Reasoning preserved in Workflow Record |
| One AI, one perspective | Two AIs, adversarial review |
| Implementation begins whenever | Implementation gated on convergence + approval |
| Design and implementation blur | Design, review, approval, implementation are separate phases |
| No audit trail | Full round-by-round decision history |
| Context must be reconstructed | Context is externalized and portable |

## Scope of Application

This workflow applies to any engineering decision that warrants structured review: database design, architecture decisions, API design, pipeline changes, Python development, SQL, or any other technical domain where getting it wrong is costly.

It is intentionally designed to work manually before any automation exists.

## What This System Actually Is

Named plainly: this is portable AI engineering governance with layered context management,
durable AI collaboration memory, and cross-agent operational semantics.

That is meaningfully beyond "AI coding assistant usage." The distinction matters because it
explains why the architecture has the shape it does:

- The wiki exists because governance must outlive any single chat session or AI platform
- The bootstrap files exist because agents need orientation before they can participate correctly
- The session starter exists because platform behavior changes but a pasted prompt always works
- The Workflow Record exists because active engineering state must be separated from durable knowledge
- The adversarial review model exists because no single AI system is a reliable sole reviewer

Each layer solves a specific failure mode. The system as a whole makes AI-assisted engineering
resumable, auditable, and portable across platforms, models, and time.
