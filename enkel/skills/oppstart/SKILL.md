---
name: oppstart
description: Bruk når kunnskapsbanken er ny eller nesten tom, eller brukeren skriver «oppstart», «kom i gang», «sett opp kunnskapsbanken», «intervju meg». Intervjuer brukeren ett spørsmål om gangen om kunder, fakturering, systemer og faste oppgaver, og lager ferdig utfylte filer (indeks, én fil per kunde, fellesregler) som brukeren laster opp i prosjektet.
---
_Versjon 1.0 · sist endret ÅÅÅÅ-MM-DD_

# Oppstartsintervju

Gjør en tom mal om til en kunnskapsbank på én gang. Du kan ikke skrive filer selv i et Claude-prosjekt,
så du lager ferdige filer brukeren kopierer inn.

## Før du starter

- Si kort hva som skjer: «Jeg stiller rundt ti korte spørsmål, ett om gangen. Si "hopp over" når du vil.»
- Be aldri om passord, API-nøkler eller kortnummer. Spør hvor noe ligger, ikke hva det er.

## Intervjuet

Ett spørsmål om gangen. Vent på svaret. Alle kan hoppes over. Stopp når brukeren sier «ferdig».

1. Hva heter du, hva er rollen din, og hva bruker du mest tid på?
2. Hvilke selskaper jobber du i eller eier?
3. Hvilke kunder er viktigst? (opptil 5: navn, hva de kjøper, kontaktperson)
4. For hver kunde fra spørsmål 3, ett om gangen: pris og intervall, hvor fakturaen skal, spesielle regler
   (PO-nummer, godkjenning, ingen faktura i juli). Si at regnskapssystemet fortsatt er fasit på pris.
5. Hva gjelder alle kunder? (betalingsfrist, fakturadato, prisjustering, purring, regnskapssystem)
6. Hvilke oppgaver gjør du hver uke eller måned på samme måte? (blir forslag til skills)
7. Hvor ligger informasjonen i dag? (Notion, Drive, e-post, gamle dokumenter)

## Lag filene

Skriv på språket brukeren svarer på. Vis planen (filnavn, én linje hver), og lag så hver fil i sin egen
kodeblokk, klar til å kopiere:

- `00-indeks.md` med én rad per kunde, etter malen i prosjektet.
- `kunde-<navn>.md` per kunde etter `kunde-MAL.md`. «Sist oppdatert» og «Sist sjekket» = i dag. Ukjent felt:
  skriv `[ukjent]`, aldri gjett. Er fakturering beskrevet: legg `fakturering` i skill-tabellen.
- `regler-fakturering.md` fra svar 5.
- `kilder-a-lese.md`: en sjekkliste over kildene fra svar 7, de mest brukte først.

## Avslutt

1. Si: «Last opp filene under Project knowledge, og slett malfilene du ikke trenger.»
2. Foreslå skills for oppgavene fra spørsmål 6 (én linje hver). Spør først etter fakta skillen trenger
   (mottaker, innhold, når) og legg dem i kundefila. `fakturering` finnes allerede.
3. Foreslå de 2-3 første kildene fra spørsmål 7 å lime inn, og si: «Når du lærer noe nytt om en kunde,
   skriv "husk at …", så foreslår jeg endringen.»

## Endringer

- 1.0 — første versjon
