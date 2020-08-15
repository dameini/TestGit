import time
import requests
from bs4 import BeautifulSoup
import re
import json
import urllib
import moviepy
import ssl
import imageio
from moviepy.editor import *
import subprocess


class videoFile():

    def __init__(self, bv):
        # 视频页地址
        self.url = 'https://www.bilibili.com/video/' + bv
        # 下载开始时间
        self.start_time = time.time()
        self.video_filename = ''
        self.audio_filename = ''

    def get_vedio_info(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
            }

            response = requests.get(url=self.url, headers=headers)
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
                for item in temp['data']['dash']['audio']:
                    if 'baseUrl' in item.keys():
                        audio_url = item['baseUrl']
                        break
                return {
                    'title': video_title,
                    'video_url': video_url,
                    'audio_url': audio_url
                }
        except requests.RequestException:
            print('视频链接错误，请重新更换')

    def schedule(self, blocknum, blocksize, totalsize):
        '''
        urllib.urlretrieve 的回调函数
        :param blocknum: 已经下载的数据块
        :param blocksize: 数据块的大小
        :param totalsize: 远程文件的大小
        :return:
        '''
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        s = ('#' * round(percent)).ljust(100, '-')
        sys.stdout.write("%.2f%%" % percent + '[ ' + s + ']' + '\r')
        sys.stdout.flush()

    def download_video(self, video):
        title = re.sub(r'[\/:*?"<>|]', '-', video['title'])
        video_url = video['video_url']
        audio_url = video['audio_url']

        # print(url)
        video_filename = title + '_video.mp4'
        video_filename = video_filename.replace(' ', '')
        audio_filename = title + '_audio.mp4'
        audio_filename = audio_filename.replace(' ', '')
        self.video_filename = video_filename
        self.audio_filename = audio_filename
        # print(filename)
        opener = urllib.request.build_opener()
        opener.addheaders = [('Origin', 'https://www.bilibili.com'),
                             ('Referer', self.url),
                             ('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=video_url, filename=video_filename,reporthook = self.schedule)
        urllib.request.urlretrieve(url=audio_url, filename=audio_filename,reporthook = self.schedule)

    def getname(self):
        return {
            self.audio_filename,
            self.video_filename
        }


BV_Num = 'BV1z64y1u7rs'

File = videoFile(BV_Num)
File.__init__(BV_Num)
video = File.get_vedio_info()
File.download_video(video)


video_filename, audio_filename = videoFile.getname(File)
outfile_name = video_filename.replace('_video','')
subprocess.call('ffmpeg -y -i ' + video_filename
                + ' -i ' + audio_filename + ' -c copy '
                + outfile_name, shell=True)
subprocess.call('del ' + video_filename
                + ',' + audio_filename, shell=True)