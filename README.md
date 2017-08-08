# PythonNotes
Python笔记始于2017-06-11

代码来之 http://blog.leanote.com/cate/qq-alan/python%E6%95%99%E7%A8%8B

我只是按我自己的习惯分类而已

从零开始学爬虫 2017-07-30

day01 通读了一下requests 和 Beautiful Soup 的 文档 

day02 写一个爬虫的小demo (百度贴吧的前几页贴中的图片),了解反爬虫的知识(robots.txt)代理IP User-Agent

day03 本来想使用squid和stunnel搭建一个代理服务器,忙了一天一点进展都没有.连最基本的安装squid后,通过SwitchyOmega/SwitchySharp连接到3128端口都不行,太失败了

day04 Scrapy入门而已,掌握XPath的基本语法  [Xpath提取多个标签下的text](http://www.tuicool.com/articles/iqQFBn)

day05 提取天气预报的关键信息练手Scrapy,大部分的时间在学json和python的结合.

day06 获取可用的IP代理,Scrapy获取的过程中遇到503错误,通过设置User-Agent或DOWNLOAD_DELAY = 3(延迟下载)来解决(docker新书已到)

day07 自定义下载器中间件,突破IP/User-Agent封锁

其实在settings.py中设置DEFAULT_REQUEST_HEADERS后,修改
```
  class xxxSpider(scrapy.Spider):
    def __init__(self): 
        self.header=DEFAULT_REQUEST_HEADERS
```
也可以实现效果

day08 爬山

day09 学习selenium(看了一遍中文文档)和安装Phantomjs,拿学校的教务系练手(登陆正方教务系统)结果敗在自动填写上,密码的填写项不允许操作

```
selenium.common.exceptions.InvalidElementStateException: Message: invalid element state: Element is not currently interactable and may not be manipulated
```

day10 使用tesseract进行验证码的解析错误提示:

```
Error in pixReadStreamGif: Can't use giflib-5.1.2; suggest 5.1.1 or earlier
```
下载了低版本的,但是不会编译链接成os文件.昨天的selenium问题还在问另一个大佬.















