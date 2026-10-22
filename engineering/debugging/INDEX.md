# Debugging — index

**last_updated:** YYYY-MM-DD

> One file per topic, one line per file here, with the symptoms someone would search for.
> Never grow one big debugging file: past ~40 KB nobody (human or agent) finds anything in it.

| Topic | Symptoms / keywords | File |
|-------|---------------------|------|
| WordPress | white screen, plugin conflict, cron not running, mail not sent | [`wordpress.md`](wordpress.md) |

## Entry format (in the topic file)

```markdown
## [Short bug title]

**Symptom:** What you observed.
**Root cause:** What was actually wrong.
**Fix:** What worked.
**Detect fast:** A command or log pattern that reveals it.
<!-- Source: <ticket>, YYYY-MM-DD -->
```

Write it down when a bug took more than an hour. One-off incidents that taught nothing reusable belong in the
client's changelog, not here.
