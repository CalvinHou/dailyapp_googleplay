__author__ = 'houhuihua'

import db
import utils
import parseapp
from appinfo import *


def collect_all_apps():
    urlGen = UrlGen()
    allCategories = urlGen.get_test_categories()
    appsList = parseapp.parse_all_apps(allCategories, None)
    cc = 0
    for i in appsList:
        i.package = utils.get_package(i.link)

        app = db.search_partappinfo(i.package)
        dev = db.search_developer(i.company, i.package)
        cc = cc + 1

        if dev is None: #maybe this package is not relative with dev.
            pass
        else:
            db.update_devinfo(dev.company, utils.getdate(), dev.status, i.package, i.company, i.company_link)

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

    return appsList

print utils.getdatedetail()
collect_all_apps()
#db.dump_app()
