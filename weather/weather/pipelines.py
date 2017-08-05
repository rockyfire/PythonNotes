# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb



class WeatherPipeline(object):
    def process_item(self, item, spider):

        with open('data/weather_data.txt','a') as f:
            f.write(str(item['site']) + '\n')
            f.write(str(item['weekday']) + '\n')
            f.write(str(item['temperature']) + '\n')
            f.write(str(item['state']) + '\n')
            f.write(str(item['wind']) + '\n\n')


        # img="".join(item['img']).rsplit('/',1)[-1]
        # with open('data/'+img,'wb') as f :
        #     f.write(requests.get("".join(item['img'])).content)

        print (isinstance(item,dict))

        my_dict={}

        for key in item:
            my_dict[key] = "".join(item[key])


        # Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str, unicode, int, long, float, bool,
        #                                                 None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key
        #
        # ensure_ascii：默认值True，如果dict内含有non - ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示
        #
        # indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty - printed
        # json
        #
        # separators：分隔符，实际上是(item_separator, dict_separator)
        # 的一个元组，默认的就是(',', ':')；这表示dictionary内keys之间用“, ”隔开，而KEY和value之间用“：”隔开。
        #
        # encoding：默认是UTF - 8，设置json数据的编码方式。
        #
        # sort_keys：将数据根据keys的值进行排序。


        with open('data/data.json','a') as f:
            f.write(json.dumps(my_dict,indent=4,ensure_ascii=False,sort_keys=True)+'\n')

        return item


class mysqlPipeline(object):
    def process_item(self, item, spider):
        site="".join(item['site'])
        weekday="".join(item['weekday'])
        temperature="".join(item['temperature'])
        state="".join(item['state'])
        wind="".join(item['wind'])
        img="".join(item['img'])
        connection=MySQLdb.connect(
                    host="localhost",
                    user="root",
                    passwd="1575",
                    db="candy", #数据库名字
                    port=3306,
                    charset="utf8",
        )
        # python3 字符串格式化问题
        try:
            with connection.cursor() as cursor:
                sql="""insert into weather(dates,week,temperature,weather,wind,img)
                        VALUES('{0}','{1}','{2}','{3}','{4}','{5}')""".format(site,weekday,temperature,state,wind,img)
                cursor.execute(sql)
            connection.commit()
        finally:
            connection.close()

        return item


class IPPipeline(object):
    def process_item(self, item, spider):
        with open("data/ip.txt",'a') as f:
            f.write("".join(item['ip'])+":"+"".join(item['port'])+'\n')
        return item

class chanyouji(object):
    def process_item(self, item, spider):
        return item





