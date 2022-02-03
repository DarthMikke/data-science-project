import pandas as pd
import json
from datetime import datetime
import Arbeidsplassen

FILENAME = "resultat/search_results-2022-02-02T18:37:15.csv"
# Kor mange stillingar skal hentast? Set til 0 for å hente alle.
TOTAL = 0

timestamp = datetime.utcnow().isoformat()[:-7]
hits_df = pd.read_csv(FILENAME)

print(hits_df.info())
uuids = hits_df.head(TOTAL)['uuid'] if 0 < TOTAL < len(hits_df) else hits_df['uuid']
columns = ['reference', 'source', 'sourceurl', 'uuid', 'postal_code', 'county', 'municipal',
           'businessName', 'title', 'extent', 'count', 'engagementtype']
openings = pd.DataFrame([], columns=columns)

total = len(uuids)
for i in range(total):
    x = uuids[i]
    print(f"Hentar {i}/{total}: {x}.")
    try:
        stilling = Arbeidsplassen.stilling(x)['_source']
        new_row = {
            'reference': stilling['reference'],
            "source": stilling['source'],
            "uuid": x,
            "postal_code": stilling['locationList'][0]['postalCode'],
            'county': stilling['locationList'][0]['county'],
            'municipal': stilling['locationList'][0]['municipal'],
            "businessName": stilling['businessName'],
            "title": stilling['title'],
            "extent": stilling['properties']['extent']
                if 'extent' in stilling['properties'].keys()
                else None,
            "count": stilling['properties']['positioncount']
                if 'positioncount' in stilling['properties'].keys()
                else None,
            "engagementtype": stilling['properties']['engagementtype']
                if 'engagementtype' in stilling['properties'].keys()
                else None,
            'sourceurl': stilling['properties']['sourceurl']
                if 'sourceurl' in stilling['properties'].keys()
                else None,
            'jobpercentage': stilling['properties']['jobpercentage']
                if 'jobpercentage' in stilling['properties'].keys()
                else None,
        }
    except Exception as e:
        with open("details.log", "a") as fh:
            fh.write(f"\n{e}")

    openings = openings.append(new_row, ignore_index=True)

print(openings.info())
NEW_FILENAME = 'resultat/detailed-{}.csv'.format(timestamp)
openings.to_csv(NEW_FILENAME)
print(f"Lagra resultatet i {NEW_FILENAME}")
