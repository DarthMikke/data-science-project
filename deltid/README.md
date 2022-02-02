# Deltidsprosjektet
## Prosjektbeskriving
Heiltidskultur er viktig for Fagforbundet. Dersom det vil
finnast kvantitative data om mangelen på heiltidskultur i
helsesektoren, vil det kunne vera lettare å utøve trykk på
politiske organ som kan setje heiltidskulturen i praksis.

Hovudformålet for dette prosjektet er å samle kvantitative data
om kva slags stillingar blir utlyst i helsesektoren med tanke på
antall stillingar per utlysing og stillingsbrøk. Beste scenario
er å analysere alle stillingar utlyst gjennom NAV Arbeidsplassen.
Dersom det ikkje er nok tid, skal eit tilfeldig utval av 
stillingane analyserast.

## Metode
Programmet lastar ned API-data frå Arbeidsplassen og lagar ein 
tabell ved hjelp av `pandas` som med ei samanstilling av 
utlysingane. Det skal samlast data etter fylke, kommune,
stillingsbrøk og talet på utlyste stillingar. Det skal så
genererast grafar i `matplotlib` som kan framstille data på ein
måte som er lett å forstå for tillitsvalte, andre medlemar og
politiske organ Fagforbundet skal påverke.

## API-beskriving
Programmet brukt til å lage rapporten tar i bruk NAVs ikkje-
offentlege API. Dei er beskrive i
[API-beskriving](API-beskriving.md).

## Rapport
Bilete til rapporten er tilgjengelege i mappa
[resultat](resultat).
