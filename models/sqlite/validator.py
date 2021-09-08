from sqlite3.dbapi2 import connect


class Validator:
    """Classe responsável por checar as informações no banco de dados."""
    def __init__(self):
        self.__connection = connect("database/data.db")  # Conexão do banco de dados.
        self.__cursor = self.__connection.cursor()  # Cursor do banco de dados.

    def check_username(self) -> bool:
        try:
            next(self.__cursor.execute("""SELECT username FROM users"""))
            return True

        except StopIteration:
            return False
