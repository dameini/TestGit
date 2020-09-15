import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def login(login_qq, password, business_qq):
    '''
    登陆
    :param login_qq: 登陆用的QQ
    :param password: 登陆的QQ密码
    :param business_qq: 业务QQ
    :return: driver
    '''
    driver = webdriver.Chrome()

    driver.get('https://user.qzone.qq.com/{}/311'.format(business_qq))  # URL
    driver.implicitly_wait(5)  # 隐示等待，为了等待充分加载好网址
    driver.find_element_by_id('login_div')
    driver.switch_to.frame('login_frame')  # 切到输入账号密码的frame
    driver.find_element_by_id('switcher_plogin').click()  ##点击‘账号密码登录’
    driver.find_element_by_id('u').clear()  ##清空账号栏
    driver.find_element_by_id('u').send_keys(login_qq)  # 输入账号
    driver.find_element_by_id('p').clear()  # 清空密码栏
    driver.find_element_by_id('p').send_keys(password)  # 输入密码
    driver.find_element_by_id('login_button').click()  # 点击‘登录’
    driver.switch_to.default_content()

    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        return driver
    except:
        print('不能访问' + business_qq)
        return None

def get_shuoshuo(driver):

    page = 1
    while True:
        # 下拉滚动条
        for j in range(1, 5):
            driver.execute_script("window.scrollBy(0,5000)")
            time.sleep(1)

        # 切换 frame
        driver.switch_to.frame('app_canvas_frame')
        # 构建 BeautifulSoup 对象
        bs = BeautifulSoup(driver.page_source.encode('GBK', 'ignore').decode('gbk'))
        # 找到页面上的所有说说
        pres = bs.find_all('pre', class_='content')

        for pre in pres:
            shuoshuo = pre.text
            tx = pre.parent.parent.find('a', class_="c_tx c_tx3 goDetail")['title']
            print(tx + ":" + shuoshuo)

        # 页数判断
        page = page + 1
        if bs.find('a',title = '下一页') == None:
            break
        else:
            maxPage = bs.find('a', title='末页').text
            #
            if int(maxPage) < page:
                break

        driver.find_element_by_link_text(u'下一页').click()
        # 回到主文档
        driver.switch_to.default_content()
        # 等待页面加载
        time.sleep(3)
        # driver.quit()


drive = login('QQ号', 'QQ密码', 'QQ号')
get_shuoshuo(drive)
