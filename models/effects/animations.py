from tkinter import (Tk, StringVar, Label)
from webbrowser import open


class Animations:
    """Classe responsável pelos efeitos do programa."""
    def __init__(self, root: Tk, stringvar: StringVar, label: Label, text: str) -> None:
        """Construtor da classe."""
        self.__root: Tk = root
        self.__stringvar: StringVar = stringvar
        self.__text: str = text
        self.__github: Label = label
        self.__counter: int = 0  # Variável contadora. Responsável por controlar o estado dos efeitos.

    def automatic_writing(self) -> None:
        """Método responsável pela criação do efeito de escrita automática na tela inicial do programa."""
        if self.__counter <= len(self.__text):
            if self.__counter == len(self.__text):
                self.__counter = 0
                self.give_me_attention()
            else:
                self.__stringvar.set(self.__stringvar.get() + self.__text[self.__counter])
                self.__counter += 1
                self.__root.after(50, self.automatic_writing)  # Velocidade da escrita automática.

    def give_me_attention(self) -> None:
        """Método responsável pelo efeito de 'pisca-pisca' no rodapé da tela inicial."""

        def blue_light(label: Label) -> None:
            """Função responsável por alterar a cor do texto para azul."""
            if self.__counter <= 5:
                label.configure(foreground="#0000FF")
                self.__root.after(100, lambda: orange_light(label))
            else:
                label.configure(foreground="#0000FF")
                self.__counter = 0

        def orange_light(label: Label) -> None:
            """Função responsável por alterar a cor do texto para laranja."""
            label.configure(foreground="#FFA500")
            self.__counter += 1
            self.__root.after(100, lambda: blue_light(label))
        blue_light(self.__github)

    @staticmethod
    def change_cursor(lb_github: Label, status: int) -> None:
        """Método responsável por alterar o cursor quando ele estiver sobre a label 'Github'."""
        if status == 1:
            lb_github.configure(cursor="hand2", font=("Segoe UI Black", 10, "underline"))
        else:
            lb_github.configure(cursor="arrow", font=("Segoe UI Black", 10))

    @staticmethod
    def redirect(event) -> None:
        """Método responsável por direcionar o usuário para o github"""
        open("https://github.com/Paulo-Andrade-Santos?tab=repositories")
