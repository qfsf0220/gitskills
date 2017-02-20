#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gevent import monkey
monkey.patch_all()

import gevent
import requests
from bs4 import BeautifulSoup
from multiprocessing import cpu_count, Process
import time


def search_price(houses_name):
    retry_time = 3
    sleep_time = 1
    url = "http://shanghai.anjuke.com/sale/rd1?from=zjsr&kw=%s" % houses_name
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}
    for i in range(retry_time):
        try:
            res = requests.get(url, headers=headers, timeout=2)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'lxml')
                text = soup.find_all('div', class_="comm-price")
                content_li = [i for i in text[0].get_text(",", strip=1).split(",") if i]
                break
            else:
                time.sleep(sleep_time)
                continue
        except:
            continue
    else:
        print("Get %s Error" % houses_name)
        return

    if  ')' in content_li[2]:
        t_li = []
        t_li = content_li[3:]
        t_li.insert(0, content_li[0])
        content_li = t_li
    loc = content_li[0].split()[0]  if "别名" in content_li[0] else content_li[0]
    cur_month = content_li[1]
    price = content_li[2]
    comp_month = content_li[3]
    comp_price = content_li[4]
    print(loc + cur_month + cprint(price,"red") + comp_month + cprint(comp_price,"red"))


def cprint(info, color):
    color_table = {
        'black': '\033[0;30m%s\033[1;m',
        'red': '\033[1;31m%s\033[1;m',
        'green': '\033[1;32m%s\033[1;m',
        'blue': '\033[1;34m%s\033[1;m',
        "yellow": "\033[1;33m%s\033[1;m"
    }
    if color in color_table:
        return color_table[color] % info
    else:
        return info


def get_avg(lst, n):
    increment = len(lst) / float(n)
    last = 0
    i = 1
    while last < len(lst):
        idx = int(round(increment * i))
        yield lst[last:idx]
        last = idx
        i += 1

def worker(houses_name=None):
    if houses_name:
        jobs = [ gevent.spawn(search_price, house)
                for house in  houses_name ]
        gevent.joinall(jobs)

def main():
    houses_names = [ '徐汇臻园','东湾度假村','苑宏新村','中海瀛台','徐汇苑','南方新村','盛华景苑','徐汇华园',
                   '紫阳花园','印象欧洲','浦润苑','华唐苑','银泰苑','新凯家园一期','中冶锦城','漓江山水花园',
                   '华泾绿苑','华泾五村','华欣家园','东湾小区','馨宁公寓','徐汇新干线','爱庐世纪新苑',
                   '新弘国际城','南方城','晶欣坊','华发小区','枫桦景苑','华建一街坊','华沁家园' ]

    gen_house = get_avg(houses_names, cpu_count())
    t1 = time.time()
    processes = [ Process(name="Process-{}".format(core), target=worker, args=( [ gen_house.__next__() ])) for core in range(cpu_count()) ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    t2 = time.time()
    print("Processing %.2f s" % (t2 - t1))


if __name__ == '__main__':
    main()