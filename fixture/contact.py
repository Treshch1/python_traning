from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_back_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_create_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.go_back_to_home_page()
        self.contact_cache = None

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_edit_contact_page_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_edit_contact_page_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.go_back_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_text_value("firstname", contact.first_name)
        self.change_text_value("middlename", contact.middle_name)
        self.change_text_value("lastname", contact.last_name)
        self.change_text_value("nickname", contact.nickname)
        self.change_text_value("title", contact.title)
        self.change_text_value("company", contact.company)
        self.change_text_value("address", contact.address)
        self.change_text_value("home", contact.home)
        self.change_text_value("mobile", contact.mobile)
        self.change_text_value("work", contact.work)
        self.change_text_value("fax", contact.fax)
        self.change_text_value("email", contact.email)
        self.change_text_value("email2", contact.email_2)
        self.change_text_value("email3", contact.email_3)
        self.change_text_value("homepage", contact.homepage)
        self.fill_with_choice("bday", contact.bday, 1)
        self.fill_with_choice("bmonth", contact.bmonth, 1)
        self.change_text_value("byear", contact.byear)
        self.fill_with_choice("aday", contact.aday, 2)
        self.fill_with_choice("amonth", contact.amonth, 2)
        self.change_text_value("ayear", contact.ayear)
        self.change_text_value("address2", contact.secondary_address)
        self.change_text_value("phone2", contact.secondary_home)
        self.change_text_value("notes", contact.notes)

    def fill_with_choice(self, field_name,  choice, sequence_number=None):
        wd = self.app.wd
        if choice is not None:
            if field_name in ["bmonth", "amonth"]:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_xpath(f"(//option[.='{choice}'])[{sequence_number}]").click()
            else:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_xpath(f"(//option[@value='{choice}'])[{sequence_number}]").click()

    def change_text_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                last_name = element.find_elements_by_xpath(".//td")[1].text
                first_name = element.find_elements_by_xpath(".//td")[2].text
                all_phones= element.find_elements_by_xpath(".//td")[5].text
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                                                  all_phones_from_home_page=all_phones))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_contact_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id,
                       home=homephone, work=workphone,
                       mobile=mobilephone, secondary_home=secondaryphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        details = wd.find_elements_by_xpath("//tr[@name='entry']//td[7]//img")[index]
        details.click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondary_home = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work,
                       mobile=mobile, secondary_home=secondary_home)
