# -*- coding:utf-8 -*-
import os
import sys
import requests
import datetime
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# reload(sys)
# sys.setdefaultencoding('utf-8')


def download(url):
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)

    # 新建日期文件夹
    download_path = os.path.join(download_path, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    # print download_path
    os.mkdir(download_path)

    all_content = requests.get(url).text  # 获取第一层M3U8文件内容
    if "#EXTM3U" not in all_content:
        raise BaseException("非M3U8的链接")

    if "EXT-X-STREAM-INF" in all_content:  # 第一层
        file_line = all_content.split("\n") # Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
        for line in file_line:
            if '.m3u8' in line:
                url = url.rsplit("/", 1)[0] + "/" + line  # 拼出第二层m3u8的URL
                all_content = requests.get(url).text

    file_line = all_content.split("\n")

    unknow = True
    key = "Njk2NTAzZGEtOGMxZS00NjJkLWI5NTItMGQ3M2M4MDQzMjU5MnNyUGRkdmpVa3M2NTIxREM1WWVWQmpyTStoTzlkSmVBQUFBQUFBQUFBRFRFZmpGSyt3SFFoakwrQnVTY0xxc00vMGhsS0xsM0ZoK3lXR2o4WElvczJOVTNvR2ZnUWFZ"
    for index, line in enumerate(file_line):  # 第二层
        # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        if "#EXT-X-KEY" in line:  # 找解密Key
            method_pos = line.find("MEATHOD")
            comma_pos = line.find(",")
            method = line[method_pos:comma_pos].split('=')[1]
            print("Decode Method：", method)


            uri_pos = line.find("URI")
            quotation_mark_pos = line.rfind('"')
            key_path = line[uri_pos:quotation_mark_pos].split('"')[1]

            key_url = url.rsplit("/", 1)[0] + "/" + key_path  # 拼出key解密密钥URL
            res = requests.get(key_url)
            key = res.content
            print
            "key：", key

        if "EXTINF" in line:  # 找ts地址并下载
            unknow = False
            pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]  # 拼出ts片段的URL
            # print pd_url

            res = requests.get(pd_url)
            c_fule_name = file_line[index + 1].rsplit("/", 1)[-1]

            if len(key):  # AES 解密
                cryptor = AES.new(key, AES.MODE_CBC, key)
                with open(os.path.join(download_path, c_fule_name + ".mp4"), 'ab') as f:
                    f.write(cryptor.decrypt(res.content))
            else:
                with open(os.path.join(download_path, c_fule_name), 'ab') as f:
                    f.write(res.content)
                    f.flush()
    if unknow:
        raise BaseException("未找到对应的下载链接")
    else:
        print
        "下载完成"
    merge_file(download_path)


def merge_file(path):
    os.chdir(path)
    cmd = "copy /b * new.tmp"
    os.system(cmd)
    os.system('del /Q *.ts')
    os.system('del /Q *.mp4')
    os.rename("new.tmp", "new.mp4")


if __name__ == '__main__':
    url = "https://media001.geekbang.org/14e7d5479d1c45669e24474e48ccbc20/650c03d496ab4debb56408a455a32225-16409e19136dd38cc7744ffc5b7e4445-ld-encrypt-stream.m3u8"
    download(url)
