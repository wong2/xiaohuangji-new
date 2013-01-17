#coding=utf-8

"""
Copyright (c) 2013 Moody _"Kuuy"_ Wizmann <mail.kuuy@gmail.com>

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

import sys
import re
import os
import requests
import HTMLParser
import redis
try:
    from settings import REDIS_HOST
except:
    REDIS_HOST = 'localhost'


city_id_by_name = {
    u"北京": u"Beijing",
    u"天津": u"Tianjin",
    u"上海": u"Shanghai",
    u"重庆": u"Chongqing",
    u"石家庄": u"Shijiazhuang",
    u"唐山": u"Tangshan",
    u"秦皇岛": u"Qinhuangdao",
    u"邯郸": u"Handan",
    u"保定": u"Baoding",
    u"邢台": u"Xingtai",
    u"张家口": u"Zhangjiakou",
    u"承德": u"Chengde",
    u"廊坊": u"Cangzhou",
    u"廊坊": u"Langfang",
    u"衡水": u"Hengshui",
    u"太原": u"Taiyuan",
    u"大同": u"Datong",
    u"阳泉": u"Yangquan",
    u"长治": u"Changzhi",
    u"临汾": u"Linfen",
    u"呼和浩特": u"Huhehaote",
    u"包头": u"Baotou",
    u"赤峰": u"Chifeng",
    u"沈阳": u"Shenyang",
    u"大连": u"Dalian",
    u"鞍山": u"Anshan",
    u"抚顺": u"Fushun",
    u"本溪": u"Benxi",
    u"锦州": u"Jinzhou",
    u"长春": u"Changchun",
    u"吉林": u"Jilin",
    u"哈尔滨": u"Haerbin",
    u"齐齐哈尔": u"Qiqihaer",
    u"大庆": u"Daqing",
    u"牡丹江": u"Mudanjiang",
    u"南京": u"Nanjing",
    u"无锡": u"Wuxi",
    u"徐州": u"Xuzhou",
    u"常州": u"Changzhou",
    u"苏州": u"Suzhou",
    u"南通": u"Nantong",
    u"连云港": u"Lianyungang",
    u"扬州": u"Yangzhou",
    u"镇江": u"Zhenjiang",
    u"淮安": u"Huai'an",
    u"盐城": u"Yancheng",
    u"台州市": u"Taizhou",
    u"宿迁": u"Suqian",
    u"杭州": u"Hangzhou",
    u"宁波": u"Ningbo",
    u"温州": u"Wenzhou",
    u"嘉兴市": u"Jiaxing",
    u"湖州": u"Huzhou",
    u"绍兴": u"Shaoxing",
    u"台州市": u"Taizhou",
    u"金华": u"Jinhua",
    u"衢州": u"Quzhou",
    u"舟山": u"Zhoushan",
    u"丽水": u"Lishui",
    u"合肥": u"Hefei",
    u"芜湖": u"Wuhu",
    u"马鞍山": u"Maanshan",
    u"福州": u"Fuzhou",
    u"厦门": u"Xiamen",
    u"泉州": u"Quanzhou",
    u"南昌": u"Nanchang",
    u"九江": u"Jiujiang",
    u"济南": u"Jinan",
    u"青岛": u"Qingdao",
    u"淄博": u"Zibo",
    u"枣庄": u"Zaozhuang",
    u"烟台": u"Yantai",
    u"潍坊": u"Weifang",
    u"济宁": u"Jining",
    u"泰安": u"Taian",
    u"威海": u"Weihai",
    u"日照": u"Rizhao",
    u"东营": u"Dongying",
    u"莱芜": u"Laiwu",
    u"临沂": u"Linyi",
    u"德州": u"Dezhou",
    u"聊城": u"Liaocheng",
    u"滨州": u"Binzhou",
    u"菏泽": u"Heze",
    u"郑州": u"Zhengzhou",
    u"开封": u"Kaifeng",
    u"洛阳": u"Luoyang",
    u"平顶山": u"Pingdingshan",
    u"安阳": u"Anyang",
    u"焦作": u"Jiaozuo",
    u"三门峡": u"Sanmenxia",
    u"武汉": u"Wuhan",
    u"宜昌": u"Yichang",
    u"荆州": u"Jingzhou",
    u"长沙": u"Changsha",
    u"株洲": u"Zhuzhou",
    u"湘潭": u"Xiangtan",
    u"岳阳": u"Yueyang",
    u"常德": u"Changde",
    u"张家界": u"Zhangjiajie",
    u"广州": u"Guangzhou",
    u"韶关": u"Shaoguan",
    u"深圳": u"Shenzhen",
    u"珠海": u"Zhuhai",
    u"汕头": u"Shantou",
    u"佛山": u"Foshan",
    u"湛江": u"Zhanjiang",
    u"中山": u"Zhongshan",
    u"江门": u"Jiangmen",
    u"肇庆": u"Zhaoqing",
    u"东莞": u"Dongguan",
    u"惠州": u"Huizhou",
    u"顺德": u"Shunde",
    u"南宁": u"Nanning",
    u"柳州": u"Liuzhou",
    u"桂林": u"Guilin",
    u"北海": u"Beihai",
    u"海口": u"Haikou",
    u"三亚": u"Sanya",
    u"成都": u"Chengdu",
    u"自贡": u"Zigong",
    u"攀枝花": u"Panzhihua",
    u"泸州": u"Luzhou",
    u"德阳": u"Deyang",
    u"绵阳": u"Mianyang",
    u"南充": u"Nanchong",
    u"宜宾": u"Yibin",
    u"贵阳": u"Guiyang",
    u"遵义": u"Zunyi",
    u"昆明": u"Kunming",
    u"曲靖": u"Qujing",
    u"玉溪": u"Yuxi",
    u"拉萨": u"Lhasa",
    u"西安": u"Xian",
    u"铜川": u"Tongchuan",
    u"宝鸡": u"Baoji",
    u"咸阳": u"Xianyang",
    u"渭南": u"Weinan",
    u"延安": u"Yanan",
    u"兰州": u"Lanzhou",
    u"金昌": u"Jinchang",
    u"西宁": u"Xining",
    u"银川": u"Yinchuan",
    u"石嘴山": u"Shizuishan",
    u"乌鲁木齐": u"Wulumuqi",
    u"克拉玛依": u"Karamay",
}


kv = redis.Redis(REDIS_HOST)


class AirParser(HTMLParser.HTMLParser):
    def __init__(self, callback):
        HTMLParser.HTMLParser.__init__(self)
        self.callback = callback
        self.tag = ['city', None, 'aqi', 'msg', 'update_time']
        self.flag = 0

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if data.strip():
            tag = self.tag[self.flag]
            self.flag += 1
            if(tag):
                self.callback[tag] = data.strip()


def test(data, bot):
    message = data['message']
    if 'PM2.5' not in message and 'pm2.5' not in message:
        return False
    req = filter(lambda p: p[0].encode('utf-8') in message, city_id_by_name)
    return len(req) > 0


def get_air_data(city, cityid):
    '''http://www.aqicn.info/?city=Beijing&widgetscript&size=xsmall'''
    r = kv.get('pm25.%s' % (cityid))
    if r:
        return r

    params = {'city': cityid, 'size': 'xsmall', 'widgetscript': ''}
    r = requests.get('http://www.aqicn.info/', params=params)
    #print r.text
    msg = re.findall('document.write\("(.*)"\)', r.text)[0]
    result = {}
    air_parser = AirParser(result)
    air_parser.feed(msg)
    res = u"%(city)s: %(aqi)s, %(msg)s \
            (%(update_time)s from aqicn.info)" % result
    kv.setex('pm25.%s' % cityid, res, 60*30)
    return res


def handle(data, bot):
    for city in city_id_by_name:
        if city.encode('utf8') in data['message']:
            reply = get_air_data(city, city_id_by_name[city])
            return reply if reply else u'亲，抓取信息失败了'
    else:
        return u'没有该地区的信息'


if(__name__ == '__main__'):
    print u"PM2.56789", test({'message': "PM2.56789"}, None)
    print u"天津PM2.56789", test({'message': "天津PM2.56789"}, None)
    print handle({u'message': "天津PM2.56789"}, None)
    print handle({u'message': "火星PM2.56789"}, None)
