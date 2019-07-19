from model.group import Group
from model.contact import Contact


def test_add_group_to_contact(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='new group name'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name"))
    available_items = orm.get_available_contact_and_group()
    if not available_items:
        app.contact.create(Contact(first_name="first name"))
        available_items = orm.get_available_contact_and_group()
    contact = available_items["contact"]
    group = available_items["group"]
    assert not orm.is_contact_in_group(contact, group)
    app.contact.add_group_to_contact(contact, group)
    assert orm.is_contact_in_group(contact, group)
