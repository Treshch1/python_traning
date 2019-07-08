from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name="first name", middle_name="middle name", last_name="last name",
                                           nickname="nickname", title="title", company="company", address="address",
                                           home="home", mobile="mobile", work="work", fax="fax", email="email",
                                           email_2="email2", email_3="email3", homepage="homepage", bday='3',
                                           bmonth="March", byear="1997", aday='3', amonth="April", ayear="2016",
                                           secondary_address="secondary address", secondary_home="secondary home",
                                           notes="notes"))