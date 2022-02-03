# Arbeidsplassen-API

NAV Arbeidsplassen bruker 2 endepunkt for API-ar:
- søkeendepunkt
- utlysingsendepunkt.

## Søk
### Førespurnad
URL: `https://arbeidsplassen.nav.no/stillinger/api/search`

Query-argument:
```
occupationFirstLevels[]=Helse%20og%20sosial
occupationSecondLevels[]=Helse%20og%20sosial.Helse
size=50
from=<int:from>
```

`from` er talet på utlysingar som klienten allereie har fått og
tenaren kan hoppe over.

### Svar
Returnerer eit objekt med talet på utlysingar som svarar til søket
(`.hits.total.value`), og sjølve lista over utlysingane
(`.hits.hits._source`).

Lista inneheld objekt med m.a. parameter:
- `reference`: referansenummeret for utlysinga,
- `locationList`: liste med lokasjonar for stillinga(ne), kvart objekt 
inneheld følgjande parameter av interesse:
  - `county`: fylke,
  - `municipal`: kommune,
  - `postalCode`: postnummer.
- `businessName`: namnet på eininga,
- `source`: `SOURCEAPI` om utlysinga er hosta hos Arbeidsplassen, eller
namnet på tenesta som hostar utlysinga, t.d. `FINN`, `AMEDIA`, `POLARIS`.
`Stillingsregistrering` var berre brukt 1 gong.
- `title`: Stillingstittel,
- `uuid`: UUID brukt til å hente utlysinga gjennom API.

Objekta beskrive her kan òg innehalde andre parameter, men dei er
ikkje nødvendige for dette prosjektet.

## Stilling
### Førespurnad
URL: `https://arbeidsplassen.nav.no/stillinger/api/stilling/<uuid>`

Path-argument:
`uuid` er id-en til stillingsutlysinga.

### Resultat
#### 200 OK
Dersom stillinga er utlyst gjennom Arbeidsplassen.


#### xxx
Dersom stillinga er utlyst gjennom ein tredjepart.
