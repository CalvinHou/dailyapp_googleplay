__author__ = 'houhuihua'
__date__ = '2018.10.05'

import db
import utils
import parseapp


def initDb():
    #db.drop_tables()
    db.create_tables()

initDb()
appsList = parseapp.parse_all_apps()
cc = 0
for i in appsList:
    #print i.title, i.link, i.company, i.company_link, i.desc
    i.package = utils.get_package(i.link)
    i.rank = utils.get_app_rank(i.title)

    app = db.search_partappinfo(i.package)
    cc = cc + 1
    if (app == None):
        db.write_appinfo(i.rank, i.title, i.package,
                         i.link, i.company, i.company_link,
                         i.desc, utils.getDate(), i.category,
                         i.icon, i.icon_small)
    else:
        db.check_append_appchangelog_info(i, app)
        db.update_appinfo(i.rank, i.title, i.package,
                          i.link, i.company, i.company_link,
                          i.desc, utils.getDate(), i.category,
                          i.icon, i.icon_small)
db.dump()

if appsList.__len__() <= 0:
    print "len = 0"
else:
    print ("len = %d, app count = %d" % (appsList.__len__(), cc))

print "Great, we collect app info over..."

