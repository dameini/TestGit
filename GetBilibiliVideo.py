import time
import requests
from bs4 import BeautifulSoup
import re
import json
import urllib

class videoFile():
    def __init__(self, bv):
        # 视频页地址
        self.url = 'https://www.bilibili.com/video/' + bv
        # 下载开始时间
        self.start_time = time.time()

    def get_vedio_info(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
            }

            response = requests.get(url = self.url, headers = headers)
            if response.status_code == 200:

                bs = BeautifulSoup(response.text, 'html.parser')
                # 取视频标题
                video_title = bs.find('span', class_='tit').get_text()

                # 取视频链接
                pattern = re.compile(r"window\.__playinfo__=(.*?)$", re.MULTILINE | re.DOTALL)
                script = bs.find("script", text=pattern)
                result = pattern.search(script.next).group(1)

                temp = json.loads(result)
                # 取第一个视频链接
                for item in temp['data']['dash']['video']:
                    if 'baseUrl' in item.keys():
                        video_url = item['baseUrl']
                        break

                return {
                    'title:'+ video_title,
                    video_url
                }
        except requests.RequestException:
            print('视频链接错误，请重新更换')

    def download_video(self, video):
        title = re.sub(r'[\/:*?"<>|]', '-', video['title'])
        url = video['url']
        filename = title + '.mp4'
        print(filename)
        opener = urllib.request.build_opener()
        opener.addheaders = [('Origin', 'https://www.bilibili.com'),
                                ('Referer', self.url),
                                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url = url, filename = filename)

bvv = 'BV1Vh411Z7j5'
bf = videoFile(bvv)
# videoFile.get_vedio_info()
title,url = bf.get_vedio_info()
# title = re.sub(r'[\/:*?"<>|]', '-', title['title'])
filename = title + '.mp4'
print(filename)
print(url)
opener = urllib.request.build_opener()
opener.addheaders = [('Origin', 'https://www.bilibili.com'),
                        ('Referer', url),
                        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')]
# urllib.request.install_opener(opener)
# urllib.request.urlretrieve(url, filename)

# print(title)
# print(url)
# print(bf)
# bf.download_video(bf.get_vedio_info())


