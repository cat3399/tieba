import requests
import re
import parsel
from parsel import Selector
import time
import random

# 通过api获取代理ip
def get_proxy():
    #return requests.get('http://127.0.0.1:5010/get').json()['proxy']
    # 快代理
    return str(requests.get('https://dps.kdlapi.com/api/getdps/?secret_id=o3r1yg352tkgd2ew53o8&num=1&signature=1frzw8th6c5wwknecf98v4lrp3bb5zmb&pt=1&format=json&sep=1').json()['data']['proxy_list'][0])

# 若访问超时则删除并切换代理
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def del_bai(list):
    list=[i.strip() for i in list]
    return list

def str2list(string:str):
    lis=string.split("'")
    lis.remove('[')
    lis.remove(']')
    # lis.remove("'")
    lis.remove(', ')
    list=[i for i in lis if i[1]=='/']
    print(list)
    return list

with open('urls.txt','r+') as fp:
    page_list=fp.readline()
# print(page_list)
text_list=[]
page_list=eval(page_list)
length=int(len(page_list)/3)
page_list=page_list[:length:]
print(page_list)
print(length)
page=''
j=0
try:
    for i in page_list:
        print(i)
        # proxy=get_proxy()
        # # 添加代理ip
        # proxy_http = 'http://' + proxy
        # proxies = {
        #     'http': proxy_http,
        # }

        base_url = f"https://tieba.baidu.com{i}"
        headers = {"User-Agent": "Mozilla/5.0 (windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        response = requests.get(url=base_url, headers=headers)
        html_str = response.text
        # xpath提取

        html = parsel.Selector(html_str)
        text=html.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/text()').extract()
        text_list.append(del_bai(text))
        print(del_bai(text))
        time.sleep(random.uniform(1,2))
        page=i
        if page !='/p/8203141222':
            with open('content.txt', 'w+',encoding='utf-8') as fp:
                fp.write(str(text_list) + page)
        else:
            with open('content-year.txt', 'w+',encoding='utf-8') as fp:
                fp.write(str(text_list) + page)
except Exception as e:
    with open('content.txt', 'w+',encoding='utf-8') as fp:
        fp.write(str(text_list)+page)
    print(text_list)
    print(e)

