#!/usr/bin/env python3
"""Bootstrap AI Engineering Workflow records and starter prompts."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


DEFAULT_WIKI = Path(r"E:\AI\AI_Engineering_Workflow_Wiki")


ASCII_TRANSLATION = {
    0x00A0: " ",
    0x2011: "-",
    0x2013: "-",
    0x2014: "-",
    0x2018: "'",
    0x2019: "'",
    0x201C: '"',
    0x201D: '"',
    0x2026: "...",
    0x2190: "<-",
    0x2192: "->",
    0x2194: "<->",
    0x2248: "~=",
    0x2260: "!=",
    0x2264: "<=",
    0x2265: ">=",
    0x2705: "[OK]",
    0x274C: "[NO]",
}


def clean_text(text: str) -> str:
    text = text.translate(ASCII_TRANSLATION)
    text = text.encode("ascii", errors="ignore").decode("ascii")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "workflow"


def read_template(path: Path) -> str:
    return clean_text(path.read_text(encoding="utf-8-sig"))


def write_text(path: Path, text: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"{path} already exists; pass --overwrite to replace it")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def create_record(args: argparse.Namespace, wiki_root: Path) -> Path:
    if args.workflow_record:
        record_path = Path(args.workflow_record)
    else:
        date = args.date or dt.date.today().isoformat()
        records_dir = Path(args.records_dir) if args.records_dir else Path(args.project_root) / "WorkflowRecords"
        record_path = records_dir / f"{date}_{slugify(args.topic)}.md"

    if args.no_create_record:
        return record_path

    template = read_template(wiki_root / "templates" / "AI_Workflow_Record_Template.md")
    today = args.date or dt.date.today().isoformat()
    text = template
    text = text.replace("[Project Name]", args.project_name or Path(args.project_root).name)
    text = text.replace("[Topic]", args.topic)
    text = text.replace("[DATE]", today)
    text = text.replace("[Claude / ChatGPT / Codex / other]", args.ai1, 1)
    text = text.replace("[Claude / ChatGPT / Codex / other]", args.ai2, 1)
    text = text.replace("[One-line session description]", args.topic)
    text = text.replace("[Proposal / Critique / Revision / Final Review / Scope Freeze / Gate / Implementation / Validation]", "Proposal")
    text = text.replace("[Round 1]", "Round 1")
    text = text.replace("[None / summary of unresolved BLOCKING or MAJOR concerns]", "None yet")
    text = text.replace("[No / Yes - see [Scope Freeze](#6-scope-freeze)]", "No")
    text = text.replace("[BLOCKED_PENDING_REVIEW / CLEARED / other - see [Implementation Gate](#7-implementation-gate)]", "BLOCKED_PENDING_REVIEW")
    text = text.replace("[AI_1 / AI_2 / Human]", args.role)
    text = text.replace("[One sentence]", f"{args.role} should draft the initial proposal for {args.topic}.")
    text = text.replace(
        "[What engineering decision or design is being worked out in this session? Be specific enough that both AIs can evaluate proposals against it.]",
        args.objective or f"Define and review the engineering approach for {args.topic}.",
    )
    write_text(record_path, text, args.overwrite)
    return record_path


def install_bootstrap(args: argparse.Namespace, wiki_root: Path) -> list[Path]:
    mode = args.install_bootstrap
    if mode == "none":
        return []

    project_root = Path(args.project_root)
    installed: list[Path] = []
    pairs = []
    if mode in {"agents", "both"}:
        pairs.append(("AGENTS_md_Project_Template.md", "AGENTS.md"))
    if mode in {"claude", "both"}:
        pairs.append(("CLAUDE_md_Project_Template.md", "CLAUDE.md"))

    for src_name, dest_name in pairs:
        src = wiki_root / "templates" / src_name
        dest = project_root / dest_name
        text = read_template(src)
        match = re.search(r"```markdown\n(.*?)\n```", text, flags=re.DOTALL)
        if match:
            text = match.group(1).rstrip() + "\n"
        write_text(dest, text, args.overwrite_bootstrap)
        installed.append(dest)
    return installed


def starter_block(wiki_root: Path, record_path: Path, role: str) -> str:
    role_text = "AI_1 proposing" if role == "AI_1" else "AI_2 reviewing"
    return f"""This engineering session follows the AI Engineering Workflow model.

Wiki:            {wiki_root}
Read first:      index.md, then governance/AI_Agent_Instructions.md
Workflow Record: {record_path}
My role:         {role_text}

