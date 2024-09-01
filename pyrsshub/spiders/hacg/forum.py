
from pyrsshub.utils import fetch

def parse(post):
    item = {}
    item["title"] = post.css('h2[class="item-heading"]').css('a::text').extract_first()
    item["description"] = post.css('div[class="item-excerpt muted-color text-ellipsis mb6"]').css('::text').extract_first()
    item["link"] = post.css('div[class="item-thumbnail"]').css('a::attr(href)').extract_first()
    item["author"] = post.css('item[class="meta-author flex ac"]').css('span[class="hide-sm ml6"]').css('::text').extract_first()
    item["pubDate"] = post.css('span[class="icon-circle"]::text').extract_first()
    # item["pubDate"] = post.css('span[class="icon-circle"]::attr(title)').extract_first()
    return item


def ctx(forum):
    web_site = f"https://www.hhacg.cc/{forum}"
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "referer": web_site,
    }
    tree = fetch(web_site, headers=default_headers)
    _title = [f'{forum}']
    _link = web_site
    _items = tree.css('posts[class="posts-item list ajax-item flex"]')

    return {
        "title": "HACG-" + _title[0],
        "link": _link,
        "description": '',
        "author": "wld",
        "items": list(map(parse, _items)),
    }

