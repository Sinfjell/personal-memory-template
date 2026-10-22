#!/usr/bin/env python3
"""Health check for a personal-memory repo. Standard library only.

Usage: python3 scripts/lint.py [repo_root]
Exit code 1 if any ERROR (broken links, oversized index); warnings alone exit 0.
"""
import datetime
import pathlib
import re
import subprocess
import sys

INDEX_MAX_LINES = 150
INDEX_MAX_ROW = 150
ENTRY_MAX_LINES = 120
FILE_MAX_BYTES = 40_000
STALE_DAYS = 120
BINARY_MAX_BYTES = 1_000_000
SKIP_DIRS = {"archive", ".git", "node_modules", "venv", ".venv", ".claude", "build"}
CONTENT_DIRS = {"clients", "companies", "engineering", "playbooks", "policies", "home"}
LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")
DATE_RE = re.compile(r"last[_ ]verified\**:?\**\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def md_files(root):
    for path in sorted(root.rglob("*.md")):
        if not SKIP_DIRS.intersection(path.relative_to(root).parts):
            yield path


def check_index(root, report):
    index = root / "MEMORY.md"
    if not index.exists():
        report("ERROR", "MEMORY.md", "missing routing index")
        return
    lines = index.read_text(encoding="utf-8").splitlines()
    if len(lines) > INDEX_MAX_LINES:
        report("ERROR", "MEMORY.md", f"{len(lines)} lines > {INDEX_MAX_LINES}: move a section to <folder>/INDEX.md")
    for n, line in enumerate(lines, 1):
        if len(line) > INDEX_MAX_ROW:
            report("WARN", f"MEMORY.md:{n}", f"row is {len(line)} chars > {INDEX_MAX_ROW}: keep detail in the target")
        if "](archive/" in line:
            report("WARN", f"MEMORY.md:{n}", "index points into archive/")


def is_placeholder(target):
    """External URLs and template placeholders like <slug>, URL or … are not checked."""
    if re.match(r"^[a-z]+:", target) or target.isupper() or target == "url":
        return True
    return "<" in target or "…" in target


def check_links(root, files, report):
    linked = set()
    for path in files:
        in_code = False
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            for target in LINK_RE.findall(line.replace("`", "")):
                if is_placeholder(target):
                    continue
                resolved = (path.parent / pathlib.Path(target).expanduser()).resolve()
                linked.add(resolved)
                if not resolved.exists():
                    report("ERROR", f"{path.relative_to(root)}:{n}", f"broken link -> {target}")
    return linked


def check_files(root, files, linked, report):
    today = datetime.date.today()
    for path in files:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        size = len(text.encode("utf-8"))
        if size > FILE_MAX_BYTES and rel.name != "log.md":
            limit = FILE_MAX_BYTES // 1000
            report("WARN", str(rel), f"{size // 1000} KB > {limit} KB: split into a folder with INDEX.md")
        is_entry = rel.parts[0] == "clients" and len(rel.parts) == 2 and not rel.name.startswith("_")
        if is_entry and text.count("\n") > ENTRY_MAX_LINES:
            report("WARN", str(rel), f"entry file > {ENTRY_MAX_LINES} lines: create clients/<slug>/ and a reading map")
        match = DATE_RE.search(text)
        if match:
            try:
                age = (today - datetime.date.fromisoformat(match.group(1))).days
            except ValueError:
                report("ERROR", str(rel), f"last_verified '{match.group(1)}' is not a valid date")
                age = 0
            if age > STALE_DAYS:
                report("WARN", str(rel), f"last_verified {age} days ago: re-read and confirm or fix")
        in_content = rel.parts[0] in CONTENT_DIRS
        is_meta = rel.name in {"INDEX.md", "README.md"} or "_TEMPLATE" in str(rel) or rel.parts[0] == "enkel"
        if in_content and not is_meta and path.resolve() not in linked:
            report("WARN", str(rel), "orphan: not linked from MEMORY.md or any other file")


def check_log(root, report):
    log = root / "log.md"
    if not log.exists():
        return
    months = re.findall(r"^## (\d{4}-\d{2})", log.read_text(encoding="utf-8"), re.MULTILINE)
    if len(set(months)) > 1:
        report("WARN", "log.md", f"{len(set(months))} months in the log: move old months to archive/log/")


def check_binaries(root, report):
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return
    for name in filter(None, out.decode("utf-8", "replace").split("\0")):
        path = root / name
        if path.is_file() and path.suffix != ".md" and path.stat().st_size > BINARY_MAX_BYTES:
            report("WARN", name, f"{path.stat().st_size // 1_000_000} MB binary in git: move to a drive and link it")


VERSION_LINE_RE = re.compile(r"^_(?:Version|Versjon) \d+(?:\.\d+){1,2}\b")
SKILL_CELL_RE = re.compile(r"`([a-z0-9][a-z0-9:-]*)`")


def skill_sets(root):
    """Map each skills/ folder (repo root and enkel/) to the skill names it defines."""
    sets = {}
    for skills_dir in [root / "skills", root / "enkel" / "skills"]:
        if skills_dir.is_dir():
            sets[skills_dir] = {p.parent.name for p in skills_dir.glob("*/SKILL.md")}
    return sets


def check_skill_files(root, report):
    for skill in sorted(root.glob("skills/*/SKILL.md")) + sorted(root.glob("enkel/skills/*/SKILL.md")):
        rel = skill.relative_to(root)
        lines = skill.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            report("ERROR", str(rel), "missing frontmatter (name + description)")
            continue
        end = lines.index("---", 1)
        front = dict(line.split(":", 1) for line in lines[1:end] if ":" in line)
        if front.get("name", "").strip() != skill.parent.name:
            report("ERROR", str(rel), f"name must match the folder name '{skill.parent.name}'")
        if len(front.get("description", "").strip()) > 1024:
            report("ERROR", str(rel), "description is over 1024 characters")
        if not any(VERSION_LINE_RE.match(line) for line in lines[end + 1:end + 3]):
            report("WARN", str(rel), "no version line after the frontmatter (e.g. `_Version 0.1.0 · …_`)")


def check_skill_refs(root, files, report):
    """Every name in a 'Skill' table column must exist in the nearest skills/ folder."""
    sets = skill_sets(root)
    for path in files:
        rel = path.relative_to(root)
        local = sets.get(root / "enkel" / "skills") if rel.parts[0] == "enkel" else sets.get(root / "skills")
        column = None
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
            if not cells:
                column = None
            elif column is None:
                column = next((i for i, c in enumerate(cells) if c.lower() == "skill"), None)
            elif column < len(cells) and not set(cells[column]) <= set("-: "):
                for name in SKILL_CELL_RE.findall(cells[column]):
                    if ":" not in name and name not in (local or set()):
                        report("ERROR", f"{rel}:{n}", f"skill '{name}' not found in skills/")


def check_changelog(root, report):
    manifest = root / ".claude-plugin" / "plugin.json"
    changelog = root / "CHANGELOG.md"
    if not manifest.exists():
        return
    match = re.search(r'"version"\s*:\s*"([^"]+)"', manifest.read_text(encoding="utf-8"))
    text = changelog.read_text(encoding="utf-8") if changelog.exists() else ""
    if match and f"## [{match.group(1)}]" not in text:
        report("WARN", "CHANGELOG.md", f"plugin version {match.group(1)} has no changelog section")


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = []

    def report(level, where, message):
        findings.append((level, where, message))

    files = list(md_files(root))
    check_index(root, report)
    linked = check_links(root, files, report)
    check_files(root, files, linked, report)
    check_log(root, report)
    check_binaries(root, report)
    check_skill_files(root, report)
    check_skill_refs(root, files, report)
    check_changelog(root, report)

    for level, where, message in sorted(findings):
        print(f"{level:5} {where}: {message}")
    errors = sum(1 for f in findings if f[0] == "ERROR")
    print(f"\n{len(files)} files checked · {errors} errors · {len(findings) - errors} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
