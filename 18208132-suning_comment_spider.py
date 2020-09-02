import re,requests,time,random,json,csv
def list_drop_duplicate(list):
    for x in list:
        while list.count(x) > 1:
            del list[list.index(x)]
    return list
def csv_writer(data):
    with open('DATAt.csv', 'a+', newline='', encoding='gbk') as f:
        writer = csv.writer(f)
        writer.writerow(data)
def get_suning_p_id():
    u = 'https://search.suning.com/iPhone11/'
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    r = requests.get(url=u, headers=h)
    r.encoding = r.apparent_encoding
    a = re.findall('id="0000000000-(.*?)"', r.text)
    print(a)
    list_drop_duplicate(a)
    return a


def suning_comment():  # 苏宁店铺
    a = 0
    h = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_snsr=baidu%7Cbrand%7C%7Ctitle%7C%25E8%258B%258F%25E5%25AE%2581*%3A*brand; tradeMA=199; _snvd=15989497575356KqSHJShL9o; streetCode=7910199; cityCode=791; districtId=11480; cityId=9188; hm_guid=45472c3a-ea77-45e0-8998-cc2532ee1ab3; smhst=11346312294|0000000000; SN_CITY=140_791_1000188_9188_01_11480_1_1_99_7910199; _df_ud=c72c183d-ca7f-4048-a815-ea3c4a5006f8; _snms=159902764275393753; _snzwt=THCt421744d79efa2kW702856; route=294b3b1f866a4fdde2449f0414059805; authId=si0C56343F7CB76521B317A5324D162289; token=d2c7e3ea-0c10-4263-85aa-6a5d41ec0698; secureToken=B8CE722FC97F095F1EA21F33AC689976; _snmc=1; _snma=1%7C159894974050276935%7C1598949740502%7C1599029095532%7C1599031031570%7C8%7C4; _snmp=159903103098753914; _snmb=159903103157747792%7C1599031031593%7C1599031031577%7C1',
        'Host': 'review.suning.com',
        'Pragma': 'no-cache',
        'Referer': 'https://product.suning.com/0000000000/11346312294.html?safp=d488778a.13701.productWrap.2&safc=prd.0.0&safpn=10007',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    for id in get_suning_p_id():
        types = ['good', 'again', 'bad', 'normal']
        for type in types:
            page = 1
            while True:
                url = 'https://review.suning.com/ajax/cluster_review_lists/cluster-37201818-0000000' + id + '-0000000000-' + type + '-' + str(
                    page) + '-default-10-----reviewList.htm?callback=reviewList'
                re = requests.get(url=url, headers=h, timeout=3)
                text = re.text[len('reviewList') + 1:-1]
                data = json.loads(text)
                if 'commodityReviews' not in data:
                    break
                else:
                    for i in data['commodityReviews']:
                        data = [i['userInfo']['nickName'], i['commodityInfo']['charaterDesc1'],
                                i['commodityInfo']['charaterDesc2'], i['publishTime'], i['content']]
                        csv_writer(data)
                        print(i['userInfo']['nickName'])
                    page += 1
                    time.sleep(random.uniform(0, 5))
suning_comment()