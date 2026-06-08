# Human Authority Model

## The Human Is Not a Rubber Stamp

The Human operator holds structural authority at multiple points in the workflow. This is not ceremonial - it is load-bearing. The workflow degrades if the Human is treated as a passive approver at the end.

---

## Where Human Authority Is Required

### Requirements Definition
The Human defines what the system must do. AI systems propose how to do it. Requirements are not negotiable by AIs - they can flag conflicts or concerns, but requirements belong to the Human.

### Scope Waivers
If a `MAJOR` concern remains unresolved at the implementation gate, only the Human can grant an explicit waiver. The waiver must be recorded in the Workflow Record with a stated reason.

### Implementation Gate Approval
Implementation does not begin until the Human explicitly approves. Both AI approvals are necessary but not sufficient. The Human may decline even when both AIs recommend proceeding.

### Deadlock Resolution
After three review rounds without convergence, the Human becomes the explicit casting authority. The Human's decision resolves the deadlock and is recorded as authoritative in the Workflow Record.

### Scope Changes After Freeze
Any change to frozen scope requires Human awareness. The new review round that a scope change triggers must produce a Human-approved outcome before implementation continues.

---

## What AI Systems Must Not Do

- Self-approve deployment or implementation
- Treat AI convergence as equivalent to Human approval
- Silently redefine requirements based on what seems technically preferable
- Expand scope without Human acknowledgment
- Resolve a deadlock by simply choosing a side

---

## Human Override

The Human may override any workflow rule with an explicit recorded decision. This includes:
- Skipping review rounds when a decision is obvious
- Granting waivers for unresolved concerns
- Unblocking a gate without full AI convergence

Human overrides are legitimate. They must be recorded. An undocumented override is a governance gap.

---

## Practical Implication

The workflow is not designed to remove the Human from engineering decisions. It is designed to give the Human better-reviewed proposals to decide on, a clear record of what was considered, and a explicit gate where their judgment is applied.

Less time re-litigating old decisions. More time making new ones with full context.
