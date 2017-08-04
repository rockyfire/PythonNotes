#encoding=utf-8

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import requests


active_ip=[]

def test_ip(proxy):

    global active_ip

    url = "http://ip.chinaz.com/getip.aspx"

    try:
        r=requests.get(url,proxies=proxy,timeout=3)
        if r.status_code == 200:
            print ('{0} Success!!!'.format(proxy))
            active_ip.append(proxy['http'])
    except:
        print ("failure {0} 失效".format(proxy['http']))

def out_file(active_ip=[]):
    with open("./active.txt","a") as f:
        for ip in active_ip:
            f.write(ip+'\n')



pool=ThreadPool()
pool=ThreadPool(10)

if __name__=='__main__':


    with open("./ip.txt", 'r') as f:
        line = f.readlines()
        proxy = []
        for i in range(0, len(line)):
            ip = line[i].split("\n")
            proxy_host = "http://" + "".join(ip)
            proxy.append({"http": proxy_host})

        pool.map(test_ip,proxy)

    out_file(active_ip)