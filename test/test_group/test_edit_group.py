from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(2)
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_edit_name(app, db, group):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='new group name'))
    old_groups = db.get_group_list()
    editable_group = random.choice(old_groups)
    group.id = editable_group.id
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(editable_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
