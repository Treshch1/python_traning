import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config["base_url"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target["db"]
        self.dbfixture = DbFixture(host=db_config["host"], name=db_config["name"],
                                   username=db_config["username"], password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_list_should_be_equal(self, new_list, old_list):
        assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)