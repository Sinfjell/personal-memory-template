# Patterns

**Last updated:** [YYYY-MM-DD]

> Reusable solutions and conventions that have proved themselves on multiple projects. Add to this file when something works well twice.

## Example: WordPress plugin update via SSH

```bash
rsync -avz --delete ./plugin/ <ssh-alias>:/path/to/plugin/ --exclude='.git'
```

**Why:** Faster than zip-upload via wp-admin, doesn't trigger plugin deactivation, leaves `.git` out of the deployed copy.

**When not to use:** On Plesk shared hosting where SSH user differs from web-server user — files end up owned wrong and break wp-admin auto-update.

## (Add more patterns as you build them up)
