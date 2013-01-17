#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
Copyright (c) 2013 Qimin Huang <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# 笑话、小知识、故事
import requests


kw = ['讲笑话', '讲个笑话', '讲故事', '讲个故事', '小知识']


def test(data, bot):
    msg = data['message']
    for i in kw:
        if i in msg:
            return True
    return False


def analyseResponse(msg, first):
    return msg.split(first.decode('utf8'))[1].split('<br><font'.decode('utf8'))[0].encode('utf8')


def getResponse(kwid, appid):
    url = 'http://www.unidust.cn/search.do?type=web&appid='
    msg = requests.post(url + appid).text
    try:
        return analyseResponse(msg, '</font><br>')
    except:
        if 1 == kwid:
            return analyseResponse(msg, '可看笑话分类<br>')
        if 3 == kwid:
            return analyseResponse(msg, '<br></font>')


def handle(data, bot):
    msg = data['message']
    try:
        if '讲笑话' in msg or '讲个笑话' in msg:
            return getResponse(1, '61')
        elif '讲故事' in msg or '讲个故事' in msg:
            return getResponse(2, '381')
        elif '小知识' in msg:
            return getResponse(3, '921')
    except:
        return '从前有座山，山上有个庙，庙里有个老和尚，老和尚正在跟小和尚讲故事，讲的是：' * 5 + '...'


if __name__ == '__main__':
    print test({'message': '小黄鸡，给爷讲个笑话'}, None)
    print test({'message': '小黄鸡，给爷讲个故事'}, None)
    print test({'message': '小黄鸡，给爷讲点小知识'}, None)
    print handle({'message': '小黄鸡，给爷讲个笑话'}, None)
    print handle({'message': '小黄鸡，给爷讲个故事'}, None)
    print handle({'message': '小黄鸡，给爷讲点小知识'}, None)
