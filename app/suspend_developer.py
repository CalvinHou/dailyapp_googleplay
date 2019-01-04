__author__ = 'houhuihua'
import db,utils,const


def check_app_developer_suspend():
    index = 0
    date = utils.getdate()
    yesterday = utils.getdate()
    devsList = db.get_specail_devslist_ex(date, yesterday)
    print "check_app_developer_suspend dev len=", devsList.__len__()
    for dev in devsList:
        if cmp(dev.date, date) != 0 and cmp(dev.status, const.OK_STATUS) == 0:
            #if dev.status != SUSPEND_STATUS:

            req = utils.get_httpstatus_request(dev.company_link.strip('\n'))
            if req.content is not None:
                error = req.content.find('We\'re sorry, the requested URL was not found on this server.')
                if error == -1:
                    dev_status = const.OK_STATUS
                    #print ("index = %d %s status:%s" % (index, dev.company, dev_status))
                else:
                    dev_status = const.SUSPEND_STATUS
                    print("dev:%s %s suspend!" % (dev.company, dev.company_link))
                    appsList = db.get_specail_appslist_bydev(dev.company)
                    for app in appsList:
                        if app.title.find(const._SUSPEND) == -1:
                            app.title = const._SUSPEND  + "[" + utils.getdate() + "]" + app.title
                            db.update_apptitle(app.title, app.package)
                            print("\t [dead now]title:%s %s suspend!" % (app.title, app.link))
                        else:
                            print("\t [dead ago]title:%s %s suspend!" % (app.title, app.link))

            elif req.status_code == 404:
                dev_status = const.SUSPEND_STATUS

            db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            index = index + 1


check_app_developer_suspend()

