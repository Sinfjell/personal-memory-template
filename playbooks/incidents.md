# Incident response

**Last updated:** [YYYY-MM-DD]

## Severity levels

- **P1** — Customer-facing service is down. All hands on deck.
- **P2** — Major feature broken, workaround exists. Fix within the day.
- **P3** — Minor issue. Fix in next sprint.

## Response steps

1. **Acknowledge** — confirm the incident in the appropriate channel
2. **Assess severity** — P1 / P2 / P3
3. **Stabilize** — restore service first, even with a hack. Root-cause later.
4. **Communicate** — let affected users know what's happening and when to expect a fix
5. **Resolve** — implement the real fix
6. **Postmortem** — for P1/P2: write up what happened, why, and what changes prevent it. Save in `projects/<incident-slug>/`.

## On-call contacts

| Role | Person | Contact |
|------|--------|---------|
| Hosting escalation | | |
| Domain / DNS | | |
| Payment provider | | |
