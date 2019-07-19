import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=username, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id, first_name, last_name = row
                contact_list.append(Contact(id=str(id), first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()

    def get_contact_list_phones(self):
        contact_list_phones = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, home, mobile, work, phone2 from "
                           + "addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id, home, mobile, work, phone2 = row
                contact_list_phones.append(Contact(id=str(id), home=home, mobile=mobile, work=work, secondary_home=phone2))
        finally:
            cursor.close()
        return contact_list_phones
