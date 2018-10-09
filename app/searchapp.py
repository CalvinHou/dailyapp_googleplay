__author__ = 'houhuihua'

import db,utils

app = db.search_appinfo("io.makeroid.antonio_aguilar_es.fondos05")
if app is not None:
    status = utils.get_httpstatuscode(app.link.strip('\n'))
    print "app status:", status
