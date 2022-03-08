import requests
from pyrsshub.utils import default_headers

domain = 'https://dig.chouti.com'


def parse(post):
    item = {}
    item['title'] = post['title']
    item['description'] = f"[{post['sectionName']}] {item['title']} "
    item['link'] = 'https://dig.chouti.com/link/' + str(post['id'])
    item['pubDate'] = str(post['created_time'])[0:10]
    item['author'] = post['submitted_user']['nick']
    return item 


def ctx(category=''):
    default_headers.update({'Referer': domain})
    post_data = {'sectionId':category}
    r_url = f'{domain}/section/links'
    posts = requests.post(r_url, data=post_data, headers=default_headers).json()['data']
    return {
        'title': f'{category} - 抽屉热榜',
        'link': r_url,
        'description': f'抽屉热榜 - {r_url}',
        'author': 'hillerliao',
        'items': list(map(parse, posts))
    }