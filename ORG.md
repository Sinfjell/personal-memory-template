# Operating Rules

> Keep this short. Max 5 min read. Details belong in the underlying files.

## How we work

- Every document has a named owner who keeps it current
- Updates happen via the `/ingest` skill (after projects) or `/capture` (mid-conversation), or by manual edit
- "Sist oppdatert" / "Last updated" date is bumped on every meaningful change
- "Sist verifisert" / "Last verified" date is bumped when we re-read a file and confirm it's still correct

## What we don't do

- Don't delete information without explicit instruction — archive instead
- Don't duplicate operational state from your task tracker (Notion / Linear / Jira) — link to it
- Don't put secrets in this repo — use a password manager

## Review routine

### Monthly review (1st Monday of the month)

1. **Clients** — Are files up to date? New clients missing a file? Closed clients to archive?
2. **Playbooks** — Have workflows changed? New processes worth documenting?
3. **Engineering** — New patterns, debugging lessons, infra changes?
4. **Policies** — Anything outdated?
5. **Verification** — Run `/wiki-lint` (or manually scan) and update "Last verified" on files that are still correct.
6. **Log trim** — If `log.md` has > 200 entries, drop the oldest.

### After larger projects (ingest)

1. Update the client file with lessons learned, new systems, changed stack
2. Add reusable patterns to `engineering/patterns.md`
3. Add hard-to-debug issues to `engineering/debugging.md`
4. Update `MEMORY.md` if new files were added

## Archive

`archive/` holds conversation artifacts (screenshots, prototypes, drafts) that aren't compiled knowledge but might have value later.

- LLMs **ignore** `archive/` unless explicitly asked to look there
- Organize in subfolders by project/context
- Don't list archive files in `MEMORY.md`
