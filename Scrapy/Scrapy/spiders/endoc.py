# -*- coding: utf-8 -*-
import scrapy

html_template="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    {content}
</body>
</html>
"""

class EndocSpider(scrapy.Spider):
    name = 'endoc'
    allowed_domains = ['scrapy.org']
    start_urls = ['https://docs.scrapy.org/en/latest/intro/overview.html']

    def parse(self, response):

        doc_a=response.xpath("//li[@class='toctree-l1']")

        for a in doc_a:
            url="".join(a.xpath("a[@class='reference internal']/@href").extract())
            if url.startswith('../'):
                urls = "https://docs.scrapy.org/en/latest/" + url[3:]
            else:
                urls = "https://docs.scrapy.org/en/latest/intro/" + url
            # 生成html序列
            # with open("data/data.txt", 'a') as f:
            #     f.write(urls.rsplit("/",1)[1]+'\n')
            yield scrapy.Request(urls,callback=self.parse_body)

    def parse_body(self,response):
        value=response.xpath('//div[@itemprop="articleBody"]').extract()
        html = html_template.format(content=value)
        html.encode("utf-8")
        # html文件
        f_name = str(response.url).rsplit("/",1)[1]
        with open(f_name, 'w') as f:
            f.write(html)
        yield



