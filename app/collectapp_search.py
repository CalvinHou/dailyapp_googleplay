#!/usr/local/bin/python2.7
__author__ = 'houhuihua'

import db
import utils
import parseapp
from appinfo import *
import requests



def save_app_to_list(appslist):
    cc = 0
    date = utils.getdate()
    #if len(appslist) > 0:
    #    print appslist[0].category
    for i in appslist:
        i.package = utils.get_package(i.link)

        app = db.search_partappinfo(i.package)
        dev = db.search_developer(i.company, i.package)
        cc += 1
        if dev is None: #maybe this package is not relative with dev.
            pass
        else:
            db.update_devinfo(dev.company, date, dev.status, i.package, i.company, i.company_link)
            #if dev is not None and cmp(dev.date, date) != 0:
            #    print "update dev:", i.company, i.company_link, dev.date, date

        if app is None:
            db.write_appinfo(i.rank, i.title, i.package,
                             i.link, i.company, i.company_link,
                             i.desc, utils.getdate(), i.category,
                             i.icon, i.icon_small)
        else:
            i.date = date
            db.check_append_appchangelog_info(i, app)
            db.update_appinfo(i.rank, i.title, i.package,
                              i.link, i.company, i.company_link,
                              i.desc, utils.getdate(), i.category,
                              i.icon, i.icon_small)
        print cc, i.title, i.package

def collect_all_apps():
    urlGen = UrlGen()
    allCategories = urlGen.get_search_url()
    appsList = parseapp.parse_all_apps(allCategories, save_app_to_list)

    return appsList


def collect_next_page():
    url = "https://play.google.com/store/apps/collection/search_results_cluster_apps?authuser=0"
    r = requests.post(url, data = {
        'start':'0',
        'num':'0',
        'numChildren':'0',
        'pagTok':'-p6BnQMCCDE=:S:ANO1ljJ4Cw8',
        'clp':'ggEJCgNzbXMaAggA:S:ANO1ljIKuaM',
        'pagtt':'3',
        'cctcss':'square-cover',
        'cllayout':'NORMAL',
        'ipf':'1',
        'xhr':'1'
    })
    print r.content
    return r.content

print utils.getdatedetail()
#collect_all_apps()
html = collect_next_page()
appsList = parseapp.parse_html_apps(html, save_app_to_list, "test url", "search-sms")
