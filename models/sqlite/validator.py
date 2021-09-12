from sqlite3 import connect


class Validator:
    """Classe responsável por checar se há usuários registrados no banco de dados assim que a tela inicial é exibida. Essa classe trabalha de forma concomitante com o efeito de escrita automática da tela inicial."""
    def __init__(self) -> None:
        """Construtor da classe."""
        self.__connection = connect("database/data.db")
        self.__cursor = self.__connection.cursor()

    def check_username(self) -> bool:
        """Método responsável por verificar se há algum usuário cadastrado no banco de dados."""
        try:
            next(self.__cursor.execute("""SELECT username FROM users"""))
            return True
        except StopIteration:
            return False
