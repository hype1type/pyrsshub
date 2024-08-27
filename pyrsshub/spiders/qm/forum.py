from pyrsshub.utils import fetch,qm_cookie

def parse(post):
    item = {}
    if post.css('th[class="common"]').css('a[class="s xst"]::text').extract_first() is None:
        item["title"] = post.css('th[class="new"]').css('a[class="s xst"]::text').extract_first()
    else:
        item["title"] = post.css('th[class="common"]').css('a[class="s xst"]::text').extract_first()
    item["description"] = ''
    if post.css('th[class="common"]').css('a[class="s xst"]::attr(href)').extract_first() is None:
        item["link"] = post.css('th[class="new"]').css('a[class="s xst"]::attr(href)').extract_first()
    else:
        item["link"] = post.css('th[class="common"]').css('a[class="s xst"]::attr(href)').extract_first()
    item["author"] = post.css('td[class="by"]').css('cite').css('a[c="1"]::text').extract_first()
    item["pubDate"] = post.css('td[class="by"]').css('em').css('::text').extract_first()
    return item


def ctx(category=""):
    web_site = f"http://www.1000qm.vip/forum.php?mod=forumdisplay&fid={category}"
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "cookie": qm_cookie,
        "referer": web_site,
    }

    tree = fetch(web_site, headers=default_headers)
    _title = tree.css('h1[class="xs2"]').css('a::text').extract()
    _link = web_site
    _items = tree.css('tbody')

    return {
        "title": "阡陌居" + _title[0],
        "link": _link,
        "description": '',
        "author": "wld",
        "items": list(map(parse, _items)),
    }
