import pymysql
from model.group import Group


class DbFixture:
    def __init__(self, host, name, username, password):
        self.host = host
        self.name = name
        self.username = username
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=username, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def destroy(self):
        self.connection.close()
