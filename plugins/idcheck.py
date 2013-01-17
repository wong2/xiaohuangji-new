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

# 查询id信息
import os
import sys
import idcheck


def test(data, bot):
    return 'id' in data['message'] and (2 == len(data['message'].strip().split()) or 2 == len(data['message'].strip().split(':')))


def handle(data, bot):
    msg = data['message'].strip()
    _id = (msg.split()[-1] if 2 == len(msg.split()) else msg.split(':')[-1]).strip().strip(':')
    reply = []
    for idcheck_name in idcheck.__all__:
        __import__('idcheck.%s' % idcheck_name)
        id_info = getattr(idcheck, idcheck_name).id_info(_id)
        reply.append(id_info + os.linesep*2) if id_info else reply
    return os.linesep.join(reply) if reply else '哇咔咔这个不存在哇'


if __name__ == '__main__':
    print test({'message': 'id guest'}, None)
    print test({'message': 'id: guest'}, None)
    print test({'message': 'id:guest'}, None)
    print test({'message': 'id : guest'}, None)
    print test({'message': 'id :  guest'}, None)
    print handle({'message': 'id xxoo'}, None)
    print handle({'message': 'id wong2'}, None)
