# -*- coding: gbk -*-
import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    # �������������
    HOST = 'smtp.qq.com'
    # �����ʼ�����
    SUBJECT = '������Դ'
    # ���÷���������
    FROM = '320783214@qq.com'
    # �����ռ�������
    TO = '359724828@qq.com'  # ������д������䣬�ö��ŷָ����������split�����ŷָ�
    message = MIMEMultipart('related')
    # --------------------------------------�����ı�-----------------
    # �����ʼ����ĵ��Է���������
    text = '���ӣ�https://pan.baidu.com/s/1GMcZ38OlYa-NN7hlDLUszg ��ȡ�룺n75H '
    message_html = MIMEText(text, 'plain', 'utf-8')  # \nΪ����
    message.attach(message_html)

    # -------------------------------------����ļ�---------------------
    # Ҫȷ����ǰĿ¼��test.csv����ļ�
    # message_xlsx = MIMEText(open('today_weather.xls', 'rb').read(), 'base64', 'utf-8')
    # �����ļ��ڸ������е�����
    # message_xlsx['Content-Disposition'] = 'attachment;filename="today_weather.xls"'
    # message.attach(message_xlsx)

    # �����ʼ�������
    message['From'] = FROM
    # �����ʼ��ռ���
    message['To'] = TO
    # �����ʼ�����
    message['Subject'] = SUBJECT

    # ��ȡ���ʼ�����Э���֤��
    email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
    # ���÷���������������Ͷ˿ڣ��˿�Ϊ465
    email_client.connect(HOST, '465')
    # ---------------------------������Ȩ��------------------------------
    result = email_client.login(FROM, 'vazakcfvsmgnbhif')
    print('��¼���', result)

    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
    # �ر��ʼ����Ϳͻ���
    email_client.close()
    print('���ͳɹ�')


send_email()
