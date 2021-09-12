from sqlite3 import connect
from tkinter.messagebox import showerror


class DataBase:
    """Classe que representará o banco de dados"""
    def __init__(self, username: str = None):
        self.__username = username
        self.__connection = connect("database/data.db")
        self.__cursor = self.__connection.cursor()

    def check_record(self, username: str):
        try:
            next(self.__cursor.execute(f""" SELECT username FROM users WHERE username='{username}' """))
            self.__connection.close()
        except StopIteration:
            print("Usuário não encontrado")
            self.__connection.close()

    def insert_record_account(self, platform: str, username: str, password: str):
        self.__cursor.execute(f""" INSERT INTO accounts(platform, username, password) VALUES('{platform}', '{username}', '{password}')""")
        self.__connection.commit()
        self.__connection.close()

    def insert_record_user(self, username, password):
        self.__cursor.execute(f""" INSERT INTO users(username, password) VALUES('{username}', '{password}')""")
        self.__connection.commit()
        self.__connection.close()

    def insert_new_account(self, platform: str, username: str, password: str):
        self.__cursor.execute(f""" INSERT INTO accounts(platform, username, password) VALUES('{platform}', '{username}', '{password}') """)
        self.__connection.commit()
        self.__connection.close()

    def delete_account(self, username):
        self.__cursor.execute(f""" DELETE FROM accounts WHERE username='{username}' """)
        self.__connection.commit()
        self.__connection.close()

    def delete_records(self, username):
        try:
            self.__cursor.execute(f""" DELETE FROM users WHERE username='{username}' """)
            self.__connection.commit()
            self.__connection.close()
        except Exception:
            showerror("Erro", "Algum erro ocorreu na exclusão do registro")
            self.__connection.close()

    def all_records(self):
        usernames: list = list()
        for record in self.__cursor.execute(""" SELECT * FROM users """):
            usernames.append(record[0].title())
        self.__connection.close()
        return usernames

    def check_password(self, password):
        try:
            next(self.__cursor.execute(f""" SELECT password FROM users WHERE password='{password}' """))
            return True
        except StopIteration:
            return False

    def show_accounts(self):
        accounts = []
        for all_accounts in self.__cursor.execute(""" SELECT * FROM accounts """):
            accounts.append(all_accounts)
        self.__connection.close()
        return accounts


if __name__ == "__main__":
    # db = DataBase()
    # DataBase().insert_records(input("username: "), input("password: "))
    # db.check_records()
    print(DataBase().all_records())
    # DataBase().all_records()
    # DataBase().check_record("tang")
    pass
