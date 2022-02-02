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

## Stilling
### Førespurnad
URL: `https://arbeidsplassen.nav.no/stillinger/api/stilling/<uuid>`

Path-argument:
`uuid` er id-en til stillinga.

### Resultat
#### 200 OK
Dersom stillinga er utlyst gjennom Arbeidsplassen.

#### xxx
Dersom stillinga er utlyst gjennom ein tredjepart.
