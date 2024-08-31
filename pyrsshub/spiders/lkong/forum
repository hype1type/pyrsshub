import json
from pyrsshub.utils import fetch,lkongcookie

import datetime

def parse(post):
    item = {}
    item["title"] = post['title']
    item["description"] = ''
    item["link"] = 'https://www.lkong.com/thread/' + str(post['tid'])
    item["author"] = post['author']['name']
    timestamp = str(post['dateline'])[:-3]
    date = datetime.datetime.fromtimestamp(int(timestamp))
    formatted_date = date.strftime('%Y-%m-%d')
    item["pubDate"] = formatted_date
    return item


def ctx(category=""):
    web_site = f"https://www.lkong.com/forum/{category}"
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "cookie": lkongcookie,
        "referer": web_site,
    }

    tree = fetch(web_site, headers=default_headers)
    _link = web_site
    _items = tree.css('script[id="__NEXT_DATA__"]::text').extract_first()
    _items = json.loads(_items)
    _title = _items['props']['pageProps']['source']['forum']['name']
    _items = _items['props']['pageProps']['threads']

    return {
        "title": _title,
        "link": _link,
        "description": '',
        "author": "wld",
        "items": list(map(parse, _items)),
    }
