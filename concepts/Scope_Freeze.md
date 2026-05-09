# Scope Freeze

## The Problem Scope Freeze Solves

AI-assisted workflows drift silently. The pattern is:

1. AI_1 proposes Design A
2. AI_2 critiques and recommends Design B
3. AI_1 revises to Design A.1, which it considers equivalent to B
4. AI_2 reviews and approves, believing it approved B
5. Implementation targets A.2, a further variation the Human recalls from an earlier session
6. Nothing in the record captures which version was actually approved

Scope freeze closes this gap. Once both AIs converge, the approved scope is documented explicitly. Everything after that point targets that version, not any AI's mental model of it.

---

## What Gets Frozen

The scope freeze section of a Workflow Record documents:

- **Approved scope version** — a version number tied to the Workflow Record version
- **What is in scope** — the specific decisions, structures, semantics, and behaviors that are approved for implementation
- **What is explicitly out of scope** — things that were discussed but deferred, to prevent scope creep during implementation

---

## Rules

- Scope freeze occurs after AI convergence and before the implementation gate
- Implementation must target the frozen scope, not any prior or later variation
- Any change to frozen scope requires:
  1. A new review round
  2. A version increment on the Workflow Record
  3. Updated scope freeze documentation
- Silent scope drift — implementing something other than the frozen scope without a new round — is a governance violation

---

## Scope Freeze Is Not Scope Perfection

The frozen scope does not need to be perfect. It needs to be agreed-upon and documented. A known imperfection in the frozen scope that both AIs accept is better than an undocumented "improvement" that was never reviewed.

Improvements belong in `FUTURE` severity concerns, or in a new Workflow Record after the current one reaches `VALIDATED`.
