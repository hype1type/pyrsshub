import re
import requests
from pyrsshub.utils import default_headers

domain = 'https://dig.chouti.com'


def parse(post):
    item = {}
    item['title'] = re.sub(r'<[^>]*>', '', post['title']).strip()
    item['description'] = post['title']
    item['link'] = 'https://dig.chouti.com/link/' + str(post['id'])
    item['pubDate'] = str(post['created_time'])[0:10]
    item['author'] = post['submitted_user']['nick']
    return item 


def ctx(category=''):
    default_headers.update({'Referer': domain})
    r_url = f'{domain}/search/show'
    post_data = {'words':category,'searchType':'2','linkType':'ALL', 'subjectId':'-1'}
    posts = requests.post(r_url, data=post_data, headers=default_headers).json()['data']['linksList']
    return {
        'title': f'{category} - 抽屉热榜',
        'link': r_url,
        'description': f'抽屉热榜 - {r_url}',
        'author': 'hillerliao',
        'items': list(map(parse, posts))
    }
