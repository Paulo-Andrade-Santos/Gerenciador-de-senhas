from sqlite3 import connect
from tkinter.messagebox import showerror


class DataBase:
    """Classe responsável por realizar todas as operações envolvendo o banco de dados da aplicação."""
    def __init__(self, username: str = None) -> None:
        """Construtor da classe."""
        self.__username = username
        self.__connection = connect("database/data.db")
        self.__cursor = self.__connection.cursor()

    def check_record(self, username: str) -> None:
        """Método responsável por verificar se o usuário passado como argumento está registrado no banco de dados."""
        try:
            next(self.__cursor.execute(f""" SELECT username FROM users WHERE username='{username}' """))
            self.__connection.close()
        except StopIteration:
            print("Usuário não encontrado")
            self.__connection.close()

    def insert_record_user(self, username: str, password: str) -> None:
        """Método responsável por inserir novos registros na tabela 'users' do bando de dados."""
        self.__cursor.execute(f""" INSERT INTO users(username, password) VALUES('{username}', '{password}')""")
        self.__connection.commit()
        self.__connection.close()

    def insert_new_account(self, platform: str, username: str, password: str) -> None:
        """Método responsável por inserir um novo registro para um usuário específico."""
        self.__cursor.execute(f""" INSERT INTO accounts(platform, username, password) VALUES('{platform}', '{username}', '{password}') """)
        self.__connection.commit()
        self.__connection.close()

    def delete_account(self, username: str) -> None:
        """Método responsável por deletar um registro de um usuário específico na tabela 'accounts'."""
        self.__cursor.execute(f""" DELETE FROM accounts WHERE username='{username}' """)
        self.__connection.commit()
        self.__connection.close()

    def delete_records(self, username: str) -> None:
        """Método responsável por deletar um usuário da tabela 'users'."""
        # noinspection PyBroadException
        try:
            self.__cursor.execute(f""" DELETE FROM users WHERE username='{username}' """)
            self.__connection.commit()
            self.__connection.close()
        except Exception:
            showerror("Erro", "Algum erro ocorreu na exclusão do registro")
            self.__connection.close()

    def all_records(self) -> list:
        """Método responsável por retornar uma lista contendo todos os usuários da tabela 'users' no banco de dados. Essa informação será utilizada pela Treview da tela inicial."""
        usernames: list = list()
        for record in self.__cursor.execute(""" SELECT * FROM users """):
            usernames.append(record[0].title())
        self.__connection.close()
        return usernames

    def check_password(self, password: str) -> bool:
        """Método utilizado para validação das senhas informadas na tela inicial."""
        try:
            next(self.__cursor.execute(f""" SELECT password FROM users WHERE password='{password}' """))
            return True
        except StopIteration:
            return False

    def show_accounts(self) -> list:
        """Método responsável por retornar uma lista contando todos os registros da tabela 'accounts'. Essa informação será utilizada pela Treeview da tela de informações de registro dos usuários."""
        accounts = []
        for all_accounts in self.__cursor.execute(""" SELECT * FROM accounts """):
            accounts.append(all_accounts)
        self.__connection.close()
        return accounts
