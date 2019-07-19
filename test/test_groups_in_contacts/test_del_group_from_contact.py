from model.group import Group
from model.contact import Contact


def test_del_group_from_contact(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='new group name'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name"))
    available_items = orm.get_available_contact_and_group_del()
    if not available_items:
        contact = db.get_contact_list()[0]
        group = db.get_group_list()[0]
        app.contact.add_group_to_contact(contact, group)
        available_items = orm.get_available_contact_and_group_del()
    contact = available_items["contact"]
    group = available_items["group"]
    assert orm.is_contact_in_group(contact, group)
    app.contact.del_group_from_contact(contact, group)
    assert not orm.is_contact_in_group(contact, group)