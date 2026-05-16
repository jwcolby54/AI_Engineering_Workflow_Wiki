# AI Engineering Workflow Wiki

The operational reference for the Human + multi-AI adversarial engineering workflow.

This wiki defines the rules. A Workflow Record stores the active engineering state. A session begins when the Human pastes the session starter into an AI chat.

---

## First Step: Paste The Starter

Use the [Session Starter Template](session_starter_template.md) as the first message to any AI agent.

The starter assigns the AI role, points it to this wiki, names the active Workflow Record, and requires the agent to update the record as reasoning evolves.

For most sessions, use the compact form in `session_starter_template.md`.

---

## What This Wiki Is

A durable knowledge and governance layer. It defines the workflow model, the rules, the semantics, and the templates. It does not contain live engineering state. Live state belongs in the Workflow Record.

## What This Wiki Is Not

- A live workflow record
- A chat log
- An implementation artifact
- A place for active review rounds or mutable approvals

---

## Navigation

### Start Here
- [Session Starter Template](session_starter_template.md) - paste this as your first message to any AI agent
- [Overview](concepts/Overview.md) - what this workflow is and why it exists
- [Workflow Model](concepts/Workflow_Model.md) - the full proposal -> critique -> convergence -> implementation cycle
- [AI Agent Instructions](governance/AI_Agent_Instructions.md) - what a participating AI must do

### Governance
- [Governance Model](governance/Governance_Model.md) - multi-agent review structure
- [Human Authority Model](governance/Human_Authority_Model.md) - where final authority lives
- [AI Agent Instructions](governance/AI_Agent_Instructions.md) - agent obligations

### Workflow Semantics
- [State Definitions](concepts/State_Definitions.md) - all valid workflow states and transition rules
- [Severity Definitions](concepts/Severity_Definitions.md) - BLOCKING / MAJOR / MINOR / FUTURE
- [Scope Freeze](concepts/Scope_Freeze.md) - what it means and why it is non-negotiable
- [Gate Model](concepts/Gate_Model.md) - the implementation gate and how approval works

### Operational Topics
- [Operational Principles](concepts/Operational_Principles.md) - philosophy behind the design
- [Context Management](concepts/Context_Management.md) - why chats are not records
- [Artifact Structure](concepts/Artifact_Structure.md) - wiki vs workflow records vs source artifacts

### Session Bootstrap
- [Session Starter Template](session_starter_template.md) - the universal paste-in bootstrap
- [CLAUDE.md Project Template](templates/CLAUDE_md_Project_Template.md) - project bootstrap for Claude Code
- [AGENTS.md Project Template](templates/AGENTS_md_Project_Template.md) - project bootstrap for Codex or other agent systems

### Templates
- [Active Workflow Record Template](templates/AI_Workflow_Record_Active_Template.md) - File A for new records using the active/history model
- [History Workflow Record Template](templates/AI_Workflow_Record_History_Template.md) - File B for new records using the active/history model
- [Workflow Record Template](templates/AI_Workflow_Record_Template.md) - legacy single-file template; use active/history templates for new records
- [Workflow Record Update Instructions](templates/AI_Workflow_Record_Update_Instructions.md) - how to update the record during a session; includes prune protocol
- [Decision Log Template](templates/Decision_Log_Template.md)
- [AI Handoff Template](templates/AI_Handoff_Template.md)

### Examples
- [Publication Workflow Record](WorkflowRecords/2026-05-08_publish_ai_engineering_workflow.md) - live worked example for this release
- [Examples README](examples/README.md) - how examples are handled

### Source Artifacts
- [AI_Workflow_Record_v1_2.md](raw/AI_Workflow_Record_v1_2.md) - historical genesis workflow record
- [AI_Workflow_Concept_Explanation_v1_2.md](raw/AI_Workflow_Concept_Explanation_v1_2.md) - original concept explanation
