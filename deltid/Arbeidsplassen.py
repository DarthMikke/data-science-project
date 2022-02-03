import json
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, urlunsplit


class URL:
    def __init__(self, url):
        self.scheme, self.netloc, self.path, query, self.fragment = urlsplit(url)
        self.query = {x[:x.find("=")]: x[x.find("=")+1:] for x in query.split("&")}

    def __str__(self):
        query = "&".join([f"{x}={y}" for (x, y) in self.query.items()])
        return urlunsplit((self.scheme, self.netloc, self.path, query, self.fragment))


def make_request(url, headers={}):
    headers["User-Agent"] = "Prosjekt ism. jobbsøknad. Kontakt mwarecki1@gmail.com."
    return Request(url, headers=headers)


def get_json(url):
    request = make_request(str(url))
    print(str(url))
    with urlopen(request) as fh:
        response = fh.read()
        response = json.loads(response)

    return response


def stilling(uuid):
    url = URL("https://arbeidsplassen.nav.no/stillinger/api/stilling/{uuid}".format(uuid=uuid))
    return get_json(url)


def sok(query):
    url = URL("https://arbeidsplassen.nav.no/stillinger/api/search")
    url.query = query
    return get_json(url)
