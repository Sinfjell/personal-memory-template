---
owner: you              # who keeps this file current
type: client
last_updated: YYYY-MM-DD
last_verified: YYYY-MM-DD
---

# [Client name]

<!-- Entry file. Max 120 lines: who they are, how to get in, the agreement, and where to read next.
Current state only. Dated events go to <slug>/changelog.md (or a "Changelog" section while small). -->

## Overview

- **Website:** https://example.com
- **Primary contact:** [Name], [role] — details live in the CRM / task tracker
- **Stack / hosting:** [WordPress on Hetzner / Next.js on Vercel / …]
- **Repos:** `~/repositories/<repo>`
- **Task tracker:** [link]

## Agreement and invoicing

| What | Value |
|------|-------|
| Agreement | [SLA / hosting / hourly], signed YYYY-MM-DD, [link to the signed copy] |
| Price | [amount] per [month / year / hour] — the accounting system is the source of truth |
| Invoice | [monthly in advance / quarterly / on delivery], sent to [invoice email / EHF] |
| Special rules | [e.g. PO number required, no invoice in July] |

## Access

| System | URL / host | Access via |
|--------|-----------|-----------|
| Admin | https://example.com/admin | Password manager: `[item name]` |
| Hosting | | Password manager: `[item name]` |

## Reading map

<!-- Add this section when the client gets a folder (copy clients/_TEMPLATE/ to clients/<slug>/).
Point to the ONE file to read for each kind of task. -->

| Task | Read |
|------|------|
| Changing code or structure | [`<slug>/architecture.md`](_TEMPLATE/architecture.md) |
| Deploy, hosting, backups | [`<slug>/operations.md`](_TEMPLATE/operations.md) |
| Something behaves oddly | [`<slug>/quirks.md`](_TEMPLATE/quirks.md) |
| What happened when | [`<slug>/changelog.md`](_TEMPLATE/changelog.md) |

## Known quirks

<!-- While the client has no folder: short bullets here. Move to <slug>/quirks.md when this passes ~20 lines. -->

## See also

- [Deploy playbook](../playbooks/deploy.md)
