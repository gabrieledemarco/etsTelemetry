from DBService import DbService


class Users:
    def __init__(self, nickname: str = None, pass_w: str = None, telemetry_url: str = None):
        self.nickname = nickname
        self.pass_w = pass_w
        self.telemetry = telemetry_url


class UsersDao:
    def __init__(self, Dbs: DbService):
        self.db = Dbs

    def insert(self, User: Users):
        self.db.insert(name_table="users", list_record=[(User.nickname,
                                                         User.pass_w,
                                                         User.telemetry)])

    def get_users_list(self):
        self.db.get_all_value_in_column(name_table="users", name_column="nickname")

    def get_passw_list(self):
        self.db.get_all_value_in_column(name_table="users", name_column="pass_word")

    def is_user_registered(self, User: Users):
        if User.nickname in self.get_users_list():
            state = True
        else:
            state = False

        return state

    def get_user_telemetry(self, User: Users):
        return self.db.get_select_with_where(select_columns='telemetry_url',
                                             name_table='users',
                                             where_columns='nickname',
                                             values_column=User.nickname)
