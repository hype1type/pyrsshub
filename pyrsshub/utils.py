import json
import re
from flask import Response
import requests
from parsel import Selector

default_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

zhihu_cookie = ''
qm_cookie = ''

class XMLResponse(Response):
    def __init__(self, response, **kwargs):
        if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
            if response.startswith('<?xml'):
                kwargs['mimetype'] = 'application/xml'
        return super().__init__(response, **kwargs)


def fetch(url: str, headers: dict = default_headers, proxies: dict = None,para_query: dict = None):
    try:
        res = requests.get(url, headers=headers, proxies=proxies,data=json.dumps(para_query))
        res.raise_for_status()
    except Exception as e:
        print(f'[Err] {e}')
    else:
        html = res.text
        tree = Selector(text=html)
        return tree


def filter_content(items):
    content = []
    p1 = re.compile(r'(.*)(to|will|date|schedule) (.*)results', re.IGNORECASE)
    p2 = re.compile(r'(.*)(schedule|schedules|announce|to) (.*)call', re.IGNORECASE)
    p3 = re.compile(r'(.*)release (.*)date', re.IGNORECASE)

    for item in items:
        title = item['title']
        if p1.match(title) or p2.match(title) or p3.match(title):
            content.append(item)
    return content


def send_email(ctx, _filter:bool):
    from email.header import Header
    from email.utils import parseaddr,formataddr
    from email.mime.text import MIMEText
    import smtplib

    if _filter:
        INFO_dict = [f"<a href='{i[1]}'>{i[2]}</a><br>" for i in filter(ctx)]
    else:
        INFO_dict = [f"<a href='{i['link']}'>{i['title']}</a><br>" for i in ctx["items"]]
    mail_msg:str = ''.join(INFO_dict)
    subject:str = ctx["title"]
    if mail_msg.strip()=='':
        pass
    else:
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = ''  # 用户名
        mail_pass = ''  # 口令
        sender = ''
        receivers = ['username@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(mail_msg, 'html', 'utf-8')
        def format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))
        message['From'] = format_addr('%s<%s>' % ('从来不会胖', sender))
        message['To'] = Header("USER", 'utf-8')
        subject = subject
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            print(e)


def send_ding(ctx, _filter:bool):
    import requests,json
    headers={"Content-Type": "application/json","Charset": "UTF-8"}
    if _filter:
        text = ''.join([f"[{i[2]}]({i[1]})<br><br>" for i in filter(ctx)])
    else:
        text = ''.join([f"[{i[2]}]({i[1]})<br><br>" for i in ctx])
    if text.strip()=='':
        pass
    else:
        webhook = ''
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title":"test",
                "text": ctx["title"] + "<br>" + text
            }
        }
        requests.post(webhook, data=json.dumps(data), headers=headers)


def filter(_dict:dict)-> tuple:
    import sqlite3
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM source')
    row = cur.fetchall()
    data = [(_dict['title'],i['link'],i['title']) for i in _dict["items"]]
    jiao = set(row)&set(data)
    _filter = set(data)^jiao
    cur.executemany('INSERT INTO source VALUES (?,?,?)', _filter)
    conn.commit()
    cur.close()
    conn.close()
    return _filter