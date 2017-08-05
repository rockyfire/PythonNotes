
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from fake_useragent import UserAgent



class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers.setdefault('User-agent',ua.random)


import random


class customRandomProxy(object):
    def active_ip(self):
        with open("data/active.txt") as f:
            line = f.readlines()
            active_ip = []
            for i in range(0, len(line)):
                active_ip.append("".join(line[i].split('\n')))
            return random.choice(active_ip)

    def process_request(self, request, spider):
        request.meta['proxy']=self.active_ip()


