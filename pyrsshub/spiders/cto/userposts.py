import sys


sys.path.append("G:/mypython_example/pyrsshub-master")

from pyrsshub.utils import fetch
import time



def parse(post):
    item = {}
    item['title'] = post[0]
    item['description'] = ''
    item['link'] = post[1]
    item['pubDate'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return item




def ctx(category=''):
    # tree = fetch(f"https://icv.51cto.com/user/posts/11867250")
    tree = fetch(f"https://icv.51cto.com/user/posts/{category}")
    public_mtabs_item = tree.css('div[class="public-mtabs-item"]')
    name = tree.css('div[class="name"]').css('a::text').extract()[0].strip()
    title_list = []
    link_list = []

    for i in public_mtabs_item:
        try:
            title = i.css('a::text').extract()[0]
            link  = 'https://icv.51cto.com' + i.css('a::attr(href)').extract()[0]
            title_list.append(title)
            link_list.append(link)
        except Exception as e:
            continue
    news = zip(title_list,link_list)

    
    return {
        'title': f'汽开社区-博主{name}',
        'link': 'https://icv.51cto.com/',
        'description': '',
        'author': 'wld',
        'items': list(map(parse, news))
    }
# print(ctx('11867250'))