# [Project Name] - [Topic] History Record

**Active Record:** `WorkflowRecords/YYYY-MM-DD_<topic>.active.md`
**Topic ID:** `YYYY-MM-DD_<topic>`
**Archive Created:** [DATE]
**Append-Only Rule:** Content is added to this file. Existing content is never
rewritten silently. Corrections require a new correction event; see below.

---

# How To Use This File

This file is the completed history archive for the paired active workflow record.
It contains material that was pruned from the active record because it is no longer
needed to continue the current work.

- Do NOT read this file by default. Read it only when the active record explicitly
  says archived context is required for your next action.
- Do NOT edit existing archive events. Add a correction event if an archive event
  contains an error.
- Do NOT summarize verbatim content. All pruned content must be copied verbatim
  from the active record unless the Human explicitly approves a summary and the
  approval is recorded in the archive event.

---

# Archive Events

<!-- Append each new Prune Event below. Do not insert between prior events.
     Use the stable event ID format: ARCHIVE-YYYY-MM-DD-NNN (NNN = 001, 002, ...).
     Event IDs are permanent. Do not reassign or reuse them. -->

<!-- EXAMPLE EVENT (remove this block when creating a real history record):

## ARCHIVE-YYYY-MM-DD-001

**Timestamp:** [YYYY-MM-DD HH:MM TZ]
**Actor:** [AI_1 / AI_2 / Human - who performed the prune]
**Reason:** [Why this material was pruned - e.g., "Round 1 resolved; scope frozen"]
**Source Sections:** [Section IDs or descriptions from the active record that were moved]
**Content Type:** [verbatim / Human-approved summary]

---

[Copied content from the active record follows exactly as it appeared in File A]

---

END ARCHIVE-YYYY-MM-DD-001

-->

<!-- EXAMPLE CORRECTION EVENT:

## ARCHIVE-YYYY-MM-DD-002-CORRECTION

**Corrects:** ARCHIVE-YYYY-MM-DD-001
**Timestamp:** [YYYY-MM-DD HH:MM TZ]
**Actor:** [who made the correction]
**Reason:** [what was wrong and why]

[Corrected content or annotation - does not overwrite the original event]

END ARCHIVE-YYYY-MM-DD-002-CORRECTION

-->
