---
name: invoice-client
description: Use when the user asks to invoice a client, prepare invoice lines, or check what to bill ("invoice Acme", "what do we bill Example Client this quarter"). Reads the client's agreement section and drafts invoice lines for the user to approve. Never sends an invoice.
---
_Version 0.1.0 · source: skills/invoice-client/SKILL.md_

# Invoice a client

The client file owns the facts (price, interval, recipient, special rules). This skill owns the steps.
If the two disagree, the client file wins — and say so.

## Steps

0. **Find the knowledge base** the same way as `ingest` step 0, and read files relative to it.
1. **Find the client.** Read `MEMORY.md`, then `clients/<slug>.md`. No file → stop and say so.
2. **Read the agreement section** (`## Agreement and invoicing`). Note price, interval, recipient and
   special rules. A `last_verified` older than ~4 months → warn that the price may be stale.
3. **Check the source of truth.** The accounting system holds the real price. If you can read it,
   compare; if they differ, show both and do not pick one.
4. **Draft the lines:** period, description, quantity, unit price, reference (PO number if required).
5. **Show the draft** and the rules you applied. The user sends the invoice, never you.
6. **Learned something new** (a new rule, a changed price)? Offer to update the client file.
