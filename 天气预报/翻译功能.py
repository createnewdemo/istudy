# -*- coding: gbk -*-
import requests

text = '����'
url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(text)
r = requests.get(url).json()
r = r['translateResult'][0][0]['tgt']
print(r)
