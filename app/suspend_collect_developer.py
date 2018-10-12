__author__ = 'houhuihua'

import utils,db

def check_new_developer():
    index = 0
    date = utils.getdate()
    appsList = db.get_specail_new_appslist(date)
    print "check_new_developer app new len=", len(appsList)
    for app in appsList:
        dev = db.search_developer(app.company, app.package)
        needupdate = 0
        if dev is None:
            dev = db.search_developer_pkg(app.package)
            if dev is None:
                db.write_developer(app.company, app.company_link, date, app.package)
                print "insert:" , index, app.company, app.company_link, app.package
                needupdate += 1
                #break
        if needupdate == 0:
            db.update_devinfo(dev.company, utils.getdate(), dev.status, app.package, app.company, app.company_link)
            #print dev.company, app.package
            #break
            pass

        #else:
        #    print "exist, index", index, dev.company, app.company_link
        index = index + 1


def update_app_developer():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist(date)
    print "update_app_developer dev len=", devsList.__len__()
    for dev in devsList:
        app = db.search_appinfo(dev.package)
        if app is not None:
            db.update_devinfo(dev.company, utils.getdate(), dev.status, app.package, app.company, app.company_link)
            print "update dev:", index, dev.company, app.package
            break
            index += 1


update_app_developer() #we should update developer first, becase developer maybe changed.
check_new_developer()
