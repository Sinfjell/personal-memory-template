# Deploy playbook

**Last updated:** [YYYY-MM-DD]

## Pre-deploy checklist

- [ ] Tests pass locally
- [ ] CHANGELOG updated for user-facing changes
- [ ] No debug logging left in
- [ ] Branch reviewed

## Deploy steps

1. Merge feature branch to `main` via PR
2. CI builds and runs tests
3. On green: deploy to staging
4. Smoke-test staging
5. Deploy to production
6. Post-deploy smoke test

## Rollback

[Steps to roll back if production breaks. Be specific — what command, what state to verify.]
