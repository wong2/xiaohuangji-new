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

# 白云黄鹤
import re
import os
import requests


class BYHH:

    def __init__(self, _id):
        self.qry_url = 'http://byhh.net/cgi-bin/bbsqry?userid=%s' % _id

    def byhh(self):
        try:
            r = requests.get(self.qry_url)
            id_info = r.text.split('<pre></center>')[1].split('</pre>')[0]
            newVkList = []
            [newVkList.append(vk) for vk in re.findall(r'<[0-9a-zA-Z /=]+>', id_info) if vk not in newVkList]
            for vk in newVkList:
                id_info = id_info.replace(vk, '')
            return '白云黄鹤'.decode('utf8') + os.linesep + id_info.strip()
        except:
            return 0


def id_info(_id):
    byhh = BYHH(_id)
    return byhh.byhh()


if __name__ == '__main__':
    print id_info('HQM')
