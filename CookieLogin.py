import requests
from pyquery import pyquery as pq


def find_html_content(url):
    headers = {
                'User-Agent': 'Mozilla/5.0(Macintosh;Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gerko) Chrome/52.0.2743.116 Safari/537.36'
            }
    html = requests.get(url,headers=headers).text
    return html


def read_and_wiriteblog(html):
    doc = pq(html)

    article = doc('.blog-content-box')
    #文章标题
    title = article('.title-article').text()

    content = article('.article_content')

    try:
        dir = "F:/python-project/SpiderLearner/CSDNblogSpider/article/"+title+'.txt'
        with open(dir, 'a', encoding='utf-8') as file:
            file.write(title+'\n'+content.text())
    except Exception:
        print("保存失败")


def geturls(url):
    content = find_html_content(url)
    doc = pq(content)
    urls = doc('.article-list .content a')
    return urls


def main(offset):
    url = '此处为博客地址' + str(offset)
    urls = geturls(url)
    for a in urls.items():
        a_url = a.attr('href')
        print(a_url)
        html = find_html_content(a_url)
        read_and_wiriteblog(html)
if __name__ == '__main__':
    doc = pq(html)
    article = doc('.blog-content-box')
    # 文章标题
    title = article('.title-article').text()

    content = article('.article_content')

    try:
        dir = "F:/python-project/SpiderLearner/CSDNblogSpider/article/" + title + '.txt'
        with open(dir, 'a', encoding='utf-8') as file:
            file.write(title + '\n' + content.text())
    except Exception:
        print("保存失败")