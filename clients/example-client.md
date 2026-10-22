---
owner: you
type: client
last_updated: 2026-10-22
last_verified: 2026-10-22
---

# Example Client

> This is a worked example. Delete this file when starting your own knowledge base, or replace its contents with a real client.

## Overview

- **Website:** https://example.com
- **Primary contact:** Jane Doe — jane@example.com
- **Hosting:** Hetzner Plesk
- **SSH alias:** `htz_example`
- **CMS / stack:** WordPress + custom plugin
- **Repos:** `~/repositories/example-website`

## Systems and access

| System | URL / host | Access via |
|--------|-----------|-----------|
| WordPress admin | https://example.com/wp-admin | 1Password: `Example: WP admin` |
| Hosting panel | https://plesk.example.host | 1Password: `Example: Plesk` |
| SSH | | SSH alias: `htz_example` |
| DNS | Cloudflare | 1Password: `Example: Cloudflare` |

## Agreement and invoicing

| What | Value |
|------|-------|
| Agreement | Hosting + support, signed 2024-08-01 |
| Price | 1 200 per month — the accounting system is the source of truth |
| Invoice | Quarterly in advance, to invoice@example.com, PO number required |

## Reading map

| Task | Read | Skill |
|------|------|-------|
| Invoicing | Agreement section above | `invoice-client` |
| Deploy | Deploy routine below | |

## Deploy routine

```bash
rsync -avz --delete ./plugin/ htz_example:/var/www/example.com/wp-content/plugins/example-plugin/ --exclude='.git'
ssh htz_example 'wp --path=/var/www/example.com plugin activate example-plugin'
```

## Known quirks

- WP cron is disabled — real cron triggers `wp-cron.php` every 5 min via Plesk scheduler. Don't rely on `wp_schedule_event` returning fast results in admin.
- Custom plugin overrides `wp_mail()` — emails sent via Mailgun API, not SMTP. Verify by checking Mailgun logs, not server `mail.log`.

## Notes

- Migrated from SiteGround to Hetzner in 2024-08. Old site backups in `~/backups/example-2024-08/`.
- Client prefers email over Slack. Don't ping for non-urgent issues.

## See also

- [Deploy playbook](../playbooks/deploy.md)
