# Operating rules

> Max 5 minutes to read. The rules for agents live in [`AGENTS.md`](AGENTS.md); this file is the human routine.

## What we don't do

- Delete information without being asked. Archive instead.
- Copy live state (tasks, status, contacts) from the task tracker. Link to it.
- Store secrets or binaries. Password manager for secrets, a drive for files.
- State the same rule in two files. One place, one link.

## Monthly review (first Monday)

1. **Lint:** `python3 scripts/lint.py`. Fix every error, then the warnings worth fixing.
2. **Rotate the log:** move last month's lines from `log.md` to `archive/log/YYYY-MM.md`.
3. **Clients:** new clients without a file? Finished ones to archive? Entry files over 120 lines → folder.
4. **Projects:** finished ones → distil lessons into topic files, move the folder to `archive/`.
5. **Verify:** re-read the files lint flags as stale and bump `last_verified`, or fix them.

## After a larger piece of work (ingest)

1. Update the client file and the topic files the work touched — the right file, not a catch-all.
2. Add a debugging entry to the matching `engineering/debugging/<topic>.md`, if a bug took more than an hour.
3. Add one line to `log.md`. Add the new files to `MEMORY.md` or the folder's `INDEX.md`.

## Archive

`archive/` holds old logs, finished projects and drafts. Agents ignore it unless asked. Never list it in `MEMORY.md`.
