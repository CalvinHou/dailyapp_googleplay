__author__ = 'houhuihua'

_base_pkg_url = "https://play.google.com/"
_base_url = "https://play.google.com/store/apps/category/"
_top_tail = "/collection/topselling_free"
_new_top_tail = "/collection/topselling_new_free"

class CategoryDetail:
    url = ""
    name = ""

    def __init__(self, url, name):
        self.url = url
        self.name = name


class AppDetail:
    rank = 0
    title = ""
    link = ""
    package = ""
    company = ""
    company_link = ""
    desc = ""
    icon = ""
    icon_small = ""
    category = ""
    date = ""

'''
    def __init__(self):
        print "init AppDetail"

    def __init__(self, rank, title, package, link, company, company_link, desc, icon, icon_small, category, date):
       self.rank = rank
       self.title = title
       self.link = link
       self.package = package
       self.company = company
       self.company_link = company_link
       self.category = category
       self.icon = icon
       self.icon_small = icon_small
       self.desc = desc
       self.date = date
'''

class UrlGen:
    def get_base_link(self):
        return _base_pkg_url

    def get_all_categories(self):
        all = []
        categories = ["PERSONALIZATION", "MUSIC_AND_AUDIO", "COMMUNICATION", "PRODUCTIVITY", "ENTERTAINMENT", "TOOLS", "SOCIAL", "VIDEO_PLAYERS",
                      "PHOTOGRAPHY", "TRAVEL_AND_LOCAL", "LIFESTYLE", "GAME_TRIVIA", "SPORTS", "MAPS_AND_NAVIGATION", "EDUCATION"]
        #categories = ["PERSONALIZATION"]
        for i in categories:
            top = CategoryDetail(_base_url + i + _top_tail + '?start=0&num=120', i.lower())
            top2 = CategoryDetail(_base_url + i + _top_tail + '?start=120&num=120', i.lower())
            top_new = CategoryDetail(_base_url + i + _new_top_tail + "?start=0&num=120", (i + "_new").lower())
            top_new2 = CategoryDetail(_base_url + i + _new_top_tail + "?start=120&num=120", (i + "_new").lower())
            all.append(top)
            all.append(top2)
            all.append(top_new)
            all.append(top_new2)

        print "all url len=", all.__len__()
        return all




