import requests
from bs4 import BeautifulSoup
import json
import time
import csv
from lxml import etree
import random
from selenium import webdriver  # 用来驱动浏览器的
DRIVER_PATH = r'D:\chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_argument('headless')  # 设置option
driver = webdriver.Chrome(options=option,executable_path=DRIVER_PATH)
# 根据url处理列表页信息
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
            'Referer': 'https://www.jd.com/',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
        }
def parse_list_page(url):
    driver.get(url)
    # 向下滑动 加载完全页面
    for i in range(2):
        driver.execute_script('document.documentElement.scrollTop=6000')
        time.sleep(3)  # 3秒再滑
    # 拿到网页完整源代码
    resp = driver.page_source
    html = etree.HTML(resp)

    goods_ids = html.xpath('.//ul[@class="gl-warp clearfix"]/li[@class="gl-item"]/@data-sku')
    goods_names_tag = html.xpath('.//div[@class="p-name p-name-type-2"]/a/em')
    goods_stores_tag = html.xpath('.//div[@class="p-shop"]')

    goods_names = []
    for goods_name in goods_names_tag:
        goods_names.append(goods_name.xpath('string(.)').strip())

    goods_stores = []
    for goods_store in goods_stores_tag:
        goods_stores.append(goods_store.xpath('string(.)').strip())

    goods_infos = list()
    idlist=[]
    for i in range(0, len(goods_ids)):
        goods_info = dict()
        idlist.append(goods_ids[i])
        goods_info['goods_id'] = goods_ids[i]
        goods_info['goods_name'] = goods_names[i]
        goods_info['goods_store'] = goods_stores[i]
        goods_infos.append(goods_info)
    return idlist
class Jd:
    def page_get(self, page, keyword):
        print('正在爬取第', page, '页')
        url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8&page=%s' % (keyword, page)
        browser = requests.get(url, headers=headers)
        idlist=parse_list_page(url)
        idlist = judge(idlist)
        return idlist

def csv_writer(data):
    with open('DATAt.csv', 'a+', newline='', encoding='gbk') as f:
        writer = csv.writer(f)
        writer.writerow(data)
def get_ip():
    proxies_list = []
    for i in range(10):
        url = "https://www.kuaidaili.com/ops/proxylist/" + str(i + 1)
        # 发送get请求
        response = requests.get(url=url)
        data_list = BeautifulSoup(response.text, "lxml")
        tr_list = data_list.select("#freelist > table > tbody")
        tr_list = BeautifulSoup(str(tr_list), "lxml")
        for tr in tr_list.find_all("tr"):
            proxies_dict = {}
            td = BeautifulSoup(str(tr), "lxml")
            try:
                http_type = td.find(attrs={"data-title": "类型"}).text.split(",")[1].strip()
            except:
                http_type = td.find(attrs={"data-title": "类型"}).text
            ip = td.find(attrs={"data-title": "IP"}).text
            port = td.find(attrs={"data-title": "PORT"}).text
            proxies_dict[http_type] = ip + ":" + port
            proxies_list.append(proxies_dict)
    return proxies_list
