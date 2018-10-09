__author__ = 'houhuihua'
__date__ = '2018.10.05'

import db
import collectapp


#initDb()
appsList = collectapp.collect_all_apps()
db.dump()

if appsList.__len__() <= 0:
    print "len = 0"
else:
    print ("len = %d, app count = %d" % (appsList.__len__(), cc))

print "Great, we collect app info over..."

