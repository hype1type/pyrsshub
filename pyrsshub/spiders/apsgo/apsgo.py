from pyrsshub.utils import fetch



def parse(post):
    item = {}
    item['title'] = post[0].strip()
    item['description'] = ''
    item['link'] = ''
    item['pubDate'] = '2023'
    return item




def ctx():
    default_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    tree = fetch('https://apsgo.com/auctions', headers=default_headers)
    _title = tree.css('div[class="name text-ellipsis-2"]::text').extract()
    _link = tree.css('a[class="item"]::attr(href)').extract()
    _combine = zip(_title, _link[:len(_title)])

    return {
        'title': "APSGO软购-捡漏拍卖",
        'link': 'https://apsgo.com/auctions',
        'description': '',
        'author': 'wld',
        'items': list(map(parse, _combine))
    }

