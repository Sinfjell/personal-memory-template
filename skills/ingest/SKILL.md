---
name: ingest
description: Use after a finished piece of work, or when the user says "ingest", "save what we learned", "update the knowledge base". Distils lessons into the right topic files of this knowledge base, updates indexes and the log, and runs the lint script.
---
_Version 0.1.0 · source: skills/ingest/SKILL.md_

# Ingest

Turn finished work into knowledge the next session can use. The rules for where things go are in
[`AGENTS.md`](../../AGENTS.md); this skill is the procedure.

## Steps

0. **Find the knowledge base.** If the current folder has `MEMORY.md` and `AGENTS.md`, it is the knowledge base.
   Otherwise use the path named in the global `~/.claude/CLAUDE.md` (default `~/repositories/personal-memory`).
   All paths below are relative to that folder; run commands there (`cd` or `git -C`).
1. **List what was learned.** Only things useful *next time*: decisions, quirks, how something actually
   works. Skip task status and meeting notes — those stay in the task tracker.
2. **Pick the file for each item.** Client fact → the client's entry file or folder. Bug that took
   more than an hour → `engineering/debugging/<topic>.md`. Procedure → a playbook or a skill. Never a
   catch-all file.
3. **Write current state, not history.** Replace outdated text. Dated events go to the client's
   `changelog.md`.
4. **Update stamps and indexes.** Bump `last_updated` (and `last_verified` where you checked).
   New file → add it to `MEMORY.md` or the folder's `INDEX.md`. Add one line to `log.md`.
5. **Run `python3 scripts/lint.py <knowledge-base path>`.** Fix every error before you finish.
6. **Report** the files you changed, one line each.

## Do not

- Copy a skill's steps into a client file, or client facts into a skill. Link instead.
- Delete information without being asked. Archive it.
