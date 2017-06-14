#!/usr/bin/python
# -*- coding:UTF-8 -*-

import urllib2
import re
import requests
from HTMLParser import HTMLParser
import time
import urllib2
from bs4 import BeautifulSoup




# re.S 整个字符串看成一行不去关注是否有换行符
# re.I 忽略大小写

# Python2.7


def crawl_joke_list(page=4):
    url = "http://www.qiushibaike.com/8hr/page/" + str(page)

    # request = urllib2.Request(url)
    # request.add_header('User-Agent', 'fake-client')
    # response = urllib2.urlopen(request)
    # text = response.read().decode("utf-8")

    text=requests.get(url).content.decode("utf-8")

    pattern = re.compile("<div class=\"article block untagged mb15.*?<div class=\"content\">.*?</div>", re.S)
    html_parser = HTMLParser()
    body = html_parser.unescape(text).replace("<br/>", "")
    m = pattern.findall(body)
    user_pattern = re.compile("<div class=\"author clearfix\">.*?<h2>(.*?)</h2>", re.S)
    content_pattern = re.compile("<div class=\"content\">.*?<span>(.*?)</span>", re.S)
    strs=""
    for joke in m:

        user = user_pattern.findall(joke)
        output = []
        if len(user) > 0:
            output.append(user[0])

        content = content_pattern.findall(joke)
        if len(content) > 0:
            output.append(content[0])
        strs="\n".join(output).encode("utf-8")
        print  strs   # "\t" 使用tab符号连接列表的所有元素  "\n" 换行

    with open("hello","arw+") as f:
        f.writelines(strs)
    time.sleep(1)

# if __name__ == '__main__':
#     crawl_joke_list()

# 爬取照片

def file_save_img(image_url, image_local_path):
    r = requests.get(image_url, stream=True)
    with open(image_local_path, "wb") as f:
        f.write(r.content)


def craw_joke_img(page=1):
    url = "http://www.qiushibaike.com/imgrank/page/" + str(page)

    request = urllib2.Request(url)
    request.add_header('User-Agent', 'fake-client')
    response = urllib2.urlopen(request)
    text = response.read().decode("utf-8")

    # text=requests.get(url).content.decode("utf-8")
    content_list = re.findall(r'<div class="thumb">(.*?)</div>', text, re.S)
    for content in content_list:
        image_list = re.findall(r'<img src="(.*?)"', content)
        for img_url in image_list:
            file_save_img("https:" + img_url, "./img/" + img_url.strip().split('/')[-1])


# beautifulsoup

def craw_beautifulsoup_img(page=1):
    urls = "http://www.qiushibaike.com/imgrank/page/" + str(page)
    res = requests.get(urls)
    soup = BeautifulSoup(res.text, "html5lib")
    joke_list = soup.find_all("div", class_="thumb")
    for child in joke_list:
        img_url = child.find("img").get("src")
        file_save_img("https:" + img_url, "./img/" + img_url.strip().split('/')[-1])


# if __name__ == '__main__':
#     craw_beautifulsoup_img()















