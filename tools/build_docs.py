"""Build the mkdocs source tree (docs/) from the repo-root pages.

The repo root is the single source of truth for these pages:

    concepts/, governance/, index.md, session_starter_template.md

mkdocs builds from docs/, so this script copies them there and rewrites
relative links that differ between the two layouts:

    root layout                      docs/ layout
    templates/X                  ->  workflow-templates/X
    docs/X (from the root)       ->  X
    ../docs/X (from a subfolder) ->  ../X
    ../templates/X               ->  ../workflow-templates/X

The generated files are gitignored. Run this before `mkdocs build --strict`
(the Pages workflow does it). Hand-written docs/ files (start.md, the
workflow-templates/, the Active/History templates, raw/, examples/) are not touched.
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TREES = ["concepts", "governance"]
FILES = ["index.md", "session_starter_template.md"]

LINK = re.compile(r"(\]\()([^)\s#]+)")


def rewrite_target(target: str) -> str:
    for prefix, repl in (
        ("../docs/", "../"),
        ("../templates/", "../workflow-templates/"),
        ("docs/", ""),
        ("templates/", "workflow-templates/"),
    ):
        if target.startswith(prefix):
            return repl + target[len(prefix):]
    return target


def rewrite(text: str) -> str:
    return LINK.sub(lambda m: m.group(1) + rewrite_target(m.group(2)), text)


def build() -> int:
    count = 0
    for tree in TREES:
        dest = DOCS / tree
        if dest.exists():
            shutil.rmtree(dest)
        for src in sorted((ROOT / tree).rglob("*.md")):
            out = DOCS / src.relative_to(ROOT)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(rewrite(src.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
            count += 1
    for name in FILES:
        out = DOCS / name
        out.write_text(rewrite((ROOT / name).read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        count += 1
    return count


if __name__ == "__main__":
    print(f"build_docs: wrote {build()} files under {DOCS}")
    sys.exit(0)
