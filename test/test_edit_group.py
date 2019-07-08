from model.group import Group


def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group name'))
    app.group.edit_first_group(Group(name="name"))


def test_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='new group name'))
    app.group.edit_first_group(Group(header="header"))
