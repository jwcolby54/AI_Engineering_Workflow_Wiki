# AI Engineering Workflow

A portable Markdown protocol for running AI-assisted engineering work like a design review: one AI proposes, another AI critiques, the Human decides, and the durable record preserves the reasoning, scope, approval state, and validation criteria.

This project is inspired by Andrej Karpathy's LLM Wiki pattern: keep durable Markdown context outside the chat so LLM agents can reload, extend, and maintain it across sessions. AI Engineering Workflow applies that idea to engineering governance.

---

## Start Here

The workflow begins by pasting a session starter into an AI chat. The starter tells the AI where the wiki is, which Workflow Record to use, and what role it is playing.

Use the canonical starter here:

**[Session Starter Template](session_starter_template.md)**

For a normal session, paste the compact form, fill in the wiki path, Workflow Record path, and role:

```text
This engineering session follows the AI Engineering Workflow model.

Wiki:            [path to AI_Engineering_Workflow_Wiki]
Read first:      index.md, then governance/AI_Agent_Instructions.md
Workflow Record: [full path to active .md] / [new session]
My role:         [AI_1 proposing / AI_2 reviewing]

Requirements:
- Read the wiki before proceeding. Do not rely on training knowledge of this workflow.
- Update the Workflow Record as reasoning evolves, not at the end.
- Use adversarial review semantics and severity levels (BLOCKING/MAJOR/MINOR/FUTURE).
- Respect frozen scope. Do not implement before the gate is cleared.
- Human remains final authority.
- Use plain ASCII only in all Workflow artifacts. No Unicode punctuation, arrows, math symbols, box drawing, emojis, non-breaking spaces, or zero-width characters.
```

That paste-in starter is the activation step for the whole workflow. Bootstrap files such as `CLAUDE.md` and `AGENTS.md` can help, but the session starter is the portable guarantee.
Bootstrap files are optional examples, not required runtime dependencies, so this workflow remains agent-agnostic.

---

## Who This Is For

This is for engineers who already understand design meetings, architecture review, RFCs, and proposal / critique / revision loops, and who want AI-assisted work to have the same durable review trail.

The workflow is useful when getting the decision wrong is costly: architecture, database design, API contracts, pipelines, release plans, migration strategy, or any implementation that should not begin from an unreviewed chat.

---

## Why Adversarial Review

Most engineers are not trained to run adversarial design review on their own ideas before implementation. Code review usually happens after code exists. Architecture review and RFC processes can catch design problems earlier, but they are often expensive: schedule the meeting, brief the reviewers, wait for availability, and reconstruct context for everyone.

This workflow makes the useful part cheap. AI_1 proposes the design. AI_2 is asked to attack it honestly, with severity levels. The Human clarifies priorities and remains the final authority. Because every participant reads and writes the same Workflow Record, the process can happen quickly without the Human becoming the copy-paste message bus.

The public-package workflow for this repository went from proposal through critique, Human clarification, revision, final review, scope freeze, gate approval, and implementation in a couple of hours on 2026-05-09. That is the point: the review pressure is real, but the coordination cost drops because the shared Markdown record carries the context.

The goal is not to make the design perfect. The goal is to expose the important objections before implementation starts, record the reasoning, freeze the agreed scope, and only then build.

---

## What This Is

AI Engineering Workflow is a manual-first governance model for Human + multi-AI engineering sessions.

The practical shift is simple:

| Ordinary multi-AI chat | AI Engineering Workflow |
|---|---|
| The Human copies summaries between AI chats. | Each AI reads and updates the same Workflow Record. |
| Decisions live in chat history. | Decisions live in structured Markdown. |
| Critique can get lost or softened during handoff. | Critique is recorded with severity: `BLOCKING`, `MAJOR`, `MINOR`, `FUTURE`. |
| Implementation can begin from an unclear memory of the decision. | Implementation waits for scope freeze and Human gate approval. |

The Human still decides. The difference is that the Human is no longer the only durable transport layer between AI systems.

The core loop:

```text
Human defines goal
-> AI_1 proposes
-> AI_2 critiques with severity-ranked concerns
-> AI_1 revises
-> AI_2 reviews again
-> Scope freezes
-> Human approves the implementation gate
-> Implementation proceeds
-> Validation is recorded
```

The durable artifact is the Workflow Record: a structured Markdown document that records proposals, critique, revisions, scope freeze, gate approval, implementation notes, and validation.

---

## What This Is Not

- It is not a chat transcript.
- It is not an autonomous agent framework.
- It is not a claim that AI output is automatically correct.
- It is not automation-first. The current protocol is intentionally manual so the process can mature before tooling freezes assumptions.

---

## Repository Map

```text
AI_Engineering_Workflow_Wiki/
    README.md                          <- public entry point
    index.md                           <- master navigation
    session_starter_template.md        <- paste this into AI chats

    concepts/
        Overview.md
        Workflow_Model.md
        Operational_Principles.md
        State_Definitions.md
        Severity_Definitions.md
        Scope_Freeze.md
        Gate_Model.md
        Context_Management.md
        Artifact_Structure.md

    governance/
        Governance_Model.md
        Human_Authority_Model.md
        AI_Agent_Instructions.md

    templates/
        AI_Workflow_Record_Template.md
        AI_Workflow_Record_Update_Instructions.md
        Decision_Log_Template.md
        AI_Handoff_Template.md
        CLAUDE_md_Project_Template.md
        AGENTS_md_Project_Template.md

    WorkflowRecords/
        2026-05-08_publish_ai_engineering_workflow.md

    examples/
        README.md

    raw/
        AI_Workflow_Record_v1_2.md
        AI_Workflow_Concept_Explanation_v1_2.md
```

New readers should start with `session_starter_template.md`, `index.md`, and the live Workflow Record in `WorkflowRecords/`.

The `raw/` directory is historical source material. It shows where the workflow came from, but it is not the current operating spec.

---

## Worked Example

The publication decision for this project is itself the worked example:

**[WorkflowRecords/2026-05-08_publish_ai_engineering_workflow.md](WorkflowRecords/2026-05-08_publish_ai_engineering_workflow.md)**

It shows the full pattern: AI_1 proposal, AI_2 critique, Human clarification, AI_1 revision, AI_2 final review, scope freeze, and implementation gate approval.

---

## License

MIT. See [LICENSE](LICENSE).