def down(id):
    h={
        'Accept': '* / *',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Cache - Control': 'no - cache',
        'Connection': 'keep - alive',
        'Cookie': 'areaId = 21;__jdu = 1429474989;shshshfpb = ruKcvuQS1JLSFK4YwVTDgVg % 3D % 3D;shshshfpa = 26bdf3e2 - 0015 - 8f1c - ae7a - bb7310b4adf0 - 1587180749;user - key = 012f3b6a - e3d8 - 4e19 - 96d5 - 7da0b22e8de7;cn = 1;ipLoc - djd = 21 - 1827 - 3502 - 40963;unpl = V2_ZzNtbUBQERcnCUNVcxwJBWJRFVlKAEcUdAhBUSwdCQBkBkJdclRCFnQUR1xnGFoUZwIZXUFcRxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHscXw1iBRdVS19zJXI4dmR4HVUNZQEiXHJWc1chVEZQch1VDSoDF15KUkUQfQFOZHopXw % 3d % 3d;__jdv = 76161171 | baidu - pinzhuan | t_288551095_baidupinzhuan | cpc | 0f3d30c8dba7459bb52f2eb5eba8ac7d_0_36c3c04094d14c659f500164f5d424a1 | 1599444775911;PCSYCityID = CN_360000_360100_360112;__jda = 122270672.1429474989.1598834012.1599012696.1599444776.14;__jdc = 122270672;shshshfp = 80c57ef9966ce3791d37227ff37a2b37;3AB9D23F7A4B3C9B = 5PVLYNOBVPBVCCY75KTWODEVOBNGNYAPNKHQNIQH2NLZLBSIES3MVAASOXWCXNBQET6M5S2XYUU3PWIW3FPDJ33FTM;jwotest_product = 99;__jdb = 122270672.7.1429474989 | 14.1599444776;shshshsID = e75a49797ecb4022f7ec18108f36277e_7_1599446902623;JSESSIONID = 7283ED5D7103C0D66F4F7F0A9114C1F7.s1',
        'Host': 'club.jd.com',
        'Pragma': 'no - cache',
        'Referer': 'https: // item.jd.com / 56647977342.html',
        'Sec - Fetch - Dest': 'script',
        'Sec - Fetch - Mode': 'no - cors',
        'Sec - Fetch - Site': 'same - site',
        'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.105Safari / 537.36'
    }
    score=['1','2','3','5','7']
    for i in score:
        page = 0
        while True:
            try:
                url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId='+id+'&score='+str(i)+'&sortType=5&page='+str(page)+'&pageSize=10&isShadowSku=0&fold=1'
                print(url)
                text = requests.get(url=url, headers=h)
                text = text.text[len('fetchJSON_comment98') + 1:-2]
                print(text)
                data = json.loads(text)
                if data['comments']==[]:
                    print('下一类')
                    break
                for d in data['comments']:
                    a = [d['nickname'], d['productColor'], d['productSize'], d['referenceTime'], "".join(d['content'].split()),i]
                    print(id,page,i,d['nickname'])
                    try:
                        csv_writer(a)
                    except:
                        pass
                page+=1
                time.sleep(random.uniform(0,5))
            except:
                time.sleep(10)
                pass
def judge(list):
    newlist=[]
    for id in list:
        url="https://item.jd.com/"+str(id[0])+".html#none"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
            'Referer': 'https://www.jd.com/',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        try:
            print(url)
            texts = soup.select("div[class='Ptable-item'] dl[class='clearfix']")[1].text
            if (texts[1:5] != '产品名称'):
                texts = soup.select("div[class='Ptable-item'] dl[class='clearfix']")[2].text
                print("")
            else:
                print("")
            titile2 = ['iPhone 11', 'Apple iPhone 11', 'IPHONE 11', 'iphone11', '苹果 iPhone 11']
            # print(texts[5:],"********",texts[5:] in titile2,len(texts[5:].strip()))
            if (texts[5:].strip() in titile2):
                print(texts[5:],id[0])
                newlist.append(id[0])
            else:
                print("")
        except:
            texts = soup.select("ul[class='parameter2 p-parameter-list'] li")[0].text
            if((texts[5:].strip()=='AppleiPhone 11') or (texts[5:].strip()=='AppleiPhone11') or[texts[5:].strip()=='商品名称：Apple 苹果  iPhone 11 手机 全网通 双卡双待 黑色 128GB']):
                print(texts[5:],id[0])
                newlist.append(id[0])
            else:
                print('非iphone11',url)
    return newlist
def jingdong():#京东店铺
    # 1差评    2中评     3好评       5追评    7视频晒单
    title=['留言人', '颜色','内存','时间', '评论内容','评论类型']
    # csv_writer(title)
    jd = Jd()
    for i in range(0,6):
        id_list = jd.page_get(i, 'iphone11')
        print(id_list)
        print(len(id_list),'店铺')
        for i in id_list:
            down(i)
jingdong()