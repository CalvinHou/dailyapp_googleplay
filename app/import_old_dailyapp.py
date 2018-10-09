__author__ = 'houhuihua'

import db, utils
import sqlite3
from appinfo import *

global cc
cc = 0

def write_app(row):
    global cc
    i = AppDetail()
    i.rank = row[0]
    i.title = row[1]
    i.link = row[2]
    i.package = row[3]
    i.company= row[4]
    i.company_link= row[5]
    i.desc = row[6]
    i.date = row[7]
    i.category = row[8]
    i.icon = row[9]
    i.icon_small = row[10]

    date = utils.getdate()
    app = db.search_partappinfo(i.package)
    dev = db.search_developer(i.company, i.package)
    cc += 1
    if dev is None: #maybe this package is not relative with dev.
        pass
    else:
        db.update_devinfo(dev.company, date, dev.status, i.package, i.company, i.company_link)

    if app is None:
        db.write_appinfo(i.rank, i.title, i.package,
                         i.link, i.company, i.company_link,
                         i.desc, utils.getdate(), i.category,
                         i.icon, i.icon_small)
    '''
    else:
        db.check_append_appchangelog_info(i, app)
        db.update_appinfo(i.rank, i.title, i.package,
                          i.link, i.company, i.company_link,
                          i.desc, utils.getdate(), i.category,
                          i.icon, i.icon_small)
    '''

    print "write app:", cc, i.title, i.package


def write_app_changelog(row):
    global cc
    i = AppDetail()
    i.rank = row[0]
    i.title = row[1]
    #i.link = row[2]
    i.package = row[2]
    i.company= row[3]
    i.desc = row[4]
    i.date = row[5]
    i.category = row[6]

    cc+=1
    date = utils.getdate()
    app = db.search_partappinfo(i.package)
    if app is not None and cc ==1:
        i.link = app.link
        i.company_link = app.company_link
        if i.title.find("new!!") != -1 or i.company.find("new!!") != -1 or i.desc.find("new!!") != -1:
            db.write_appchangelogInfo_ex(i)
            print "update appchangelog :", cc, i.title, i.package, i.company, i.desc

    #if i.title.find("new!!") != -1 or i.company.find("new!!") != -1 or i.desc.find("new!!") != -1:
    #    print "update appchangelog :", cc, i.title, i.package, i.company, i.desc

def write_app_developer(row):
    global cc
    cc+=1

    i = CompanyDetail(row[2], "", row[1], row[3], row[0])

    company = db.search_developer(i.company, "xxxxx")
    if company is not None:
        pass
        print "upate dev:", cc, i.status, company.package, i.date, company.company, company.company_link
        db.update_devinfo(i.company, i.date, i.status, company.package, company.company, company.company_link)

def dump_app(callback):
    conn = sqlite3.connect('topapp_rank')
    for row in conn.execute("SELECT rank, title, link, package, company, company_link, desc, date, category, icon_link, icon_link_small FROM topapps_list"):
        if callback is not None:
            callback(row)
        else:
            print row

def dump_appchangelog(callback):
    conn = sqlite3.connect('topapp_rank')
    count = 0
    for row in conn.execute("SELECT rank, title, package, company, desc, date, category FROM topapps_changelog_list"):
        count +=1
        if callback is not None:
            callback(row)
        else:
            print row
    print "changelog:", count

def dump_app_developer(callback):
    conn = sqlite3.connect('topapp_rank')
    for row in conn.execute("SELECT url,date, category, status FROM categories_list"):
        if callback is not None:
            callback(row)
        else:
            print row


#dump_app(write_app)
#dump_appchangelog(write_app_changelog)
#dump_app_developer(write_app_developer)

