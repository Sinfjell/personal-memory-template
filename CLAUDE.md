# Personal Memory — LLM Instructions

This repo is your long-term memory. It's the compiled, curated layer above raw conversations and source documents.

## How to use this repo

**Start with `MEMORY.md`** — it's the routing index. Find the right file based on the task, then read that file.

### When working in OTHER repos

Reference this repo for context whenever you need:

- Client details → `clients/<name>.md`
- Strategy or company decisions → `companies/`
- Coding standards and patterns → `engineering/`
- Security and access policies → `policies/`

If the user mentions a client by name, read `clients/<name>.md` without being asked.

### When working IN this repo

You're updating the knowledge base itself. Rules:

- **Never delete information** without explicit instruction
- **Update `MEMORY.md`** if you add or remove files
- **Use `clients/_TEMPLATE.md`** as the base for new client files
- **Keep files focused** — one topic per file, details in the file, not in `MEMORY.md`
- **Update timestamps** — `Sist oppdatert` / `Last updated` and `Sist verifisert` / `Last verified`
- **Append to `log.md`** when making non-trivial changes (newest first, max ~200 entries)

## File conventions

| File | Purpose |
|------|---------|
| `MEMORY.md` | Routing index. Max 200 lines. Links + one-line descriptions only. |
| `ORG.md` | Operating rules and review routine. |
| `CLAUDE.md` | This file — instructions for the LLM. |
| `log.md` | Append-only changelog. |
| `clients/` | One file per client. Follows `_TEMPLATE.md`. |
| `companies/` | Your own companies, strategy, finances. |
| `engineering/` | Patterns, standards, debugging knowledge. |
| `playbooks/` | Step-by-step procedures. |
| `policies/` | Security, access, AI use rules. |
| `home/` | Personal/household info. |
| `projects/` | Time-bound (incidents, events). Distill into `clients/`/`engineering/` when resolved. |
| `archive/` | **IGNORE** unless explicitly asked. Conversation artifacts. |

## Knowledge base vs task tracker

- **Task tracker** (Notion / Linear / Jira) = live operational state — tasks, deadlines, current status
- **This repo** = compiled knowledge — quirks, patterns, decisions, how-things-actually-work

**Do not duplicate.** Contact info, task status, meeting notes, project progress — those belong in the task tracker. If information is useful *next time you work on this client/system*, regardless of any specific task → it belongs here.

## Citations and cross-references

When making non-obvious claims, add a citation comment:

```markdown
<!-- Source: TSK-12345, 2026-01-15, https://link/to/source -->
```

When pages relate to each other, add a `## Se også` / `## See also` section with bidirectional links.

## Adding new knowledge

1. Find the right file (or create one based on `_TEMPLATE.md`)
2. Update it with what was learned
3. Bump `Sist oppdatert` / `Last updated`
4. Append a one-line entry to `log.md`
5. Update `MEMORY.md` if a new file was created
