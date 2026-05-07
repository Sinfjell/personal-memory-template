# Security policy

**Last updated:** [YYYY-MM-DD]

## Secrets

- All passwords and API keys live in **1Password** (or your password manager of choice)
- Reference 1Password items by name in this repo — never paste actual values
- `.env` files: gitignored, synced separately via password manager attachments

## SSH

- Use SSH config aliases (`~/.ssh/config`) — never paste IPs and users into commands
- Keys are passphrase-protected and stored in the OS keychain
- Production SSH access requires explicit user approval before any destructive command

## Access reviews

- Quarterly: review who has access to which systems
- After leaving roles or projects: rotate keys/passwords for affected systems

## Backup

- Backups happen on the hosting layer (Kinsta / Plesk daily snapshots)
- Local development backups: Time Machine + cloud sync
- Critical client data is backed up to a separate provider — no single-vendor lock-in
