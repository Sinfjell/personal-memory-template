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

## Structure

```
personal-memory/
├── MEMORY.md          ← routing index, read first
├── ORG.md             ← conventions and review routine
├── CLAUDE.md          ← instructions for the LLM working here
├── log.md             ← append-only changelog
├── clients/           ← one file per client (template: _TEMPLATE.md)
├── companies/         ← your own companies, strategy, finances
├── engineering/       ← patterns, debugging, repo registry
├── playbooks/         ← step-by-step procedures
├── policies/          ← AI use, security, access
├── home/              ← private (housing, finance, training, car)
├── projects/          ← time-bound incidents/events
└── archive/           ← LLM ignores this — old artifacts
```

## Bootstrap

1. **Click "Use this template"** on GitHub (or `git clone` and `rm -rf .git && git init`).
2. **Make it private** — this will hold personal data.
3. **Edit the example files** (or delete them and start blank). The structure matters more than the seed content.
4. **Tell your LLM about it.** Add a section to your global `CLAUDE.md` (or equivalent):

   ```
   My personal knowledge base lives at ~/repositories/personal-memory/.
   Always start by reading MEMORY.md. If I mention a client by name,
   read clients/<name>.md without being asked.
   ```

5. **Use it.** Next time the LLM gives you a good answer, say "save this" — point it at the right file.

## What makes the difference

- **Routing index with a strict line budget.** `MEMORY.md` should fit in one screen — links only, one sentence per file. Without this, the index becomes a dump that doesn't help.
- **One file per topic, never per date.** Date-organized notes are useless as LLM context. Topic-organized are gold.
- **Write for future-you.** If it would help you read this in 6 months, it's good LLM context too.
- **Don't duplicate your task tracker.** Operational state (tasks, deadlines, current status) belongs in Notion/Linear/Jira. This repo is *compiled* knowledge — quirks, decisions, how-things-actually-work.

## Maintenance — three skills worth building

If you use Claude Code, three custom skills (slash commands) keep this alive without effort:

- `/ingest` — after a finished project: distill what was learned into the right file, update `MEMORY.md`, log to `log.md`.
- `/capture` — mid-conversation: "save this" → finds the right file and appends.
- `/wiki-lint` — auditing: stale dates, broken links, orphan files, contradictions.

You don't need these to start. Just open the markdown file and edit it manually. Add automation when the manual part starts feeling tedious.

## License

MIT. Fork it, gut it, rebuild it. The point is the pattern, not the words.
