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

day11 no zuo,no die .昨天想用python弄个html转pdf的小demo,参考[html转pdf](https://foofish.net/python-crawler-html2pdf.html)
秉承杀鸡用牛刀的精神,使用Scrapy写一个,yield scrapy.Request(urls,callback=self.parse_body) 返回的html不是按原网页列表中html顺序来的.无奈只能用写文件的操作把html按顺序排列,最后pdfkit的时候又出现
```
The switch --outline-depth, is not support using unpatched qt, and will be ignored.Error: This version of wkhtmltopdf is build against an unpatched version of QT, and does not support more then one input document.
```

最近几天的运气有点不好啊,issue有人说换个版本的wkhtmltopdf就可以了[换wkhtmltopdf版本](https://github.com/lzjun567/crawler_html2pdf/issues/12) --用命令行下载真是慢的一笔

day12 解决了前天的无法填写的问题,问题的原因主要是因为一开始password的display设置为none,只有点击后才会改变display为inline-block(其实在password上面还有一个input,点击这个input后,填写的就是password).

```
driver.execute_script('document.getElementById("TextBox2").style="display: inline-block; visibility: visible;"')
driver.execute_script('document.getElementById("TextBox2").contentEditable = true')
```

[参考资料](http://blog.csdn.net/windanchaos/article/details/55348061)
[display:none与visible:hidden的区别](http://www.cnblogs.com/nicholas_f/archive/2009/03/27/1423207.html)














