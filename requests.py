import requests

payload={'key1':'value1','key2':['value2','value3']}
headers={'user-agent':'1'}
r=requests.get("https://www.baidu.com",params=payload,headers=headers)

# print (r.url)


# print (r.text)
# print (r.status_code)
# print (r.headers) r.headers['Content-Type|...'] r.headers.get('content-type|...')
# print (r.encoding)
# print (r.apparent_encoding)
# print (r.content)

# print (r.json())



# 二进制内容 比如图片

# from PIL import Image
# from io import BytesIO
#
# i=Image.open(BytesIO(r.content))


# Post请求 Json格式

# url='https://api.github.com/some/endpoint'
# payload={'some':'data'}
# r=requests.post(url,json=payload)


# 上传文件

# files={'file':('report.xls',open('report.xls','rb'),'application/vd.ms-excel',{'Expires':'0'})}
# r=requests.post(url,files=files)
# r.text


# 发送cookie到服务器

# cookies=dict(cookies_are='working')
# r.request.get(url,cookies=cookies)


# 禁止重定向处理
# r=requests.get(url,allow_redirects=False)


# 服务器返回给我们的响应头部信息
# r.headers
# 发送到服务器的请求的头部
# r.request.headers

# 身份验证

# from requests.auth import AuthBase
#
# class PizzaAuth(AuthBase):
#     def __init__(self,username):
#         self.username=username
#
#     def __call__(self,r):
#         r.headers['']=self.username
#         return r
#
# requests.get('http://pizzabin.org/admin',auth=PizzaAuth('rockyfire'))



def getHtmlText(url):
    try:
        headers = {'user-agent': '1'}
        r=requests.get(url,timeout=3000,verify=True)
        r.raise_for_status() # if r.status_code==request.codes.ok
        r.encoding=r.apparent_encoding
        return r.status_code
    except:
        return "Something Wrong!"


if __name__=="__main__":

    # url = "https://www.baidu.com"
    url = "https://www.github.com"

    print (getHtmlText(url))