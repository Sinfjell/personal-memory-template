# Kunnskapsbank i Claude — enkel variant

For deg som vil at Claude skal kunne svare på spørsmål om kundene dine («hvordan fakturerer vi Acme?»),
uten git eller koding. Oppsett: 15 minutter.

## Velg plass

| Du … | Bruk |
|------|------|
| jobber alene og endrer sjelden innholdet | **Claude Project** (krever betalt Claude-plan) |
| er flere som redigerer, eller har alt i Notion fra før | **Notion** + Notion-koblingen i Claude |

Claude Project leser filene du laster opp, men oppdaterer dem ikke selv. Endrer du noe, laster du opp
filen på nytt. I Notion skriver Claude rett i sidene, og alle ser samme versjon.

## Oppsett i Claude Project

1. Opprett et prosjekt, f.eks. «Fakturering».
2. Lim inn teksten fra [`prosjektinstruks.md`](prosjektinstruks.md) under *Instructions*.
3. Kopier [`kunde-MAL.md`](kunde-MAL.md) én gang per kunde. Gi filen et tydelig navn: `kunde-acme.md`.
4. Fyll inn [`regler-fakturering.md`](regler-fakturering.md) med det som gjelder alle kunder.
5. Fyll inn [`00-indeks.md`](00-indeks.md) med én linje per kunde.
6. Last opp alle filene under *Project knowledge*.

## Oppsett i Notion

1. Lag en side «Kunnskapsbank» med en underside per kunde (bruk innholdet i `kunde-MAL.md`), én side for
   fellesregler og én indeksside.
2. Koble Notion til Claude under *Connectors* i innstillingene, og gi tilgang til «Kunnskapsbank».
3. Lim inn `prosjektinstruks.md` i et Claude Project, og bytt «filene» med «Notion-siden Kunnskapsbank».

## Bruk

- **Spør med kundenavn:** «Hvordan fakturerer vi Acme, og hvem sender vi til?»
- **Lær den noe:** «Husk at Acme vil ha PO-nummer på alle fakturaer.» Claude foreslår endringen i kundefilen.
  I et Project laster du så opp den oppdaterte filen. I Notion skriver Claude den rett inn.
- **Én gang i måneden:** kjør sjekken i [`vedlikehold.md`](vedlikehold.md).

## Tre regler som holder banken nyttig

1. **Én fil per kunde, ikke én fil per dato.** Det som gjelder nå, står øverst. Historikk står nederst.
2. **Oppdater med en gang du lærer noe nytt.** En utdatert bank gir feil svar med stor selvtillit.
3. **Regnskapssystemet er fasit på priser.** Banken forklarer regler og avtaler, den erstatter ikke fakturaene.
