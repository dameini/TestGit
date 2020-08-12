import requests
from bs4 import BeautifulSoup
import prettytable as pt
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_tianqi(url):
    # 获取天气状态
    data_list = []
    # url = "https://tianqi.so.com/weather/101270102"
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')  # 自动补全html代码，并按html代码格式返回

    WenDu = soup.find('div', class_='temperature').get_text()

    TianQi = soup.find('div', class_='weather-icon-wrap').get_text()

    data_list.append("现在的温度：%s\n现在天气情况：%s" % (WenDu, TianQi))

    List = soup.find_all('ul', class_='weather-columns')

    for item in List:
        data_list.append(item.get_text())

    # print("列表数据：", data_list)
    a = 1
    # 创建PrettyTable对象，用于将天气数据用表格的方式输出
    liebiao = pt.PrettyTable()
    liebiao.field_names = ["日期", "天气", "详情"]
    for item in data_list:
        # print(a)
        if a != 1:
            liebiao.add_row(
                [item.strip().split()[0] + item.strip().split()[1], item.strip().split()[2], item.strip().split()[3]])
        else:
            print(item.strip())
        a += 1

    print(liebiao)
    return liebiao


def send_email(sender, receiver, msg):
    # 发送邮件
    # 收件人
    receiver = receiver

    #发件人

    mail_title = '小可爱，请查收今天以及往后15天的天气预报，愿你三冬暖，春不寒'
    mail_body = str(msg)


    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    # (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）


    # 邮件的发件人
    message['From'] = sender
    # 邮件的收件人
    message['To'] = receiver
    # 邮件主题
    message['Subject'] = Header(mail_title, 'utf-8')

    # 创建发送邮件连接
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)

    # 发件人邮箱的SMTP服务器（即sender的SMTP服务器）
    smtpserver = 'smtp.qq.com'
    # 连接发送邮件的服务器
    smtp.connect(smtpserver)

    # 发件人邮箱的用户名和授权码（不是登陆邮箱的密码）
    username = '1029177123'
    # 邮箱授权码
    password = 'qytwreztbqxjbebb'
    # 登录到邮件服务器
    smtp.login(username, password)

    # 填入邮件的相关信息并发送
    smtp.sendmail(sender, receiver, message.as_string())

    smtp.quit()


# receiver_list = 'XXX@qq.com'
# tb = get_Data(url1)  # 获得每一个用户的数据
# send_mail(tb, receiver_list)  # 发送邮件
chengshi = 1

if chengshi:
    url = "https://tianqi.so.com/weather/101270110"  # 新津区天气
    tq = get_tianqi(url)
    jint = '今天天气'
    # msg1 = msg.add_row(jint + msg)
    # print(msg1)
    sender = input('输入发件人邮箱')
    send_email('1101165851@qq.com', tq)
else:
    url = "https://tianqi.so.com/weather/101270102"  # 龙泉
    tq = get_tianqi(url)


