from model.contact import Contact
import random
import time


def test_delete_random_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="first name"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(0.1)
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
