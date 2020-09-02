import csv

import requests
import json

basic_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100009177422&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'


headers = {
    "cookie": "shshshfpa=9ee33117-b637-bc6a-33d3-90f02342594c-1590892079; __jdu=15908920799891096227338; areaId=21; ipLoc-djd=21-1827-3502-0; PCSYCityID=CN_360000_360100_360112; shshshfpb=cQ%20zDy2dX6CV70pZh0%2FapOw%3D%3D; jwotest_product=99; unpl=V2_ZzNtbUdXE0J2DkNTKxteUWJUEw5LBRERcQoVXSgQXgQzAhJbclRCFnQUR1xnGF8UZgoZXUNcQxZFCEdkeB5fA2AFEFlBZwFLI1YCFi9JH1c%2bbRFcS1dKFHYOQVxLKV8FVwMTbUJTSxR8AEVVfRFUDG8DE1VFVEATdwpPZEsebDVXBBFUQ1BKJXQ4R2Q5TQAMZgQbXUMaQxF9CU9ceBhaDW8KGl1DX0QWdg5EVnIpXTVk; __jdv=76161171|sogou-search|t_262767352_sogousearch|cpc|2081802769_0_41af2746a33e4f0b8cc553b8b830e017|1599005412819; shshshfp=b7846d979faddfe5c6ace412c575eb06; __jdc=122270672; 3AB9D23F7A4B3C9B=BPPEBARANL63K4233VO3AOUHUOI7OBUMDHY2KDKTP4OHPIS7FSZZ2L53VSOUD6YNXFNRTYVMQ32ZP72QJMGFKCHWKI; __jda=122270672.15908920799891096227338.1590892080.1599007255.1599033887.8; JSESSIONID=00E4C9DF94B3939B9B31837ACE6977CD.s1; shshshsID=f746367f143ff4251d9acfc07d712a4d_3_1599034054198; __jdb=122270672.3.15908920799891096227338|8.1599033887",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}


def get_page(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'gbk'
        # print(r.text)

        return r.text
    except Exception as e:
        print(e)


def get_info(page):
    try:
        page = page[len('fetchJSON_comment98') + 1:-2]
        text= json.loads(page)

        for i in text['comments']:
            a = [i['nickname'], i['productColor'], i['productSize'], i['referenceTime'], "".join(i['content'].split())]
            print(a)
            save_data([a])


       # 从Json对象获取想要的内容
       #  toCntPercent = jsonobj['data']['interCrowdInfo'][1]['toCntPercent']
       #
       #  # 生成行数据
       #  row.append(str(toCntPercent) + "%")
       #
       #  for item in items: #
       #      print(item)
       #
       #      yield item
    except Exception as e:
        print(e)


def save_data(datas):

    # with open("D:\\python自学\\数据采集.txt", "a", encoding="gbk") as f:
    #     for data in datas:
    #         f.write(data)
    #         f.write('\n')
    with open('DATA2.csv', 'a+', newline='', encoding='gbk') as f:
        for data in datas:
            writer = csv.writer(f)
            writer.writerow([data])
        f.close()

# def get_storeid():
#     initial_url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAmate30&enc=utf-8&spm=2.1.0'



urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100009177422&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(i) for i in range(0,100)]
for url in urls:
    page = get_page(url)
    datas = get_info(page)

