# AI use policy

**Last updated:** [YYYY-MM-DD]

## What I share with LLMs

✅ **OK to share:**
- Code from this repo
- Public client info (website URL, public docs)
- Anonymized data (test fixtures, structure descriptions)
- General architecture and stack details

❌ **Never share:**
- Production secrets (API keys, DB passwords, OAuth tokens)
- Customer PII (names + emails + financial data combined)
- Anything covered by NDA without checking the NDA terms first
- Private keys, certificates, `.env` files

## Tools I use

| Tool | Purpose | Notes |
|------|---------|-------|
| Claude Code | Coding agent | Reads this repo as long-term memory |
| ChatGPT | Quick questions | Browser only, no integrations |

## Data retention

- Local LLM clients (Claude Code, Cursor) read files but don't store them externally beyond the API request
- Web LLM clients may retain conversation history per their terms — check before pasting sensitive info
