#!/usr/local/bin/python2.7
__author__ = 'houhuihua'

import urllib2
import utils

from bs4 import BeautifulSoup
from appinfo import *


def parse_all_apps(allcategories, callback):
    urlGen = UrlGen()
    appsListTotal = []
    appsList = []
    count = 0
    for url in allcategories:
        try:
            htmlTxt = urllib2.urlopen(url.url).read()
            print("cc:%d len = %d category = %s, url=%s" % (count, len(htmlTxt), url.name, url.url))
            soup = BeautifulSoup(htmlTxt, 'html.parser')
            appTitleLists = soup.select("div.details > a.title")
            appDescLists = soup.select("div.details > div.description")
            appCompanyLists = soup.select("div.details > div.subtitle-container > a.subtitle")
            appIconLists = soup.select("div.cover-inner-align > img.cover-image")

            base = len(appsListTotal)
            for i in appTitleLists:
                text = i.get_text()
                href = i.get("href")
                rank = utils.get_app_rank(text)
                #print "title:", text
                #print "href:", href
                app = AppDetail()
                app.rank = rank
                app.title = i.get("title")
                app.link = urlGen.get_base_link() + href
                app.category = url.name
                appsListTotal.append(app)
                appsList.append(app)

            index = base
            for i in appDescLists:
                desc = i.get_text()
                #print "desc:", desc
                appsListTotal[index].desc = desc
                appsList[index - base].desc = desc
                index += 1

            index = base
            for i in appCompanyLists:
                title = i.get("title")
                href = i.get("href")
                #print "company:", title
                #print "href:", href
                appsListTotal[index].company = title
                appsListTotal[index].company_link = urlGen.get_base_link() + href
                appsList[index-base].company = title
                appsList[index-base].company_link = urlGen.get_base_link() + href
                index += 1

            index = base
            for i in appIconLists:
                icon = i.get("data-cover-large")
                icon_small = i.get("data-cover-small")
                appsListTotal[index].icon = urlGen.get_base_https() + icon
                appsListTotal[index].icon_small = urlGen.get_base_https() + icon_small
                #print icon, icon_small
                appsList[index-base].icon = urlGen.get_base_https() + icon
                appsList[index-base].icon_small = urlGen.get_base_https() + icon_small
                index += 1

            if (callback is not None): #appsList is an catergory app list.
                callback(appsList)

            appsList[:] = []
            count += 1

        except urllib2.HTTPError, e:
            print 'http error:', e.code
            return None
        except urllib2.URLError, e:
            print 'url error:', e.code
            return None

    return appsListTotal

