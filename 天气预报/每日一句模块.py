# -*- coding: gbk -*-
import requests


def get_news():
    # �����ǰѽ�������ÿ��һ�����ù�������Ϣ���͸�������
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['note']
    print(contents)
    print(translation)
    # return contents,translation


get_news()
