import requests
import parsel
import time
import random


def get_proxy():
    return str(requests.get('https://dps.kdlapi.com/api/getdps/?secret_id=o3r1yg352tkgd2ew53o8&num=1&signature=1frzw8th6c5wwknecf98v4lrp3bb5zmb&pt=1&format=json&sep=1').json()['data']['proxy_list'][0])

page_list = [i*50 for i in range(200)]
url_list = []
name_list = []
for i in page_list:
    #proxy = get_proxy()
    #proxy ='58.209.32.79:17971'
    #proxies = {
    #     'http': proxy,
    #     # 'https': proxy
    # }
    #print(proxy)
    base_url = f"https://tieba.baidu.com/f?kw=%E4%B8%9C%E5%8C%97%E7%9F%B3%E6%B2%B9%E5%A4%A7%E5%AD%A6&ie=utf-8&pn={i}]"
    headers = {"User-Agent": "Mozilla/5.0 (windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
               "Referer": "https://cn.bing.com/search?q=%E4%B8%9C%E5%8C%97%E7%9F%B3%E6%B2%B9%E5%A4%A7%E5%AD%A6%E5%90%A7&qs=n&form=QBRE&sp=-1&lq=0&pq=%E4%B8%9C%E5%8C%97%E7%9F%B3%E6%B2%B9%E5%A4%A7%E5%AD%A6%E5%90%A7&sc=5-7&sk=&cvid=82516763F37A4164A4DC50641F9DA86C&ghsh=0&ghacc=0&ghpl="}
    response = requests.get(url=base_url, headers=headers)
    html_str = response.text
    html = parsel.Selector(html_str)
    title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').extract()
    creator_list = html.xpath(
        '//div[@class="threadlist_author pull_right"]/span[@class="tb_icon_author"]/@title').extract()
    url_list = url_list + title_url
    with open('url.txt','w+') as fp:
        fp.write(str(url_list))
    print(title_url)
    # print(html_str)
    print(response.status_code)
    time.sleep(random.uniform(15,20))