#!/usr/local/bin/python2.7
__author__ = 'houhuihua'

import sqlite3

from appinfo import *

_new_flag = '[new!!]'

def connect():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfull.'

'''
def write_appinfo_simple(title, package, company):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("INSERT INTO topapps_list (title, package, company) VALUES (?,?,?);", (title, package, company))
    conn.commit()
    conn.close()
'''
def update_apptitle(title, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_list SET "
              "title=? where package=?", (title, package))
    conn.commit()
    conn.close()

def update_appdate(date, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_list SET "
              "date=? where package=?", (date, package))
    conn.commit()
    conn.close()

def update_devinfo_company_pkg(company, date, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_developer_list SET "
              "date=?, package=?, company=? "
              "where company=?", (date, package, company, company))
    conn.commit()
    conn.close()


def update_devinfo_simple(company, date, status, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_developer_list SET "
              "date=?, status=? , package=?, company=? "
              "where company=?", (date, status, package, company, company))
    conn.commit()
    conn.close()

def update_devinfoex(dev, oldcompany):
    update_devinfo(oldcompany, dev.date, dev.status, dev.package, dev.company, dev.company_link)

def update_devinfo(oldcompany, date, status, package, newcompany, company_link):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_developer_list SET "
              "date=?, status=? , package=?, company=?, company_link=? "
              "where company=?", (date, status, package, newcompany, company_link, oldcompany))
    if cmp(oldcompany, newcompany) != 0:
        print "updage_devinfo:", oldcompany, newcompany

    app = search_appinfo(newcompany)
    '''
    if app is not None:
        print("%s:%s", newcompany, package)
        raise Exception("write company and package errror!!!!")
    '''
    conn.commit()
    conn.close()

def write_appinfo(rank, title, package, link, company, company_link, desc, date, category, icon, icon_small):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("INSERT INTO topapps_list (rank, title, package, link, "
              "company, company_link, desc, date, category, icon_link, icon_link_small) "
              "VALUES (?,?,?,?,?,?,?,?,?,?,?);",
              (rank, title, package, link, company, company_link, desc, date, category, icon, icon_small))
    print "insert appinfo:", title, package
    conn.commit()
    conn.close()

def update_appinfo(rank, title, package, link, company, company_link, desc, date, category, icon, icon_small):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_list SET "
              "rank=?, title=?, package=?, "
              "link=?, company=?, company_link=? ,"
              "desc=?, date=?, category=?, "
              "icon_link=?, icon_link_small=? "
              "WHERE package=?",
              (rank, title, package, link, company, company_link, desc, date, category, icon, icon_small, package))
    #print "update app:", title, package
    conn.commit()
    conn.close()


def write_appchangelogInfo_ex(app):
    write_appchangelogInfo(app.rank, app.title, app.package, app.link, app.company, app.company_link, app.desc, app.date, app.category)

def write_appchangelogInfo(rank, title, package, link, company, company_link, desc, date, category):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("INSERT INTO topapps_changelog_list "
              "(rank, title, package, "
              "link, company, company_link, "
              "desc, date, category) "
              "VALUES (?,?,?,?,?,?,?,?,?);",
              (rank, title, package, link, company, company_link, desc, date, category))
    conn.commit()
    conn.close()

def delete_developer(id):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("DELETE FROM topapps_developer_list where id=?;", (id,))

    #print "write_developer", company, company_link, date, 'ok', package
    conn.commit()
    conn.close()


