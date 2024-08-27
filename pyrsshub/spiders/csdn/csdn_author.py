import feedparser

def parse(post):
    item = {}
    item['title'] = post['title']
    item['description'] = post['summary']
    item['link'] = post['link']
    item['pubDate'] = post['published']
    return item



# https://blog.csdn.net/m0_64336780?type=blog
def ctx(category=''):
    tree = feedparser.parse(f'https://blog.csdn.net/{category}/rss/list')
    return {
        'title': 'CSDN-' + category + '-作者文章',
        'link': f'https://blog.csdn.net/{category}',
        'description': '',
        'author': 'wld',
        'items': list(map(parse, tree.entries))
    }
