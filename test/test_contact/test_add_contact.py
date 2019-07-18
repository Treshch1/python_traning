# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db):
    old_contacts = db.get_contact_list()
    contact = Contact(first_name="first name", middle_name="middle name", last_name="last name",
                      nickname="nickname", title="title", company="company", address="address",
                      home="home", mobile="mobile", work="work", fax="fax", email="email", email_2="email2",
                      email_3="email3", homepage="homepage", bday='3', bmonth="March", byear="1997",
                      aday='3', amonth="April", ayear="2016", secondary_address="secondary address",
                      secondary_home="secondary_home", notes="notes")
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
