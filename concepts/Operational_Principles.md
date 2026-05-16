# Operational Principles

These principles explain why the workflow is designed the way it is. Understanding them is necessary to apply the workflow correctly in edge cases.

---

## Chats Are Not Records

A chat session is a working surface, not a durable artifact. Reasoning made in chat that is not externalized into the Workflow Record is lost. This is not a failure of memory - it is a structural property of chat systems. The Workflow Record is the system of record. The chat is the scratch pad.

## Different AIs Have Different Blind Spots

The value of adversarial review is not that two AIs produce more output. It is that they have different failure modes. In observed sessions, Claude tends toward governance structure and process correctness; ChatGPT tends toward operational mechanics and state transition semantics. Running a proposal through both surfaces problems that either system alone would normalize.

This asymmetry is a feature. It should be preserved and not collapsed into a single AI reviewing its own proposal.

## Convergence Must Be Earned, Not Declared

A proposal is not approved because no one objected. It is approved because concerns were raised, addressed, and explicitly resolved. The record shows this history. A `NEEDS_REVISION` state that was never recorded means the revision either did not happen or cannot be verified.

## Scope Freeze Is Non-Negotiable

AI-assisted workflows drift. AI_1 approves one design. AI_2 implements a variation it considers equivalent. The Human recalls a third version from an earlier chat. Without an explicit scope freeze, these divergences are invisible until they become bugs.

Freeze pins the approved version. Any change after freeze is a new decision requiring new review.

## Severity Exists To Enable Convergence

Without severity levels, every concern carries equal weight and review loops become endless. A `MINOR` concern about naming convention should not block implementation the same way a `BLOCKING` concern about a missing convergence gate does. Severity creates prioritization and enables closure.

## Delay Automation Until The Protocol Matures

The workflow must first be used manually on real projects to discover its failure modes. Automating prematurely locks in bad assumptions. The structured Markdown format is already machine-readable by design - when automation is appropriate, it can be added without restructuring the artifacts.

## Human Authority Is Structural, Not Ceremonial

The Human does not simply rubber-stamp AI decisions. The Human defines requirements, grants scope waivers for unresolved `MAJOR` concerns, resolves deadlocks between AI systems, and controls the implementation gate. These are load-bearing responsibilities. An AI that treats the implementation gate as a formality has broken the governance model.

## Preserve History, Never Overwrite It

When a revision is made to a Workflow Record, the prior round is preserved. The record shows the evolution of the decision. Future AI systems, future humans, and future automation tools depend on being able to read that evolution. Silent rewrites break auditability.

## Commit To Git At Gate Events

The Workflow Record is the system of record for decisions. Git is the external backup and audit trail for all project artifacts. These are complementary - the Workflow Record shows why; git shows what changed and when.

Commit project artifacts to git at each major gate event: IMPLEMENTED and VALIDATED at minimum. Do not let a session close without committing the work it produced. This is easy to forget and painful to reconstruct later.

AI agents should prompt the Human to commit if it has not been done at the end of a session.
