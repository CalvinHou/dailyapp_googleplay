__author__ = 'houhuihua'

import urllib2
import utils

from bs4 import BeautifulSoup
from appinfo import *


def parse_all_apps():
    appsList = []
    urlGen = UrlGen()
    allCategories = urlGen.get_all_categories()
    for url in allCategories:
        try:
            htmlTxt = urllib2.urlopen(url.url).read()
            print "url=, len=", url.name, url.url, len(htmlTxt)
            soup = BeautifulSoup(htmlTxt, 'html.parser')
            appTitleLists = soup.select("div.details > a.title")
            appDescLists = soup.select("div.details > div.description")
            appCompanyLists = soup.select("div.details > div.subtitle-container > a.subtitle")
            appIconLists = soup.select("div.cover-inner-align > img.cover-image")

            for i in appTitleLists:
                text = i.get_text()
                href = i.get("href")
                rank = utils.get_app_rank(text)
                #print "title:", text
                #print "href:", href
                app = AppDetail()
                app.title = i.get("title")
                app.link = urlGen.get_base_link() + href
                app.category = url.name
                appsList.append(app)


            index = 0
            for i in appDescLists:
                desc = i.get_text()
                #print "desc:", desc
                appsList.__getitem__(index).desc = desc
                index = index + 1

            index = 0
            for i in appCompanyLists:
                title = i.get_text()
                href = i.get("href")
                #print "company:", title
                #print "href:", href
                appsList.__getitem__(index).company = title
                appsList.__getitem__(index).company_link = urlGen.get_base_link() + href
                index = index + 1

            index = 0
            for i in appIconLists:
                icon = i.get("data-cover-large")
                icon_small = i.get("data-cover-small")
                appsList.__getitem__(index).icon = icon
                appsList.__getitem__(index).icon_small = icon_small
                #print icon, icon_small
                index = index + 1
        except urllib2.HTTPError, e:
            print 'http error:', e.code
            return None
        except urllib2.URLError, e:
            print 'url error:', e.code
            return None

    return appsList

