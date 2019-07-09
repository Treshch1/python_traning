from model.contact import Contact


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

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_edit_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_edit_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.go_back_to_home_page()

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

    def get_contact_list(self):
        wd = self.app.wd
        self.go_to_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            first_name = element.find_elements_by_xpath("//td")[1].text
            last_name = element.find_elements_by_xpath("//td")[2].text
            contacts.append(Contact(id=id, first_name=first_name, last_name=last_name))
        return contacts
