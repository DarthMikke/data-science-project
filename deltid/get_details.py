import pandas as pd
import json
from datetime import datetime
from Arbeidsplassen import stilling

FILENAME = "resultat/search_results-2022-02-02T16:24:12.csv"
# Kor mange stillingar skal hentast? Set til 0 for å hente alle.
TOTAL = 10

timestamp = datetime.utcnow().isoformat()[:-7]
hits_df = pd.read_csv(FILENAME)

print(hits_df.info())
uuids = [x for x in hits_df.head(TOTAL)['uuid']]
openings = [stilling(x) for x in uuids]
openings = [
    {
        'reference': x['reference'],
        "source": x['source'],
        "sourceurl": x['properties']['sourceurl'],
        "uuid": x['uuid'],
        "postal_code": x['locationList'][0]['postalCode'],
        'county': x['locationList'][0]['county'],
        'municipal': x['locationList'][0]['municipal'],
        "businessName": x['businessName'],
        "title": x['title'],
        "extent": x['properties']['extent'],
        "count": x['properties']['positioncount'],
        "engagementtype": x['properties']['engagementtype'],
    } for x in openings
]

openings = pd.read_json(json.dumps(openings), orient='records')
print(openings.info())
openings.to_csv('resultat/detailed-{}.csv'.format(timestamp))
