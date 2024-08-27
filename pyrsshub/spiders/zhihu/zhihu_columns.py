from pyrsshub.utils import fetch,zhihu_cookie
import requests
import json
import time


def parse(post):
    item = {}
    item["title"] = post["title"]
    item["description"] = post["excerpt"]
    item["link"] = post["url"]
    item["pubDate"] = time.strftime(
        "%a %b %d %H:%M:%S %z %Y", time.localtime(int(post["updated"]))
    )
    return item


def ctx(category=""):
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "cookie": zhihu_cookie,
        "referer": f"https://www.zhihu.com/column/{category}",
    }
    # https://www.zhihu.com/api/v4/columns/c_1263999612412952576/items?limit=10&offset=10
    tree = requests.get(
        f"https://www.zhihu.com/api/v4/columns/{category}/items",
        headers=default_headers,
    )
    # cont = tree.text.encode("utf-8").decode("unicode_escape")
    _dict = json.loads(tree.text)
    # print(_dict['paging'])
    # print(_dict['data'])

    return {
        "title": "知乎-" + _dict["data"][0]["author"]["name"],
        "link": f"https://www.zhihu.com/column/{category}",
        "description": _dict["data"][0]["author"]["description"],
        "author": "wld",
        "items": list(map(parse, (_dict["data"]))),
    }
