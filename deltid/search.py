import pandas as pd
import json
from datetime import datetime
from Arbeidsplassen import sok


# Kor mange stillingar skal hentast? Set til 0 for å hente alle.
TOTAL = 0

search_query = {
    'occupationFirstLevels[]': 'Helse%20og%20sosial',
    'occupationSecondLevels[]': 'Helse%20og%20sosial.Helse',
    'size': '50'
}

timestamp = datetime.utcnow().isoformat()[:-7]
fetched = -1
all_hits = []

# resolved = pd.read_csv('resolved.csv')
while fetched < TOTAL:
    if fetched > 0:
        search_query['from'] = fetched

    response = sok(search_query)

    if TOTAL == 0:
        TOTAL = response['hits']['total']['value']

    hits = [x['_source'] for x in response['hits']['hits']]

    hits = [
        {
            'reference': x['reference'],
            'county': x['locationList'][0]['county'],
            'municipal': x['locationList'][0]['municipal'],
            "postal_code": x['locationList'][0]['postalCode'],
            "businessName": x['businessName'],
            "source": x['source'],
            "title": x['title'],
            "uuid": x['uuid']
        } for x in hits
    ]

    all_hits += hits
    fetched += len(hits)

hits_df = pd.read_json(json.dumps(all_hits), orient='records')
print(hits_df.info())
print(hits_df[:10]['uuid'])
hits_df.to_csv('resultat/search_results-{}.csv'.format(timestamp))
