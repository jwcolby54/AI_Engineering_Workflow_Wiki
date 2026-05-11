#!/usr/bin/env python3
"""Bootstrap AI Engineering Workflow records and starter prompts."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
from pathlib import Path


DEFAULT_WIKI = Path(r"E:\AI\AI_Engineering_Workflow_Wiki")


MOJIBAKE_REPLACEMENTS = {
    "â€”": "-",
    "â€“": "-",
    "â€˜": "'",
    "â€™": "'",
    "â€œ": '"',
    "â€\x9d": '"',
    "Â": "",
}


def clean_text(text: str) -> str:
    for bad, good in MOJIBAKE_REPLACEMENTS.items():
        text = text.replace(bad, good)
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
- Human remains final authority."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, help="Project/repo root for the workflow.")
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
