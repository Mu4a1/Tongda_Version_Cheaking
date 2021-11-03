# !/usr/bin/env python
# encoding  : utf-8
# @Time     : 2021/11/3/18:22
# @Author   : Mu4a1
# @File     : tongda version query.py
# @Desc     : tongda

import sys
import getopt
import requests
from bs4 import BeautifulSoup

def exp(url):
    urll = open(url)
    for i in urll:
        uri = i.strip() + 'inc/reg_trial.php'
        target = requests.get(uri)
        if target.status_code == 200:
            html = target.text
            version = BeautifulSoup(html, "html.parser")
            testx = version.find_all('div', class_='hd-title')
            print("%s -》" % i.strip() + testx[0].text)
        else:
            print("%s -》" % i.strip() + "查询失败！")

def main(argv):
    url = None

    try:
        opts,args = getopt.getopt(argv,'f:',["file="])
    except getopt.GetoptError:
        print("Target:python -f ip.txt")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-f','--file']:
            url = arg
        else:
            print("Target:python -f ip.txt")
    url = exp(url)


if __name__ == '__main__':
    main(sys.argv[1:])
