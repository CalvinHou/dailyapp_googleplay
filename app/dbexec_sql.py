__author__ = 'houhuihua'
import db
import sys
import sqlite3

class DevId:
    id = 0
    company = ""

    def __init__(self, c, id):
        self.company = c
        self.id = id


class Dev:
    company = ""
    package = ""

    def __init__(self, c, p):
        self.company = c
        self.p = p

global companyList
companyList = []

def update_devinfo_simple(conn, company, package, search):
    conn = sqlite3.connect('topapps')
    c = conn.cursor()
    c.execute("UPDATE topapps_developer_list SET "
              "package=?, company=? "
              "where company=?", (company, package, search))
    conn.commit()
    conn.close()

def search_error_company(row):
    app = db.search_appinfo(row[0])
    i = 0
    if app is not None:
        print "i:", i, row
        dev = Dev(row[0], row[1])
        companyList.append(dev)
        i +=1

    for dev in companyList:
        print dev
        update_devinfo_simple(dev.company, dev.package, dev.company)
        break

def db_exec_sql(callback, sql):
    conn = sqlite3.connect('topapps')
    print sys.argv[1]

    result = conn.execute(sql)
    ii = 0

    '''
    for row in result:
        ii +=1
        if callback is not None:
            callback(row)
        else:
            #print ii, row
            pass
    '''

    cc = 0
    print cc
    i1 = 0
    sameList = []

    result3 = []
    result2 = conn.execute(sql)
    for row in result2:
        result3.append(row[0])

    result2
    '''
    for i in result:
        i2 = 0
        #result2 = conn.execute(sql)
        for j in result3:
            if i1 != i2 and cmp(i[0], j) == 0:
                print "same", cc, i[2]
                sameList.append(i[2])
                cc +=1
            i2 += 1
        print "ove one"
        i1 +=1

    print "total cc:", cc
    '''
    appsList = []
    i = 0
    cc = 0
    for row in result:
        app = db.search_appinfo(row[0])
        if app is not None:
            #db.update_devinfo_company_pkg(app.company, app.date, app.package)
            appsList.append(app)
            print i, row[0], app.company
            i +=1
        cc +=1
        print cc, i

    conn.commit()
    conn.close()

    for app in appsList:
        print "update", app.company
        db.update_devinfo_company_pkg(app.company, app.date, app.package)

    #for i in sameList:
    #    db.delete_developer(i)
    #    pass


#db.delete_developer(12871)
db_exec_sql(None, sys.argv[1])
#print sys.argv[1]
