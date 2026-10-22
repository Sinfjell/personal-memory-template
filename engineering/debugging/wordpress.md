# Debugging — WordPress

**last_updated:** YYYY-MM-DD · **last_verified:** YYYY-MM-DD

## WP cron never fires on low-traffic sites

**Symptom:** Scheduled posts and plugin jobs run hours late or never.
**Root cause:** WP cron only runs on page loads; with `DISABLE_WP_CRON` set and no real cron, nothing triggers it.
**Fix:** Add a server cron calling `wp cron event run --due-now` every 5 minutes.
**Detect fast:** `wp cron event list` shows events with a "next run" in the past.
