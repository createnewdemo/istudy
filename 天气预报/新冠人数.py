# -*- coding: gbk -*-
import requests


def COV():
    url = 'https://api.yonyoucloud.com/apis/dst/ncov/country'
    Headers = {
        'apicode': '1aaef2983911441ba03470a297b1c163'
    }
    r = requests.get(url, headers=Headers).json()
    currentConfirmedCount = r['data']['currentConfirmedCount']  # �ִ�ȷ�ȥ���Ѿ�������
    currentConfirmedAdd = r['data']['currentConfirmedAdd']  # ���������ӻ����
    suspectedCount = r['data']['suspectedCount']  # �ִ�����
    suspectedAdd = r['data']['suspectedAdd']  # ��������
    curedCount = r['data']['curedCount']  # �ۼ�����
    updateTime = r['data']['updateTime']  # ����ʱ��
    # print(updateTime)
    info = [currentConfirmedCount, currentConfirmedAdd, suspectedCount, suspectedAdd, curedCount, updateTime,
            updateTime]
    text = '�ִ�ȷ�ȥ���Ѿ�������:' + str(info[0]) + '\n���������ӻ����:' + str(info[0]) + '\n�ִ�����:' + str(info[0]) + '\n��������:' + str(
        info[0]) + '\n�ۼ�����:' + str(info[0]) + '\n����ʱ��:' + str(info[0])
    print(text)


COV()

# if msg_content == '�¹�����':
#     try:
#         time.sleep(1)
#         eng = self.get_news()[0]
#         info = self.COV()
#         text = """
#         �ִ�ȷ�ȥ���Ѿ�������+info['currentConfirmedCount']\n
#         ���������ӻ����+info['currentConfirmedAdd']\n
#         �ִ����� + info['suspectedCount']\n
#         �������� + info['suspectedAdd']\n
#         �ۼ����� + info['curedCount']\n
#         ����ʱ�� + info['updateTime']
#         """
#
#         self.wx.send_text(to_user=self.wx_id, msg=text)
#
#     except Exception as error:
#         print(error)
