import re
import json
from typing import Any
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as Soup
from datetime import datetime


handles = ["fagforbundet", "sykepleierforbundet", "delta.i.ys"]
full_names = {
    "fagforbundet": "Fagforbundet",
    "sykepleierforbundet": "Norsk sykepleierforbund",
    "delta.i.ys": "Delta"
}
like = re.compile("([0-9]+) likar")
engagement = re.compile("([0-9]+) snakkar")

if __name__ == "__main__":

    urls = [(x, f'https://www.facebook.com/{x}') for x in handles]
    urls += [(x, f'https://m.facebook.com/{x}') for x in handles]

    sites: [str, Any] = {}

    for (handle, url) in urls:
        request = Request(url, headers={'Accept-Language': 'nn-NO'})
        with urlopen(request) as fh:
            html = fh.read()
            soup = Soup(html, "lxml")

        if handle not in sites.keys():
            content = [y['content'] for y in [x for x in soup.find_all('meta') if x.has_attr('name')] if y['name'] == "description"][0]
            content = content.replace('\xa0', '')
            likes = like.findall(content)
            engagements = engagement.findall(content)

            if len(likes) == 0 or len(engagements) == 0:
                continue

            sites[handle] = {
                'handle': handle,
                'verbose': full_names[handle],
                'page_likes': likes[0],
                'engagement': engagements[0]
            }

    result = {
        'date': datetime.now().isoformat(),
        'sites': list(sites.values())
    }
    print(json.dumps(result, indent=2))
