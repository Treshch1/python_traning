from model.group import Group


def test_edit_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='new group name'))
        old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='new group name'))
        old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
