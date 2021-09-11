from sqlite3 import connect


class Validator:
    """Classe responsável por checar as informações no banco de dados."""
    def __init__(self):
        self.__connection = connect("database/data_test.db")  # Conexão do banco de dados.
        self.__cursor = self.__connection.cursor()  # Cursor do banco de dados.

    def check_username(self) -> bool:
        """Método responsável por verificar se há algum usuário cadastrado no banco de dados."""
        try:
            next(self.__cursor.execute("""SELECT username FROM users"""))
            return True  # Retorna True se existir algum perfil no banco de dados

        except StopIteration:
            return False  # Retorna False se o banco de dados não tiver nenhum perfil registrado
