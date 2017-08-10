from selenium import webdriver
import random
import requests
from bs4 import  BeautifulSoup


login_ip=[
    "http://210.38.137.125:8016/(f1e4b2j0meyp0u45omq5pbb0)/default2.aspx",
    "http://210.38.137.124:8016/(nxqwnjilyquwh33rb0ajh4fq)/default2.aspx"
]


driver=webdriver.Chrome()
random_ip=random.choice(login_ip)
validate_img=random_ip.rsplit("/",1)[0]+"/CheckCode.aspx"
#
driver.get(random_ip)
driver.implicitly_wait(3)
username=driver.find_element_by_id("txtUserName")
password=driver.find_element_by_id("TextBox2")

username.clear()
username.send_keys("201411701418")


driver.execute_script('document.getElementById("TextBox2").style="display: inline-block; visibility: visible;"')
driver.execute_script('document.getElementById("TextBox2").contentEditable = true')

password.clear()
password.send_keys("")

html=requests.get(random_ip)
soup=BeautifulSoup(html.text,'html.parser')

s=soup.find('img',attrs={'id':'icode'})['src']
print ("".join(s))







# 2.0 使用直接提交表单进行操作

# def get_data(url,username,password):
#     html=requests.get(url)
#     soup=BeautifulSoup(html.text,'html.parser')
#     __VIEWSTATE=soup.find_all('input',attrs={'name':'__VIEWSTATE'})['value']
#
#     data={}
#     data['__VIEWSTATE']=__VIEWSTATE
#     data['txtUserName']=username
#     data['TextBox2']=password
#     data['txtSecretCode']=''
#
#     return data


# import os
# import subprocess
#
# def image_to_string(img,cleanup=True,plus=''):
#     subprocess.check_output('tesseract '+img+' '+img+' '+plus,shell=True)
#     text=''
#     with open(img+'.txt','r') as f:
#         text = f.read().strip()
#     if cleanup:
#         os.remove(img+'.txt')
#
#     return text
#
#
# print(image_to_string())

# from PIL import Image
# import pytesseract as ocr
# from io import BytesIO
#
# img = Image.open(BytesIO(requests.get(s).content))
# img.load()
# img.show()