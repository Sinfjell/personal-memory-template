# Personal Memory — rules for every agent

<!-- The one rules file. Claude Code reads it through CLAUDE.md (`@AGENTS.md`); Codex, Cursor and others
read it directly. Never keep a second copy for another tool — copies drift. Keep this file under 150 lines. -->

This repo is long-term memory: the compiled, curated layer above raw conversations and documents.

## Reading

1. **Start with `MEMORY.md`.** It routes you to the right file. Read that file, not the whole repo.
2. **Client mentioned by name?** Read `clients/<slug>.md` without being asked, then the one deep file its
   reading map (`## Reading map`) points to.
3. **Ignore `archive/`** unless the user asks you to look there.
4. **Check freshness.** A file with `last_verified` older than ~4 months may be wrong. Say so when it matters.

## Writing

- **One topic per file, never one file per date.** Current state goes in the topic file. Dated events go in a
  client's changelog (`clients/<slug>/changelog.md`, or its entry file's Changelog section).
- **Write into the right topic file.** Do not append to a catch-all. If no file fits, create one and add it
  to the index.
- **Never delete information** without explicit instruction. Move it to `archive/` instead.
- **Bump `last_updated`** on every meaningful edit and **`last_verified`** when you re-read a file and confirm
  it is still true.
- **Cite non-obvious claims:** `<!-- Source: <ticket or link>, YYYY-MM-DD -->`.
- **No secrets.** Name the password-manager item, never the value.
- **No binaries.** Screenshots, PDFs and photos go to a drive; link them from the markdown file.

## Size limits (the lint script checks these)

| Thing | Limit | When exceeded |
|-------|-------|---------------|
| `MEMORY.md` | 150 lines, rows ≤ 150 chars | Move a section to `<folder>/INDEX.md`, keep one pointer line |
| Client entry file | 120 lines | Create `clients/<slug>/` from `clients/_TEMPLATE/` and add a reading map |
| Any topic file | 40 KB | Split into a folder with an `INDEX.md` |
| `log.md` | current month | Move older months to `archive/log/YYYY-MM.md` |

Why: an index the agent can't read in full is worse than no index. Claude Code loads only the first 200 lines
or 25 KB of an auto-memory index, and long rule files lower adherence.

## Where things go

| Folder | Holds |
|--------|-------|
| `clients/` | One entry file per client (`_TEMPLATE.md`); a folder per client when it grows (`_TEMPLATE/`) |
| `companies/` | Your own companies: strategy, finances, decisions |
| `engineering/` | `patterns.md` and `debugging/` (one file per topic, listed in `debugging/INDEX.md`) |
| `playbooks/` | Step-by-step procedures |
| `policies/` | Security, access, AI use |
| `home/` | Private: housing, finance, health |
| `skills/` | Procedures, one folder per skill, versioned (see Skills) |
| `projects/` | Time-bound work. When it ends, distil the lessons into a topic file and move it to `archive/` |
| `archive/` | Ignored by default |

## Skills (procedures)

Skills in `skills/<name>/SKILL.md` hold *how* to do a recurring task; the topic files hold the *facts*.

- **Facts live in files, steps live in skills.** A client file never copies a skill's steps; a skill never
  hardcodes client facts — it reads the client file.
- **Point by name, not version.** Reading maps name the skill (`invoice-client`); the version lives in
  the skill's second line and in `.claude-plugin/plugin.json`.
- **Version every change.** Bump the skill's version line and add an `[Unreleased]` entry in
  `CHANGELOG.md`. `.claude/skills` points to `skills/`, so they work in this repo; link single skills into
  `~/.claude/skills/` to use them elsewhere (never install the whole repo as a plugin: it holds private data).

## Knowledge base vs task tracker

The task tracker (Notion, Linear, Jira) holds live state: tasks, deadlines, status, contact lists, meeting
notes. This repo holds what will still be useful **next time** you work on the client or system: quirks,
decisions, how things actually work. Do not copy live state here; link to it.

## Maintenance

- **Ingest:** after a finished piece of work, update every affected topic file, then add one line to `log.md`.
- **Save answers:** when the user says "save this", write the answer into the right topic file.
- **Lint:** run `python3 scripts/lint.py` monthly and before big ingests. Fix errors, then warnings.
- **One rule, one place.** If a rule is needed elsewhere, link to it here instead of restating it.
