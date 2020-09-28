def get_request(self, url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
    except Exception as e:
        print("请求出错：", e)

    return None


def search_music(self, key):
    # 20: 查询 20 条数据，key：关键字
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=%d&w=%s' % (20, key)
    resp = self.get_request(url)
    resp_json = json.loads(resp.text[9:][:-1])
    data_song_list = resp_json['data']['song']['list']
    song_list = []
    for song in data_song_list:
        singers = [s.get("name", "") for s in song.get("singer", "")]
        song_list.append({'name': song['songname'], 'songmid': song['songmid'], 'singer': '|'.join(singers)})

    return song_list