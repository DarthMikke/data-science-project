import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def convert_to_percentage(string):
    string = str(string).strip()
    if string[-1] == "%":
        string = string[:-1]
    try:
        return int(string.strip())
    except:
        return None


FILENAME = 'resultat/detailed-2022-02-03T07:20:43.csv'
df = pd.read_csv(FILENAME)

timestamp = datetime.now().isoformat()[:-7]
PATHBASE = f'rapportar/{datetime.now().isoformat()[:-7]}/'
if not os.path.isdir(PATHBASE):
    os.mkdir(PATHBASE)

df['calculated'] = df['jobpercentage'].apply(convert_to_percentage)

# # Heiltid vs. deltid
# ## Noreg åleine
noreg = df.groupby('extent').size().plot.pie(y='extent', xlabel='', ylabel='')
noreg.set_title("Noreg")
noreg.legend()
fig = noreg.get_figure()
fig.suptitle("Stillingsbrøk i utlysingar")
fig.savefig(f"{PATHBASE}/fig3.png", dpi=400)
fig.clf()

# ## Noreg vs fylka
counties = list(df.groupby('county').size().axes[0])
extents = list(df.groupby('extent').size().axes[0])
for county in counties:
    print(county)
    fig, axs = plt.subplots(1, 2)
    axs[0].pie(df.groupby('extent').size(), labels=extents)
    axs[0].set_title("NOREG")
    axs[0].legend()
    axs[1].pie(df.query(f'county == "{county}"').groupby('extent').size())
    axs[1].set_title(county)
    fig.suptitle("Stillingsbrøk i utlysingar i helsesektoren")
    fig.savefig(f"{PATHBASE}/fig-{county}.png", dpi=400)
    fig.clf()

# ## Alle fylka på éin graf
fig, axs = plt.subplots()

grouped = pd.DataFrame(
    df.groupby(['county', 'extent']).size()
        .reset_index().rename(columns={0: 'count'})
)
grouped['Heltid'] = (grouped['extent'] == "Heltid")*grouped['count']
grouped['Deltid'] = (grouped['extent'] == "Deltid")*grouped['count']
shift = -1 if grouped['Heltid'][0] == 0 else 1
grouped['Heltid_s'] = grouped['Heltid'].shift(shift)
grouped = grouped.query("Deltid != 0 and Heltid_s != 0").set_index('county')
grouped = grouped.drop(columns='Heltid').rename(columns={'Heltid_s': 'Heltid'})
grouped = grouped.sort_values('Deltid')

heiltid = grouped['Heltid']
deltid = grouped['Deltid']
axs.barh(counties, heiltid, label='Heiltid')
axs.barh(counties, deltid, label='Deltid')
axs.legend()
print(axs.get_position())
axs.set_position([0.3, 0.11, 0.65, 0.77])
fig.suptitle("Heiltidsdel i stillingsutlysingar i helsesektoren")
fig.savefig(f"{PATHBASE}/fig4.png", dpi=400)
fig.clf()

# ## Scatter
sdf = df[['uuid', 'count', 'calculated']].dropna()
fig = sdf.plot.scatter(x='calculated', y='count').get_figure()
fig.savefig(f"{PATHBASE}/fig5.png", dpi=400)
