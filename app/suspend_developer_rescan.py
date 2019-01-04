__author__ = 'houhuihua'

import db


def rescan_developers():
    dict = db.search_not_insert_dev()
    index = 0
    print "rescan_developers dev len=", dict.__len__()
    for key, value in dict.items():
        db.write_developer(value.company, value.company_link, value.date, value.package)
        index = index + 1
        print index, value.company, value.date

def delete_dup_developers():
    devsList = db.get_specail_devslist('xxx')
    dict = {}
    print 'delete before:', devsList.__len__()
    for dev in devsList:
        if dev.company_link not in dict.keys():
            dict[dev.company_link] = dev.package
        else:
            print 'exist:', dev.company, dev.company_link
            db.delete_developer(dev.id)
        dict[dev.company_link] = dev.package
    print 'delete after:', dict.__len__()

rescan_developers()
delete_dup_developers()

