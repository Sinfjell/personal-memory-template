---
name: setup
description: Use when the knowledge base is new or nearly empty, or when the user says "setup", "set up my memory", "kom i gang", "sett opp kunnskapsbanken", "interview me". Interviews the user one question at a time (who they are, companies, key clients and how they are invoiced, systems, recurring tasks, where information lives today), then fills the templates, the index and the first skills, and runs the lint script.
---
_Version 0.2.0 · source: skills/setup/SKILL.md_

# Setup interview

Turn an empty template into a working knowledge base in one sitting. The rules for where things go are in
[`AGENTS.md`](../../AGENTS.md); this skill is the procedure. Interview in the user's language and write the
file content in that language too (template headings may stay as they are).

## 0. Safety first

- Run `git remote -v`. For a GitHub remote, run `gh repo view --json visibility -q .visibility`.
  **Public → stop:** tell the user to make it private (Settings → General → Danger zone) before any client
  data goes in. No remote, or no `gh`: say you couldn't check, ask the user to confirm it is private, and warn
  that any remote they add later must be private too.
- Never ask for or write passwords, API keys or card numbers. Ask *where* a secret lives
  (password-manager item name), not what it is.

## 1. Interview

Ask **one question at a time**, wait for the answer, and keep a short running summary. Every question can be
skipped ("skip" / "hopp over"). Stop when the user says "done". Destinations in brackets.

1. **You:** name, role, what you spend most of your week on. [`AGENTS.md` → About the user]
2. **Companies:** which companies or organisations you work in or own, and your role in each. [`companies/<slug>.md`]
3. **Clients, most important first (up to 5):** name, what they buy, contact person. [`clients/<slug>.md` Overview]
4. **Invoicing — ask once per client named in 3:** price and interval, where invoices go, special rules
   (PO number, approval, no invoice in July). Say the accounting system stays the source of truth for prices.
   [client file → Agreement and invoicing]
5. **Systems:** accounting, CRM, task tracker, hosting, e-mail, password manager. One line each.
   [`companies/<slug>.md` → Systems; password-manager item names → client Access tables]
6. **Recurring tasks:** what you do every week or month with the same steps (invoicing, reports, onboarding).
   [skill candidates, step 3]
7. **Where information lives today:** Notion pages, Drive folders, e-mail threads, old docs.
   [`projects/setup-ingest-queue.md`]
8. **Rules for the assistant:** anything it must always or never do (never send e-mail, always Norwegian,
   ask before touching invoices). [`AGENTS.md` → About the user]

## 2. Build

Show the plan (files to create or move, one line each) and **ask for a go-ahead once** before writing. Then:

- **`AGENTS.md`:** add `## About the user` directly under the H1: one line from answer 1, then the rules from
  answer 8 as bullets.
- **`companies/<slug>.md`** per company, with the user's role and a `## Systems` list from answer 5.
- **`clients/<slug>.md`** per client, copied from `clients/_TEMPLATE.md`:
  - Fill Overview (incl. **Buys**) and Agreement and invoicing. Set `owner` to the user's name, and
    `last_updated` and `last_verified` to today. Unknown → `[unknown]`; never guess a price or a date.
  - Access: one row per system the client uses, with the password-manager item name if given, else `[unknown]`.
  - Reading map: keep only rows that point at something that exists. Without a client folder, that is the
    invoicing row (`| Invoicing | Agreement section above | invoice-client |`) and rows for accepted skills.
  - Keep Known quirks, Changelog and See also as empty headings.
- **`projects/setup-ingest-queue.md`:** a checklist of the sources from answer 7, newest or most used first.
- **Move the examples to `archive/`** (`git mv clients/example-client.md archive/`, same for
  `companies/your-company.md`) once real files exist. Never delete: `AGENTS.md` says archive instead.
- **`MEMORY.md`:** one row per new file; remove the rows for the archived examples.
- **`log.md`:** `YYYY-MM-DD — created — setup interview — clients: <n>, companies: <n>`.

## 3. First skills

For each recurring task from answer 6, propose a skill in one line: name, trigger, what it reads.

- **Before creating one, ask the facts it needs** (e.g. a report: who receives it, what it contains, when) and
  write those facts into the client or company file. The skill only holds steps.
- **`invoice-client` already exists.** Put client-specific rules in the client files, not in the skill.
  Change the skill's steps only for rules that apply to every client (e.g. "ask for hours on hourly clients").
- Create only the skills the user accepts, in the format of `skills/invoice-client/SKILL.md`: frontmatter
  `name` = folder name, a version line, steps that read client files.
- **Versioning:** new skill → version line `0.1.0`; changed skill → bump its patch number. Add one line per
  skill under `[Unreleased]` in `CHANGELOG.md`. Leave `.claude-plugin/plugin.json` alone; that is bumped when
  a version is cut. Each new skill gets a `MEMORY.md` row.

## 4. Finish

1. Run `python3 scripts/lint.py`. Fix every error; warnings about placeholders are fine.
2. Show what was created or moved, one line per file.
3. Next step: the first 2-3 items in `projects/setup-ingest-queue.md` to `/ingest`, and "after each piece of
   work, run `/ingest`".
4. Offer to commit (`git add -A && git commit -m "feat: set up knowledge base"`). Before any push, re-run the
   visibility check from step 0; never push without asking.
