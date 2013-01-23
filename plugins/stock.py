'''
改自wiki查询插件, 用了hexun.com的接口, 尚未测试
'''

# 实时股票查询从hexun.com

import urllib2
import urllib
import re

def test(data, bot=None):
    return '股' in data['message']

def handle(data, bot=None):
    m = re.search('(?<=股)(票?)([0-9].{6}?)(?=行情|\?|\s|\Z)', data['message'])
    if m and m.groups():
        return stock(m.groups()[0])
    raise Exception

def remove(s):
    ans = ''
    while True:
        i = s.find('<')
        if i < 0:
            ans += s
            break
        ans += s[:i]
        s = s[i+1:]
        s = s[s.find('>')+1:]
    s = ans
    ans = ''
    while True:
        i = s.find('[')
        if i < 0:
            ans += s
            return ans
        ans += s[:i]
        s = s[i+1:]
        s = s[s.find(']')+1:]


def stock(title):
    url = 'http://bdcjhq.haexun.com/quote?s2=' + title + '.sh'
    req = urllib2.Request(url, headers={'User-Agent': "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3"})
    wp = urllib2.urlopen(req, timeout=10)
    html = wp.read()
    #防止404，实际上似乎py会直接在urlopen的时候发现404并抛异常
    i = html.find('.sh')
    if i < 0:
        raise Exception
    html = html[i:]
    html = html[html.find('try{parent.bdcallback({"000001.sh":'):html.find('},"tofnow"')]
    return remove(html)


if __name__ == '__main__':
    for data in [ {'message': '什么是SVM  ????'}, {'message': '什么是薛定谔方程啊'} ]:
        if test(data):
            print handle(data)
