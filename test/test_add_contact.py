# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.create_contact(Contact(first_name="first name", middle_name="middle name", last_name="last name",
                   nickname="nickname", title="title", company="company", address="address", home="home",
                   mobile="mobile", work="work", fax="fax", email="email", email_2="email2", email_3="email3",
                   homepage="homepage", bday='3', bmonth="March", byear="1997", aday='3', amonth="April", ayear="2016",
                   secondary_address="secondary address", secondary_home="secondary home", notes="notes"))
    app.session.logout()