def write_developer(company, company_link, date, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("INSERT INTO topapps_developer_list "
              "(company_link, date, status, package, company) "
              "VALUES (?,?,?,?,?);", (company_link, date, 'ok', package, company))

    #print "write_developer", company, company_link, date, 'ok', package
    conn.commit()
    conn.close()

def search_developer_pkg(package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select company, company_link, date, status, package from topapps_developer_list where package=?;", (package,))
    for row in result:
        dev = CompanyDetail(row[0], row[1], row[2], row[3], row[4])
        print row
        return dev
    return None

def search_developer(company, package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select company, company_link, date, status, package from topapps_developer_list where company=?;", (company,))
    for row in result:
        dev = CompanyDetail(row[0], row[1], row[2], row[3], row[4])
        #print "find company:",company
        return dev

    '''
    result = c.execute("select company, company_link, date, status, package from topapps_developer_list where package=?;", (package,))
    for row in result:
        dev = CompanyDetail(row[0], row[1], row[2], row[3])
        print row
        return dev
    '''
    #print "not find pkg:", result
    return None

def search_appinfo(package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select rank, title, package, "
                       "link, company, company_link, "
                       "desc, date, category, "
                       "icon_link, icon_link_small "
                       "from topapps_list where package=?;", (package,))
    for row in result:
        app = AppDetail()
        app.rank = row[0]
        app.title = row[1]
        app.package = row[2]
        app.link = row[3]
        app.company = row[4]
        app.company_link = row[5]
        app.desc = row[6]
        app.date = row[7]
        app.category = row[8]
        app.icon = row[9]
        app.icon_small = row[10]
        return app
    return None

def search_partappinfo(package):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select title, package, company, desc, company_link from topapps_list where package=?;", (package,))
    for row in result:
        app = AppDetail()
        app.title = row[0]
        app.package = row[1]
        app.company = row[2]
        app.desc = row[3]
        app.company_link = row[2]
        #print row
        return app

    return None

def check_append_appchangelog_info(app, appold):
    change = False
    title = app.title
    company = app.company
    desc = app.desc

    if cmp(app.title, appold.title) != 0:
        title = app.title + _new_flag + ' from ' + appold.title
        change = True

    if cmp(app.company, appold.company) != 0:
        company = app.company + _new_flag + ' from ' + appold.company
        change = True

    if cmp(app.desc, appold.desc) != 0:
        desc = app.desc + _new_flag + ' from ' + appold.desc
        change = True
    if (change == True):
        write_appchangelogInfo(app.rank, title, app.package,
                              app.link, company, app.company_link,
                              desc, app.date, app.category)

def get_specail_appslist_bydev(company):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select rank, title, package, "
                       "link, company, company_link, "
                       "desc, date, category, "
                       "icon_link, icon_link_small "
                       "from topapps_list where company=?;", (company,))
    appsList = []
    for row in result:
        app = AppDetail()
        app.rank = row[0]
        app.title = row[1]
        app.package = row[2]
        app.link = row[3]
        app.company = row[4]
        app.company_link = row[5]
        app.desc = row[6]
        app.date = row[7]
        app.category = row[8]
        app.icon = row[9]
        app.icon_small = row[10]
        appsList.append(app)
    return appsList


def get_specail_new_appslist(date):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select rank, title, package, "
                       "link, company, company_link, "
                       "desc, date, category, "
                       "icon_link, icon_link_small "
                       "from topapps_list where date=?;", (date,))
    appsList = []
    for row in result:
        app = AppDetail()
        app.rank = row[0]
        app.title = row[1]
        app.package = row[2]
        app.link = row[3]
        app.company = row[4]
        app.company_link = row[5]
        app.desc = row[6]
        app.date = row[7]
        app.category = row[8]
        app.icon = row[9]
        app.icon_small = row[10]
        appsList.append(app)
    return appsList


def get_specail_old_appslist(date):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select rank, title, package, "
                       "link, company, company_link, "
                       "desc, date, category, "
                       "icon_link, icon_link_small "
                       "from topapps_list where date!=?;", (date,))
    appsList = []
    for row in result:
        app = AppDetail()
        app.rank = row[0]
        app.title = row[1]
        app.package = row[2]
        app.link = row[3]
        app.company = row[4]
        app.company_link = row[5]
        app.desc = row[6]
        app.date = row[7]
        app.category = row[8]
        app.icon = row[9]
        app.icon_small = row[10]
        appsList.append(app)
    return appsList

