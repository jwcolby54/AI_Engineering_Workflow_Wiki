# Artifact Structure

Five layers of artifact exist in this system. Each serves a distinct purpose. They must not be mixed.

---

## The Five Layers

| Layer | Purpose | Characteristics |
|---|---|---|
| Wiki | Durable knowledge and governance | Stable, system-wide, not project-specific |
| Bootstrap Files | Platform-specific runtime shim | Compact, auto-loaded by agent, points to wiki |
| Session Starter | Universal cross-platform bootstrap | Portable, vendor-neutral, always works |
| Workflow Records | Active engineering state | Mutable, transactional, one per topic |
| Source Artifacts | Ground truth implementation | Code, SQL, schema, docs, config - what was actually built |

**Design principle:** Bootstrap files are convenience. The session starter is the guarantee. Platform behavior changes. Features drift. Loading semantics differ. A compact prompt pasted at session start works on every platform.

---

## Layer 1: The Wiki

**Location:** `[path to AI_Engineering_Workflow_Wiki]`

**Purpose:** The deep reference system. Defines the workflow model, governance rules, state semantics, severity levels, and templates. Stable changes should be intentional and reviewed.

**What belongs here:**
- Workflow concepts and philosophy
- Governance rules and authority model
- State and severity definitions
- Operational principles
- Templates
- Historical source artifacts

**What does not belong here:**
- Live project-specific engineering state
- Active review rounds for unrelated project work
- Implementation artifacts for a product being built

---

## Layer 2: Bootstrap Files

**Location:** Project root directory

**Purpose:** A compact file that auto-loads when an AI agent starts a session. It tells the agent where the wiki is, what to read first, where the Workflow Records are, and what required behaviors apply.

| Agent System | Bootstrap File | Template |
|---|---|---|
| Claude Code | `CLAUDE.md` | [CLAUDE.md Project Template](../templates/CLAUDE_md_Project_Template.md) |
| OpenAI Codex | `AGENTS.md` | [AGENTS.md Project Template](../templates/AGENTS_md_Project_Template.md) |
| Other chat systems | No reliable convention | Use [Session Starter Template](../session_starter_template.md) |

**What belongs here:**
- Wiki location
- Workflow Record locations for this project
- Required behaviors summary
- Project-specific rules that are not in the wiki

**What does not belong here:**
- Full wiki content
- Active engineering state
- Implementation detail unrelated to agent startup

---

## Layer 3: Session Starter

**Location:** [Session Starter Template](../session_starter_template.md)

**Purpose:** The universal paste-in activation step. It tells an AI where the wiki is, which Workflow Record to use, and which role it is playing.

**What belongs here:**
- Wiki path placeholder
- Workflow Record path placeholder
- AI role assignment
- Required behavior summary

**What does not belong here:**
- Full wiki content
- Long-lived engineering decisions
- Source implementation detail

---

## Layer 4: Workflow Records

**Location:** `[PROJECT_ROOT]/WorkflowRecords/`

**Filename convention:** `YYYY-MM-DD_<topic>.md`

**Purpose:** The mutable, transactional record of a specific engineering session. One document per topic. This is what participating AIs read and write during a session.

**What belongs here:**
- Objective and Human requirements
- All review rounds
- Concern severity tables
- Human clarifications
- Scope freeze
- Implementation gate status and approvals
- Validation criteria and results
- Next actions

**What does not belong here:**
- Workflow rules
- Finished code or schema
- Unstructured chat transcript

Example:

```text
[PROJECT_ROOT]/
  WorkflowRecords/
    2026-05-08_initial_project_review.md
    2026-05-08_database_schema_review.md
    2026-05-09_import_pipeline_design.md
```

---

## Layer 5: Source Artifacts

**Location:** Project source directories

**Purpose:** The actual implementation: what was built. Authoritative on ground truth after implementation.

**What belongs here:**
- Code
- SQL
- Schema files
- Configuration
- Generated outputs
- Published documentation

---

## Relationship Between Layers

```text
Wiki
  defines rules and templates for
Bootstrap Files and Session Starter
  orient agents and point them to
Workflow Records
  govern the creation of
Source Artifacts
```

The wiki does not change when a project changes. Bootstrap files change only when project structure or paths change. Workflow Records change as a session progresses. Source artifacts change as implementation proceeds.

---

## Common Mistakes

**Burying the session starter.**
The session starter is how the workflow begins. Keep it visible in public documentation and project onboarding.

**Putting workflow rules only in AGENTS.md or CLAUDE.md.**
Bootstrap files should be compact pointers, not copies of the wiki. If rules live only in bootstrap files, every project needs manual updates.

**Treating Workflow Records as chat logs.**
Workflow Records are structured engineering artifacts. They preserve decisions, rationale, critique, state, and approvals.

**Letting implementation drift from frozen scope.**
If implementation needs different scope, stop and start a new review round.
