from sqlite3 import connect


class DataBase:
    """Classe que representará o banco de dados"""
    def __init__(self, username: str = None):
        self.__username = username
        self.__connection = connect("database/data_test.db")
        self.__cursor = self.__connection.cursor()

    def check_record(self, username: str):
        try:
            next(self.__cursor.execute(f""" SELECT username FROM users WHERE username='{username}' """))
            self.__connection.close()
        except StopIteration:
            print("Usuário não encontrado")
            self.__connection.close()

    def insert_records(self, username: str, password: str):
        self.__cursor.execute(f""" INSERT INTO users(username, password) VALUES('{username}', '{password}')""")
        self.__connection.commit()
        self.__connection.close()

    def delete_records(self, username):
        try:
            self.__cursor.execute(f""" DELETE FROM users WHERE username='{username}' """)
            self.__connection.commit()
            self.__connection.close()
        except Exception:
            print("ERRO: ALGUM ERRO OCORREU AO EXCLUIR UM REGISTRO")
            self.__connection.close()

    def all_records(self):
        usernames: list = list()
        for record in self.__cursor.execute(""" SELECT * FROM users """):
            # print(record[0])
            usernames.append(record[0])
        self.__connection.close()
        return usernames


if __name__ == "__main__":
    # db = DataBase()
    # DataBase().insert_records(input("username: "), input("password: "))
    # db.check_records()
    print(DataBase().all_records())
    # DataBase().all_records()
    # DataBase().check_record("tang")
    pass
