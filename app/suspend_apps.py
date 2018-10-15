__author__ = 'houhuihua'

import db,utils,const

def check_apps_suspend():
    appsList = db.get_specail_old_appslist(utils.getdate())
    index = 0
    print "check_apps_suspend app old len=", len(appsList)
    for app in appsList:
        if app.title.find(const._SUSPEND) == -1:
            status = utils.get_httpstatuscode(app.link.strip('\n'))
            if status != 200:
                print("title:%s %s suspend!" % (app.title, app.link))
                if app.title.find(const._SUSPEND) == -1:
                    app.title = const._SUSPEND  + "[" + utils.getdate() + "]" + app.title
                    db.update_apptitle(app.title, app.package)
                db.update_appdate(utils.getdate(), app.package)
            else:
                db.update_appdate(utils.getdate(), app.package)
                print ("index = %d %s status:%d" % (index, app.title, status))
        index = index + 1


check_apps_suspend()


