from bs4 import BeautifulSoup
import requests
import os


#获取网页
def get_HtmlText(url,**kwargs):
    try:
        r = requests.get(url, params=kwargs,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except :
        return "Wrong Error"

# 解析下载后html
def get_Content(url,number):
    url_list=[]
    for i in range(1,number):
        html = get_HtmlText(url + str("/f"), kw="林允儿", ie="utf-8", pn=50*i)
        url_list.append(html)

    os.chdir("./" + str("img")) #新建img目录后切换到该目录下

    for html in url_list:
        soup = BeautifulSoup(html, 'html.parser')
        for i in get_url(soup,"a","j_th_tit ",'href',url):
            html=get_HtmlText(i)
            soup = BeautifulSoup(html, 'html.parser')
            for img_src in get_url(soup,'img',"BDE_Image",'src'):
                img_name=img_src.rsplit('/',1)[-1]
                down_load(img_src,img_name)

# 下载图片
def down_load(img_src,img_name):
    res=requests.get(img_src)
    with open(img_name,'wb') as f:
        f.write(res.content)

# 获取url
def get_url(soup,attrs,classs,search,url=""):

    comment=[]
    for a in soup.find_all(attrs,class_=classs):
        urls=url+a[search]
        comment.append(urls)
    return comment

if __name__ == "__main__":
    url="http://tieba.baidu.com"
    get_Content(url,2)



# 链接去重
# url_lists=list(set(url_lists))


# html = get_html(url).replace('<br/>', '\n')

