__author__ = 'houhuihua'

import utils,const,db


def force_check_suspended_developer():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist("xxxx")
    print "force_check_suspended_developer dev len=", devsList.__len__()
    for dev in devsList:
        if dev.status == const.SUSPEND_STATUS:
            #if dev.status != SUSPEND_STATUS:
            status = utils.get_httpstatuscode(dev.company_link.strip('\n'))
            if status != 200:
                print("dev:%s %s suspend!" % (dev.company, dev.company_link))
                dev_status = const.SUSPEND_STATUS
            else:
                dev_status = const.OK_STATUS
            db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            print ("index = %d %s status:%d" % (index, dev.company, status))
            index = index + 1
