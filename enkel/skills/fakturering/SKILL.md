---
name: fakturering
description: Bruk når brukeren ber om fakturagrunnlag, vil vite hva en kunde skal faktureres, eller skriver «fakturer Acme», «hva sender vi Acme i år». Leser kundefila og fellesreglene i kunnskapsbanken og lager et utkast til fakturalinjer. Sender aldri faktura.
---
_Versjon 1.0 · sist endret ÅÅÅÅ-MM-DD_

# Fakturagrunnlag

Kundefila eier fakta (pris, intervall, mottaker, spesialregler). Denne skillen eier fremgangsmåten.
Er de uenige, vinner kundefila, og du sier fra.

## Slik gjør du det

1. **Finn kunden** i `00-indeks.md` og les kundefila. Finnes den ikke: si det og stopp.
2. **Les Fakturering-tabellen** og `regler-fakturering.md`. Kundens egne regler vinner over fellesreglene.
3. **Sjekk alderen.** Er «Sist sjekket» eldre enn 6 måneder, si at prisen bør sjekkes mot regnskapssystemet.
4. **Lag utkastet:** periode, beskrivelse, antall, pris, referanse (PO-nummer hvis kunden krever det).
5. **Vis utkastet** og hvilke regler du brukte. Brukeren sender fakturaen selv.
6. **Lærte vi noe nytt?** Foreslå endringen i kundefila, klar til å lime inn.

## Endringer

<!-- Øk versjonen når du endrer skillen: 1.0 → 1.1 for små endringer, 2.0 når den gjør noe nytt. -->
- 1.0 — første versjon
