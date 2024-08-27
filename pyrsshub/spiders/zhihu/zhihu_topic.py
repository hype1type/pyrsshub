from pyrsshub.utils import fetch,zhihu_cookie


def parse(post):
    item = {}
    item["title"] = post[0].extract()
    item["description"] = post[0].extract()
    item["link"] = "https:" + post[1].extract()
    item["pubDate"] = "2023"
    return item


def ctx(category=""):
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "cookie": zhihu_cookie,
        "referer": f"https://www.zhihu.com/topic/{category}/hot",
    }

    tree = fetch(f"https://www.zhihu.com/topic/{category}/hot", headers=default_headers)
    _title = tree.css('a[data-za-detail-view-element_name="Title"]::text')
    _href = tree.css('a[data-za-detail-view-element_name="Title"]::attr(href)')
    # print(_title,_href)
    _combine = zip(_title, _href)
    _link = tree.css('a[class="Tabs-link is-active"]::attr(href)').extract()
    _title = tree.css('div[class="TopicMetaCard-title"]::text').extract()

    return {
        "title": "知乎-" + _title[0],
        "link": "https://www.zhihu.com" + _link[0],
        "description": tree.css('div[class="TopicMetaCard-title"]::text').extract(),
        "author": "wld",
        "items": list(map(parse, _combine)),
    }
