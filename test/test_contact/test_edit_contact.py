from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first name"))
        old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first name", middle_name="middle name", last_name="last name",
                                           nickname="nickname", title="title", company="company", address="address",
                                           home="home", mobile="mobile", work="work", fax="fax", email="email",
                                           email_2="email2", email_3="email3", homepage="homepage", bday='3',
                                           bmonth="March", byear="1997", aday='3', amonth="April", ayear="2016",
                                           secondary_address="secondary address", secondary_home="secondary home",
                                           notes="notes")
    contact_id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[-1] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)