import requests

cookies = [{'uuid_tt_dd': '10_30632948830-1583285720224-599567', 'dc_session_id': '10_1583285720224.580152',
            '__gads': 'ID=17a2b4f3abafd742-2276b60689c2003a:T=1594951644:S=ALNI_Mb5LiGVHxH-iimKzHCnDPGUmPkYkA',
            'p_uid': 'U010000',
            'searchHistoryArray': '%255B%2522MATLAB%2522%252C%2522QT%2522%252C%2522%25E6%258A%25A5'
                                  '%25E6%2596%2587%25E6%2595%25B0%25E6%258D%25AE%25E9%2595'
                                  '%25BF%25E5%25BA%25A6%25E4%25B8%25BA0%2520%2522%255D',
            'UserName': 'weixin_43189821', 'UserInfo': '05ed460b6ec346b4a4ddd3594691cdf7',
            'UserToken': '05ed460b6ec346b4a4ddd3594691cdf7',
            'UserNick': '%E5%B0%8F%E9%92%A2%E7%82%AE%E3%80%82%E3%80%82%E3%80%82	', 'AU': '6FB',
            'UN': 'weixin_43189821', 'BT': '1600661902098',
            'Hm_up_6bcd52f51e9b3dce32bec4a3997715ac': '%7B%22uid_%22%3A%7B%22value%22%3A%22weixin_43189821'
                                                      '%22%2C%22scope%22%3A1%7D%2C%22islogin%22%3A%7B%22value'
                                                      '%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value'
                                                      '%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value'
                                                      '%22%3A%220%22%2C%22scope%22%3A1%7D%7D	',
            'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac': '6525*1*10_30632948830-1583285720224-599567!5744*1*weixin_43189821',
            'announcement': '%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl'
                            '%2522%253A%2522https%253A%252F%252Flive.csdn.net'
                            '%252Froom%252Fyzkskaka%252F5n5O4pRs%253Futm_source'
                            '%253D1598583200%2522%252C%2522announcementCount%2522%253A0%257D	',
            'log_Id_click': '9', 'dc_sid': '360480f982744c5da1046c58bc627645', 'c_first_ref': 'www.baidu.com	',
            'c_segment': '15',
            'aliyun_webUmidToken': 'T2gAQgjryiNpiEytz-tEgX8zBbapOqhlP2U3osBIv5vc4rTM3Wsor4WeqTKgbL1tk7lhDjcMbtBcZ-YAkif6GquZ	',
            'c_first_page': 'https%3A//blog.csdn.net/wangzi11111111/article/details/79601860	',
            'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac': '1601263411,1601263430,1601271942,1601272042',
            'c_page_id': 'default', 'log_Id_view': '383',
            'c_ref': 'https%3A//blog.csdn.net/xyfx_fhw/article/details/94611533',
            'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac': '1601272747', 'dc_tos': 'qhctyj', 'log_Id_pv': '122'}]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

r = requests.get('https://i.csdn.net/', cookies=cookies, headers=headers)
print(r.text)
print()