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

# 饮水思源
import re
import os
import requests


class YSSY:

    def __init__(self, _id):
        self.qry_url = 'https://bbs.sjtu.edu.cn/bbsqry?userid=%s' % _id

    def yssy(self):
        try:
            r = requests.get(self.qry_url)
            pre = r.text.split('<pre class=tight>')[1]
            back = pre.split('</pre>')
            id_info = back[0] if len(back) == 2 else pre.split('目前 '.decode('utf8'))[0]
            newVkList = []
            [newVkList.append(vk) for vk in re.findall(r'<[a-zA-Z0-9 /=\']+>', id_info) if vk not in newVkList]
            for vk in newVkList:
                id_info = id_info.replace(vk, '')
            return '饮水思源'.decode('utf8') + os.linesep + id_info.strip()
        except:
            return 0


def id_info(_id):
    yssy = YSSY(_id)
    return yssy.yssy()


if __name__ == '__main__':
    print id_info('guest')
    print id_info('python')
