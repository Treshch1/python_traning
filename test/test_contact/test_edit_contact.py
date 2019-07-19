from model.contact import Contact
import random


def test_edit_first_contact(app, db):
    if  len(db.get_contact_list())== 0:
        app.contact.create(Contact(first_name="first name"))
    old_contacts = db.get_contact_list()
    editable_contact = random.choice(old_contacts)
    contact = Contact(first_name="first name", middle_name="middle name", last_name="last name",
                      nickname="nickname", title="title", company="company", address="address",
                      home="home", mobile="mobile", work="work", fax="fax", email="email",
                      email_2="email2", email_3="email3", homepage="homepage", bday='3',
                      bmonth="March", byear="1997", aday='3', amonth="April", ayear="2016",
                      secondary_address="secondary address", secondary_home="secondary_home",
                      notes="notes")
    contact.id = editable_contact.id
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(editable_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