Requirements:
- Read the wiki before proceeding. Do not rely on training knowledge of this workflow.
- Update the Workflow Record as reasoning evolves, not at the end.
- Use adversarial review semantics and severity levels (BLOCKING/MAJOR/MINOR/FUTURE).
- Respect frozen scope. Do not implement before the gate is cleared.
- Human remains final authority.
- Use plain ASCII only in all Workflow artifacts. No Unicode punctuation, arrows, math symbols, box drawing, emojis, non-breaking spaces, or zero-width characters."""


def ask(prompt: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{prompt}{suffix}: ").strip()
        if value:
            return value
        if default is not None:
            return default
        print("Please enter a value.")


def ask_choice(prompt: str, choices: set[str], default: str) -> str:
    choice_list = "/".join(sorted(choices))
    while True:
        value = ask(f"{prompt} ({choice_list})", default).lower()
        if value in choices:
            return value
        print(f"Please choose one of: {choice_list}")


def apply_interactive_defaults(args: argparse.Namespace) -> argparse.Namespace:
    if args.project_root:
        return args

    print("AI Engineering Workflow bootstrap")
    print("---------------------------------")
    print("Press Enter to accept a value shown in brackets.\n")

    args.project_root = ask("What is the root directory for this project?")
    project_name = Path(args.project_root).name
    args.project_name = args.project_name or ask("Project name", project_name)
    args.objective = args.objective or ask("What is the stated purpose of this Workflow?")
    args.topic = ask("Short topic for the Workflow Record filename", slugify(args.objective).replace("_", " ")[:48].strip())

    bootstrap = ask_choice("Install project bootstrap files", {"none", "agents", "claude", "both"}, "both")
    args.install_bootstrap = args.install_bootstrap if args.install_bootstrap != "none" else bootstrap

    active_role = ask_choice("Which role is this AI playing", {"ai_1", "ai_2"}, args.role.lower())
    args.role = active_role.upper()

    second_ai = ask_choice("Print a starter block for a second reviewing AI", {"yes", "no"}, "yes")
    if second_ai == "yes":
        args.reviewer_role = "AI_2"

    overwrite = ask_choice("Overwrite existing Workflow Record if the same filename exists", {"yes", "no"}, "no")
    args.overwrite = args.overwrite or overwrite == "yes"

    overwrite_bootstrap = ask_choice("Overwrite existing AGENTS.md/CLAUDE.md if present", {"yes", "no"}, "no")
    args.overwrite_bootstrap = args.overwrite_bootstrap or overwrite_bootstrap == "yes"
    return args


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", help="Project/repo root for the workflow. If omitted, prompts interactively.")
    parser.add_argument("--topic", default="workflow", help="Short workflow topic used for filename and title.")
    parser.add_argument("--objective", help="Objective text for a new Workflow Record.")
    parser.add_argument("--project-name", help="Project name for the record header.")
    parser.add_argument("--wiki-root", default=str(DEFAULT_WIKI), help="AI Engineering Workflow wiki path.")
    parser.add_argument("--records-dir", help="Override WorkflowRecords directory.")
    parser.add_argument("--workflow-record", help="Existing or desired Workflow Record path.")
    parser.add_argument("--date", help="Date to use, default today, YYYY-MM-DD.")
    parser.add_argument("--role", choices=["AI_1", "AI_2"], default="AI_1")
    parser.add_argument("--reviewer-role", choices=["AI_2"], help="Also print a second-AI starter.")
    parser.add_argument("--ai1", default="Codex / Claude / ChatGPT")
    parser.add_argument("--ai2", default="Codex / Claude / ChatGPT")
    parser.add_argument("--install-bootstrap", choices=["none", "agents", "claude", "both"], default="none")
    parser.add_argument("--no-create-record", action="store_true")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing Workflow Record.")
    parser.add_argument("--overwrite-bootstrap", action="store_true", help="Overwrite existing AGENTS.md/CLAUDE.md.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args = apply_interactive_defaults(args)
    wiki_root = Path(args.wiki_root)
    if not wiki_root.exists():
        raise SystemExit(f"Wiki root not found: {wiki_root}")

    record_path = create_record(args, wiki_root)
    installed = install_bootstrap(args, wiki_root)

    print(f"Wiki: {wiki_root}")
    print(f"Workflow Record: {record_path}")
    if not args.no_create_record:
        print("Record status: created" if record_path.exists() else "Record status: planned")
    for path in installed:
        print(f"Installed bootstrap: {path}")

    print("\n=== Paste to active AI ===")
    print(starter_block(wiki_root, record_path, args.role))

    if args.reviewer_role:
        print("\n=== Paste to reviewing AI ===")
        print(starter_block(wiki_root, record_path, args.reviewer_role))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
