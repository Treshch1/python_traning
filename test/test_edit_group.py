from model.group import Group


def test_edit_name(app):
    app.group.edit_first_group(Group(name="name"))


def test_edit_header(app):
    app.group.edit_first_group(Group(header="header"))
