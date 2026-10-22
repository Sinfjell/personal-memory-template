# Personal Memory — LLM-maintained knowledge base template

A starter scaffold for keeping a persistent, structured knowledge base that LLMs (Claude Code, ChatGPT, Cursor — anything that can read files) can use as long-term memory.

Inspired by [Andrej Karpathy's "LLM Wiki" gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## The idea

Stop relying on query-time RAG over raw documents. Instead, maintain a *compiled* knowledge layer — a wiki of markdown files where the LLM accumulates synthesis over time. Three layers:

1. **Raw sources** (immutable — emails, docs, conversations)
2. **Wiki** (LLM-owned markdown — this repo)
3. **Schema/config** (`CLAUDE.md` / `AGENTS.md` — rules for how the wiki is structured and maintained)

Three operations:

- **Ingest** — one source updates many pages
- **Query** — when the LLM gives a good answer, save it back into the wiki
- **Lint** — periodic health check for contradictions, stale claims, orphan pages

Why it works: humans abandon wikis because of maintenance overhead. LLMs do the repetitive upkeep (cross-links, deduplication, freshness checks) cheaply, so the knowledge base stays current.

## Two variants

| Variant | For | Where |
|---------|-----|-------|
| **Full** | Claude Code / Codex / Cursor users who want a git repo as long-term memory across all their work, with versioned skills | this repo root |
| **Simple** (Norwegian) | Non-coders who want Claude to answer questions about customers, e.g. invoicing rules. Claude Project or Notion, no git; one uploadable skill | [`enkel/`](enkel/README.md) |

Both variants split **facts** (files: one per client) from **procedures** (skills). A client file points to
the skill by name; the skill reads the client file. Neither copies the other.

## Structure (full variant)

```
personal-memory/
├── MEMORY.md          ← routing index, read first (≤150 lines)
├── AGENTS.md          ← the one rules file (CLAUDE.md just imports it)
├── ORG.md             ← human review routine
├── log.md             ← this month's changes; older months in archive/log/
├── CHANGELOG.md       ← skill changes (Keep a Changelog + SemVer)
├── .claude-plugin/    ← makes the repo a Claude Code plugin
├── skills/            ← procedures: ingest, invoice-client (versioned)
├── clients/           ← entry file per client + a folder when it grows
│   ├── _TEMPLATE.md
│   └── _TEMPLATE/     ← architecture · operations · quirks · changelog
├── companies/         ← your own companies
├── engineering/       ← patterns + debugging/ (one file per topic, INDEX.md)
├── playbooks/  policies/  home/  projects/
├── scripts/lint.py    ← health check, standard library only
└── archive/           ← ignored by agents
```

## Start in five minutes

1. **Clone it** (or "Use this template" on GitHub) and **make your copy private**: it will hold client data.

   ```bash
   git clone https://github.com/Sinfjell/personal-memory-template.git ~/repositories/personal-memory
   ```

2. **Open Claude Code in the folder** (`cd ~/repositories/personal-memory && claude`). The skills in `skills/`
   work there right away (`.claude/skills` points to them).
3. **Add your first client:** "Create a client file for Acme from `clients/_TEMPLATE.md`: …" and paste what you know.
4. **Work as usual. When something is done, run `/ingest`.** It writes what was learned into the right files,
   updates the index and the log, and runs the lint script.
5. **Use it from your other repos:** add this to your global `~/.claude/CLAUDE.md`:

   ```
   My knowledge base lives at ~/repositories/personal-memory/. Start with its MEMORY.md.
   If I mention a client by name, read clients/<name>.md without being asked.
   ```

   To get `/ingest` and the other skills everywhere, install the repo as a plugin:
   `/plugin marketplace add ~/repositories/personal-memory`, then `/plugin install memory@memory`.

6. **Once a month:** `python3 scripts/lint.py` and fix what it finds.

## Lessons from running this for six months

The first version of this template grew to ~800 files in daily use. What broke, and the rule that now prevents it:

| What broke | Rule |
|------------|------|
| The index grew to 300 lines of prose rows, and agents stopped reading all of it | `MEMORY.md` ≤ 150 lines, rows ≤ 150 chars, sub-indexes per folder |
| Claude Code loads only the first 200 lines / 25 KB of its auto-memory index, so the newest notes vanished silently | Keep auto-memory small; promote durable facts into this repo |
| A copied rules file for a second tool drifted until it said the opposite | One `AGENTS.md`; `CLAUDE.md` contains only `@AGENTS.md` |
| "Add bugs to debugging.md" produced a 327 KB file nobody could search | One file per topic plus an index; split anything over 40 KB |
| Client files became diaries: 46 dated sections above the facts | Entry file = current state, ≤ 120 lines; dated events go to `changelog.md` |
| An append-only log reached 1 MB and nothing ever read it | Keep the current month; archive the rest |
| Screenshots and PDFs made the git history 3x the content | Binaries in `.gitignore`; link to a drive |
| The weekly lint stopped and nobody noticed for 3 months | A lint script anyone can run, and a monthly review that starts with it |

## What makes the difference

- **One file per topic, never per date.** Topic files are context; date files are noise.
- **The index routes, the files explain.** If an index row needs a second sentence, it belongs in the file.
- **Don't duplicate your task tracker.** Live state (tasks, deadlines, status) belongs in Notion/Linear/Jira.
- **Write for future-you.** If it would help you in six months, it is good context for the agent too.

## Maintenance skills worth building

- `/ingest` — after a finished piece of work: update the right topic files, one line in `log.md`.
- `/capture` — mid-conversation "save this": find the right file and write it there.
- `/lint` — run `scripts/lint.py`, then ask the agent to check contradictions the script can't see.

`ingest` and an example domain skill (`invoice-client`) ship in `skills/`. The lint script checks that every
skill has a matching name and a version line, that every skill a reading map names exists, and that the
plugin version has a changelog section.

Inspired by [Andrej Karpathy's "LLM Wiki"](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and
the [Claude Code memory docs](https://code.claude.com/docs/en/memory).

## License

MIT. Fork it, gut it, rebuild it. The point is the pattern, not the words.
