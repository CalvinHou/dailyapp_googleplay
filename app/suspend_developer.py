__author__ = 'houhuihua'
import db,utils,const


def check_app_developer_suspend():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist(date)
    print "check_app_developer_suspend dev len=", devsList.__len__()
    for dev in devsList:
        if cmp(dev.date, date) != 0 and cmp(dev.status, const.OK_STATUS) == 0:
            #if dev.status != SUSPEND_STATUS:
            status = utils.get_httpstatuscode(dev.company_link.strip('\n'))
            if status != 200:
                print("dev:%s %s suspend!" % (dev.company, dev.company_link))
                dev_status = const.SUSPEND_STATUS
                appsList = db.get_specail_appslist_bydev(dev.company)
                for app in appsList:
                    if app.title.find(const._SUSPEND) == -1:
                        app.title = const._SUSPEND  + "[" + utils.getdate() + "]" + app.title
                        db.update_apptitle(app.title, app.package)
                        print("\t [dead now]title:%s %s suspend!" % (app.title, app.link))
                    else:
                        print("\t [dead ago]title:%s %s suspend!" % (app.title, app.link))
            else:
                dev_status = const.OK_STATUS
            db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            #print ("dev:index = %d %s status:%d" % (index, dev.company, status))
            index = index + 1


check_app_developer_suspend()

