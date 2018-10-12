__author__ = 'houhuihua'
import db


def test_update_dev():
    app = db.search_appinfo("com.mfa.filemanager")
    db.update_devinfo(app.company, app.date, "ok", app.package, app.company, app.company_link)
    db.update_devinfo_company_pkg(app.company, app.date, app.package)
    db.update_devinfo_simple(app.company, app.date, "ok", app.package)


test_update_dev()
