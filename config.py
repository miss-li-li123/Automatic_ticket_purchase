# -*- coding = utf-8 -*-
# @Time: 2023/5/30 21:53
# @File: config.PY
import json

user_agent = 'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.0.0 Mobile/15E148 Safari/604.1j'

info = {
    'id': '17773560880',
    'password': 'Woshishui1314@',
    'item_id': '610820299671',
    'viewer': ['viewer1'],
    'price': 580
    }
try:
    with open('info.txt', 'r', encoding='utf-8') as f:
        info = json.load(f)
except Exception as e:
    print('-' * 10, 'User information Exception! Check file info.txt', '-' * 10)
    with open('info.txt', 'w+') as f:
        json.dump(info, f)

# basic headers with user agent set to iPhone
base_headers = {
    'authority': 'm.damai.cn',
    'sec-ch-ua': '""',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '""',
    'upgrade-insecure-requests': '1',
    'user-agent': user_agent,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://damai.cn',
    'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7'
    }

base_params = {
    'jsv': '2.7.2',
    'appKey': 12574478,
    't': 0,
    'sign': '',
    'type': 'originaljson',
    'dataType': 'json',
    'v': '4.0',
    'H5Request': 'true',
    'AntiCreep': 'true',
    'AntiFlood': 'true',
    'api': 'mtop.trade.order.build.h5',
    'method': 'POST',
    'ttid': '#t#ip##_h5_2014',
    'globalCode': 'ali.china.damai',
    'tb_eagleeyex_scm_project': '20190509-aone2-join-test'
    }

# urlencode:
# exParams=%7B%22damai%22%3A+%221%22%2C+%22channel%22%3A+%22damai_app%22%2C+%22umpChannel%22%3A+%2210002%22%2C+%22atomSplit%22%3A+%221%22%2C+%22serviceVersion%22%3A+%221.8.5%22%7D&spm=a2o71.project.0.bottom&sqm=dianying.h5.unknown.value
#
# unquote damai url:
# exParams=%7B%22channel%22%3A%22damai_app%22%2C%22damai%22%3A%221%22%2C%22umpChann
#
# replace '+' then quote:
# exParams=%257B%2522damai%2522%253A%25221%2522%252C%2522channel%2522%253A%2522damai_app%2522%252C%2522umpChannel%2522%253A%252210002%2522%252C%2522atomSplit%2522%253A%25221%2522%252C%2522serviceVersion%2522%253A%25221.8.5%2522%257D&spm%3Da2o71.project.0.bottom%26sqm%3Ddianying.h5.unknown.value
# exParams=%257B%2522channel%2522%253A%2522damai_app%2522%252C%2522damai%2522%253A%25221%2522%252C%2522umpChannel%2522%253A%2522100031004%2522%252C%2522subChannel%2522%253A%2522damai%2540damaih5_h5%2522%252C%2522atomSplit%2522%253A1%257D&spm=a2o71.project.0.bottom&sqm=dianying.h5.unknown.value

