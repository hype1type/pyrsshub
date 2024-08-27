from pyrsshub.utils import fetch




def parse(post):
    item = {}
    item['title'] = post[0]
    item['description'] = post[2]
    item['link'] = post[1]
    item['pubDate'] = ''
    return item




def ctx(category='', category2=''):
    default_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    tree = fetch(f'https://blog.csdn.net/nav/{category}/{category2}', headers=default_headers)
    _title = tree.css('span[class="blog-text"]::text').extract()
    _link = tree.css('a[class="blog"]::attr(href)').extract()
    _desc = tree.css('p[class="desc"]::text').extract()
    
    # print(_title)
    # print(_link)
    # print(_desc)
    _combine = zip(_title, _link, _desc)
    
    return {
        'title': 'CSDN-' + category + '-' + category2,
        'link': f'https://blog.csdn.net/nav/{category}/{category2}',
        'description': '',
        'author': 'wld',
        'items': list(map(parse, _combine))
    }

