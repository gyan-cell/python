import requests
from lxml.html import fromstring
import random
import time


def getCurrentIp():
    r = requests.get("https://api.ipify.org")
    print(r.text)


class rotateIp:
    def __init__(self):
        self.ipList = []

    def addIp(self, ip):
        self.ipList.append(ip)

    def showAllIp(self):
        print(self.ipList)

    def generateIpList(self):
        respone = requests.get("https://free-proxy-list.net/")
        parsed = fromstring(respone.text)
        for i in parsed.xpath("//tbody/tr"):
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join(
                    [i.xpath(".//td[1]/text()")[0], i.xpath(".//td[2]/text()")[0]]
                )
                self.addIp(proxy)

    def generateRandomIp(self):
        if self.ipList.__len__() < 3:
            print("Not enough proxies , The operation will be terminated")
        else:
            proxy = random.choice(self.ipList)
            print(proxy)
            return proxy
