# [Client Name] — Client Memory

**Owner:** [You]
**Last updated:** [YYYY-MM-DD]
**Last verified:** [YYYY-MM-DD]

## Overview

- **Website:** https://example.com
- **Primary contact:** [Name] — [email]
- **Hosting:** [Kinsta / Hetzner / Vercel / other]
- **SSH alias:** `[alias]` / n/a
- **CMS / stack:** [WordPress / Next.js / other]
- **Repos:** `~/repositories/<repo-name>`
- **Task tracker entity:** [link or ID] / n/a

## Systems and access

| System | URL / host | Access via |
|--------|-----------|-----------|
| Admin panel | https://example.com/admin | 1Password: `[item-name]` |
| Hosting panel | | 1Password: `[item-name]` |
| SSH | | SSH alias: `[alias]` |
| DNS | | 1Password: `[item-name]` |

## Deploy routine

```bash
# Example:
rsync -avz --delete ./plugin/ alias:/path/to/wp-content/plugins/plugin/ --exclude='.git'
```

## Known quirks

<!-- Bugs, workarounds, race conditions, cache problems, etc. -->

## Notes

<!-- History, decisions, special considerations -->

## See also

- [Related file 1](../engineering/patterns.md)
