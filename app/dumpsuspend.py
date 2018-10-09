__author__ = 'houhuihua'

import db
#import suspend

global index
index = 0

def output_suspend_apps(row):
    if row[0].find("suspend") != -1:
        global index
        print index, row[0]
        index += 1

def output_suspend_developers(row):
    if row[0].find("suspend") != -1:
        global index
        print index, row
        index += 1

print "suspend app:"
db.dump_app(output_suspend_apps)
index = 0
print "suspend dev:"
db.dump_developer(output_suspend_developers)
#db.dump_developer(None)
