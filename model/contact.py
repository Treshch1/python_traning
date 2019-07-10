from sys import maxsize


class Contact:

    def __init__(self, amonth=None, aday=None, byear=None, bmonth=None, bday=None, homepage=None, email_3=None,
                 email_2=None, email=None, fax=None, work=None, mobile=None, home=None, address=None, company=None,
                 title=None, nickname=None, last_name=None, middle_name=None, first_name=None, ayear=None,
                 secondary_address=None, notes=None, secondary_home=None, id=None, all_phones_from_home_page=None):
        self.amonth = amonth
        self.aday = aday
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.homepage = homepage
        self.email_3 = email_3
        self.email_2 = email_2
        self.email = email
        self.fax = fax
        self.work = work
        self.mobile = mobile
        self.home = home
        self.address = address
        self.company = company
        self.title = title
        self.nickname = nickname
        self.last_name = last_name
        self.middle_name = middle_name
        self.first_name = first_name
        self.ayear = ayear
        self.secondary_address = secondary_address
        self.notes = notes
        self.secondary_home = secondary_home
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return f"{self.id}, {self.first_name}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
