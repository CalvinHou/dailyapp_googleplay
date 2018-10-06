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

def write_appinfo(rank, title, package, link, company, company_link, desc, date, category, icon, icon_small):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("INSERT INTO topapps_list (rank, title, package, link, "
              "company, company_link, desc, date, category, icon_link, icon_link_small) "
              "VALUES (?,?,?,?,?,?,?,?,?,?,?);",
              (rank, title, package, link, company, company_link, desc, date, category, icon, icon_small))
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
              (rank, title, package, link, company, company_link, desc, date, category, package, icon, icon_small))
    conn.commit()
    conn.close()


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
    result = c.execute("select title, package, company, desc from topapps_list where package=?;", (package,))
    for row in result:
        app = AppDetail()
        app.title = row[0]
        app.package = row[1]
        app.company = row[2]
        app.desc = row[3]
        print row
        return app

    return None

def check_append_appchangelog_info(app, appnew):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    change = False

    if (cmp(app.title, appnew.title) != 0):
        appnew.title = app.title + _new_flag + ' to ' + appnew.title
        change = True

    if (cmp(app.company, appnew.company) != 0):
        appnew.company = app.company + _new_flag + ' to ' + appnew.company
        change = True

    if (cmp(app.desc, appnew.desc) != 0):
        appnew.desc = app.desc + _new_flag + ' to ' + appnew.desc
        change = True
    if (change == True):
        write_appchangelogInfo(appnew.rank, appnew.title, appnew.package,
                              appnew.link, appnew.company, appnew.company_link,
                              appnew.desc, appnew.date, appnew.category)


def dump():
    conn = sqlite3.connect('topapps')
    print 'topapps_list'
    for row in conn.execute("SELECT * FROM topapps_list"):
        print row
    print 'topapps_changelog_list'
    for row in conn.execute("SELECT * FROM topapps_changelog_list"):
        print row

def dump_changelog():
    conn = sqlite3.connect('topapps')
    for row in conn.execute("SELECT * FROM topapps_changelog_list"):
        print row

def drop_tables():
    conn = sqlite3.connect('topapps')
    try:
        conn.execute("DROP table topapps_list")
        conn.execute("DROP table topapps_changelog_list")
        conn.execute("DROP table topapps_icon_list")
    except sqlite3.OperationalError:
        print "sqlite3.OperationalError: table not exist!"


def create_tables():
    create_app_tables()
    create_appchangelog_tables()
    create_appicon_tables()

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
    print "app icon table created successfully"
    conn.commit()
    conn.close()


def create_appchangelog_tables():
    conn = sqlite3.connect('topapps')
    print 'connect top apps successfull.'

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

