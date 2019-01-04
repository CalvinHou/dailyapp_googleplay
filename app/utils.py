#!/usr/local/bin/python2.7
__author__ = 'houhuihua'

import time
import requests

def getdatedetail():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def getdate():
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

def get_httpstatuscode(url):
    try:
        request = requests.get(url)
        httpStatusCode = request.status_code
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        return e

def get_httpstatus_request(url):
    try:
        request = requests.get(url)
        return request
    except requests.exceptions.HTTPError as e:
        return e

