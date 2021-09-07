from tkinter import (
    Tk,
    Frame,
    Label,
    Entry,
    Button
)


class WelcomeScreen:
    """Classe resposável por exibir a janela inicial do programa."""
    def __init__(self) -> None:
        """Construtor da classe. Responsável por atribuir as características da janela principal (__main_window)."""
        self.__main_window = Tk()
        self.__main_window.title("Gerenciador de senhas")
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.resizable(width=0, height=0)
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (
            self.__main_window.winfo_screenwidth() / 2,
            self.__main_window.winfo_screenheight() / 2,
            self.__main_window.winfo_screenwidth() / 2 - (self.__main_window.winfo_screenwidth() / 2) / 2,
            self.__main_window.winfo_screenheight() / 2 - (self.__main_window.winfo_screenheight() / 2 + 100) / 2
        ))
        self.execute()

    def execute(self) -> None:
        """Método responsável por iniciar a execução da janela principal."""
        self.__main_window.mainloop()
