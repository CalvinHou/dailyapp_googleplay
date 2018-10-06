__author__ = 'houhuihua'

import time

def getDateDetail():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def getDate():
    return time.strftime("%Y-%m-%d", time.localtime())

def get_package(link):
    pos = link.find("id=")
    if (pos > -1):
        return link[pos+3:]
    return ""

def get_app_rank(title):
    pos = title.find(".")
    if (pos > -1):
        return title[0:pos]
    return ""

