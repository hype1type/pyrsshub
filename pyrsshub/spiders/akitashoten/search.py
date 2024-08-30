from pyrsshub.utils import fetch


def parse(post):
    item = {}
    item["title"] = post.css('div[class="bookInfo"]').css('h2::text').extract_first()
    item["description"] = ''
    item["link"] = 'https://www.akitashoten.co.jp'+post.css('a::attr(href)').extract_first()
    item["author"] = post.css('div[class="bookInfo"]').css('span[class="authorName"]::text').extract_first()
    item["pubDate"] = post.css('div[class="bookInfo"]').css('span[class="date"]::text').extract_first()[4:]
    return item


def ctx(query=''):
    # from urllib.parse import quote
    # query = quote(query, encoding="GBK")
    web_site = f"https://www.akitashoten.co.jp/comics/search"
    p_query = {
    "q": f"{query}"
}
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "referer": web_site,
    }

    tree = fetch(web_site, headers=default_headers,para_query=p_query)
    _title = [f'{query}-搜索结果']
    _link = web_site
    _items = tree.css('div[class="book"]')
    # print(_items)

    return {
        "title": "秋田书店-" + _title[0],
        "link": _link,
        "description": '',
        "author": "wld",
        "items": list(map(parse, _items)),
    }