def get_specail_devslist(date):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    result = c.execute("select company, company_link, "
                       " date, status, package "
                       "from topapps_developer_list where date!=?;", (date,))
    devsList = []
    for row in result:
        dev = CompanyDetail(row[0], row[1], row[2], row[3], row[4])
        devsList.append(dev)
    return devsList


def dump():
    conn = sqlite3.connect('topapps')
    #print 'topapps_list'
    #for row in conn.execute("SELECT * FROM topapps_list"):
    #    print row
    print 'topapps_changelog_list'
    for row in conn.execute("SELECT * FROM topapps_changelog_list"):
        print row

def dump_app(callback):
    conn = sqlite3.connect('topapps')
    for row in conn.execute("SELECT title, * FROM topapps_list"):
        if callback is not None:
            callback(row)
        else:
            print row

def dump_changelog():
    conn = sqlite3.connect('topapps')
    for row in conn.execute("SELECT * FROM topapps_changelog_list"):
        print row

def dump_developer(callback):
    conn = sqlite3.connect('topapps')
    for row in conn.execute("SELECT status, * FROM topapps_developer_list"):
        if callback is not None:
            callback(row)
        else:
            print row

def drop_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_list")
        conn.execute("DROP table topapps_changelog_list")
        conn.execute("DROP table topapps_icon_list")
        conn.execute("DROP table topapps_developer_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"

def drop_dev_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_developer_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"

def drop_app_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"

def drop_appchangelog_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_changelog_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"

def drop_icon_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_icon_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"

def create_tables():
    create_app_tables()
    create_appchangelog_tables()
    create_appicon_tables()
    create_developer_tables()

def create_app_tables():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfull.'
    conn.execute('''CREATE TABLE  topapps_list
       (id INTEGER PRIMARY KEY     NOT NULL,
       title           TEXT    NOT NULL,
       rank            TEXT    NOT NULL,
       package         TEXT    NOT NULL,
       date            TEXT    NOT NULL,
       category        TEXT    NOT NULL,
       link            TEXT    NOT NULL,
       desc            TEXT    NOT NULL,
       company         TEXT    NOT NULL,
       icon_link       TEXT    NOT NULL,
       icon_link_small TEXT    NOT NULL,
       company_link    TEXT    NOT NULL
       );''')
    print "app table created successfully"
    conn.commit()
    conn.close()

def create_appicon_tables():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfull.'
    conn.execute('''CREATE TABLE  topapps_icon_list
       (id INTEGER PRIMARY KEY     NOT NULL,
       package         TEXT    NOT NULL,
       date            TEXT    NOT NULL,
       icon_data       BLOB
       );''')
    print "app icon table created successfully."
    conn.commit()
    conn.close()


def create_appchangelog_tables():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfully.'

    conn.execute('''CREATE TABLE  topapps_changelog_list
       (id INTEGER PRIMARY KEY     NOT NULL,
       title           TEXT    NOT NULL,
       rank            TEXT    NOT NULL,
       package         TEXT    NOT NULL,
       date            TEXT    NOT NULL,
       category        TEXT    NOT NULL,
       link            TEXT    NOT NULL,
       desc            TEXT    NOT NULL,
       company         TEXT    NOT NULL,
       company_link    TEXT    NOT NULL
       );''')
    print "app changelog table created successfully"
    conn.commit()
    conn.close()

def create_developer_tables():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfull.'
    conn.execute('''CREATE TABLE  topapps_developer_list
       (id INTEGER PRIMARY KEY     NOT NULL,
       date            TEXT    NOT NULL,
       status          TEXT    NOT NULL,
       package         TEXT    NOT NULL,
       company         TEXT,
       company_link    TEXT    NOT NULL
       );''')
    print "app developer table created successfully"
    conn.commit()
    conn.close()


