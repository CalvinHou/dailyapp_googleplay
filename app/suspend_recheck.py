__author__ = 'houhuihua'

import utils,const,db


def force_check_suspended_developer():
    index = 0
    date = utils.getdate()
    devsList = db.get_specail_devslist("xxxx")
    print "force_check_suspended_developer dev len=", devsList.__len__()
    for dev in devsList:
        if dev.status == const.SUSPEND_STATUS:
            req = utils.get_httpstatus_request(dev.company_link.strip('\n'))
            if req.content is not None:
                error = req.content.find('We\'re sorry, the requested URL was not found on this server.')
                #print("dev:%s %s %s, %s, suspend!" % (dev.company, dev.company_link, error, req.content.__len__()))
                if error == -1:
                    dev_status = const.OK_STATUS
                    print ("index = %d %s status:%s" % (index, dev.company, dev_status))
                else:
                    dev_status = const.SUSPEND_STATUS
            elif req.status_code == 404:
                dev_status = const.SUSPEND_STATUS
            #db.update_devinfo_simple(dev.company, utils.getdate(), dev_status, dev.package)
            index = index + 1
force_check_suspended_developer();
