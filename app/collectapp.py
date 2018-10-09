__author__ = 'houhuihua'

import db
import utils
import parseapp
from appinfo import *


def save_app_to_list(appslist):
    cc = 0
    date = utils.getdate()
    if len(appslist) > 0:
        print appslist[0].category
    for i in appslist:
        i.package = utils.get_package(i.link)

        app = db.search_partappinfo(i.package)
        dev = db.search_developer(i.company, i.package)
        cc += 1
        if dev is None: #maybe this package is not relative with dev.
            pass
        else:
            db.update_devinfo(dev.company, date, dev.status, i.package, i.company, i.company_link)

        if app is None:
            db.write_appinfo(i.rank, i.title, i.package,
                             i.link, i.company, i.company_link,
                             i.desc, utils.getdate(), i.category,
                             i.icon, i.icon_small)
        else:
            db.check_append_appchangelog_info(i, app)
            db.update_appinfo(i.rank, i.title, i.package,
                              i.link, i.company, i.company_link,
                              i.desc, utils.getdate(), i.category,
                              i.icon, i.icon_small)

def collect_all_apps():
    urlGen = UrlGen()
    allCategories = urlGen.get_all_categories()
    appsList = parseapp.parse_all_apps(allCategories, save_app_to_list)

    return appsList

print utils.getdatedetail()
collect_all_apps()
#db.dump_app()
