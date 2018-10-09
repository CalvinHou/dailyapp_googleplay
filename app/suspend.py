__author__ = 'houhuihua'

import db,utils
from appinfo import *

_SUSPEND = "[suspend]:"
OK_STATUS = "ok"
SUSPEND_STATUS = "suspend"

def check_apps_suspend():
    appsList = db.get_specail_old_appslist(utils.getdate())
    index = 0
    print "check_apps_suspend app old len=", len(appsList)
    for app in appsList:
        status = utils.get_httpstatuscode(app.link.strip('\n'))
        if status != 200:
            print("title:%s %s suspend!" % (app.title, app.link))
            if app.title.find(_SUSPEND) == -1:
                app.title = _SUSPEND  + "[" + utils.getdate() + "]" + app.title
                db.update_apptitle(app.title, app.package)
            db.update_appdate(utils.getdate(), app.package)
        else:
            db.update_appdate(utils.getdate(), app.package)
            print ("index = %d %s status:%d" % (index, app.title, status))
        index = index + 1


def check_new_developer():
    index = 0
    date = utils.getdate()
    appsList = db.get_specail_new_appslist(date)
    print "check_new_developer app new len=", len(appsList)
    for app in appsList:
        dev = db.search_developer(app.company, app.package)
        if dev is None:
            db.write_developer(app.company, app.company_link, date, app.package)
            print "insert:" , index, app.company, app.company_link, app.package
        else:
            db.update_devinfo(dev.company, utils.getdate(), dev.status, app.package, app.company, app.company_link)
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
            print "update dev:", index, dev.company, app.company
            index += 1


def check_app_developer_suspend():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist(date)
    print "check_app_developer_suspend dev len=", devsList.__len__()
    for dev in devsList:
        if dev.date != date and dev.status != SUSPEND_STATUS:
        #if dev.status != SUSPEND_STATUS:
            status = utils.get_httpstatuscode(dev.company_link.strip('\n'))
            if status != 200:
                print("dev:%s %s suspend!" % (dev.company, dev.company_link))
                dev_status = SUSPEND_STATUS
            else:
                dev_status = OK_STATUS
            db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            print ("index = %d %s status:%d" % (index, dev.company, status))
            index = index + 1

def force_check_suspended_developer():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist("xxxx")
    print "force_check_suspended_developer dev len=", devsList.__len__()
    for dev in devsList:
        if dev.status == SUSPEND_STATUS:
            #if dev.status != SUSPEND_STATUS:
            status = utils.get_httpstatuscode(dev.company_link.strip('\n'))
            if status != 200:
                print("dev:%s %s suspend!" % (dev.company, dev.company_link))
                dev_status = SUSPEND_STATUS
            else:
                dev_status = OK_STATUS
            db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            print ("index = %d %s status:%d" % (index, dev.company, status))
            index = index + 1

force_check_suspended_developer()
update_app_developer()
check_new_developer()
check_app_developer_suspend()
check_apps_suspend()
#db.dump_developer()
#db.dump_app()

