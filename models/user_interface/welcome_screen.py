from tkinter import (
    Tk,
    Frame,
    Label,
    Button,
    PhotoImage,
    StringVar,
    LEFT
)
from models.effects.animations import Animations
from models.sqlite.validator import Validator


class WelcomeScreen:
    """Classe resposável por exibir a janela inicial do programa."""
    def __init__(self) -> None:
        """Construtor da classe. Responsável por atribuir as características da janela principal (__main_window)."""
        self.__main_window: Tk = Tk()
        self.__main_window.title("SinglePass")
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.resizable(width=0, height=0)
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (
            self.__main_window.winfo_screenwidth() / 2,
            self.__main_window.winfo_screenheight() / 2,
            self.__main_window.winfo_screenwidth() / 2 - (self.__main_window.winfo_screenwidth() / 2) / 2,
            self.__main_window.winfo_screenheight() / 2 - (self.__main_window.winfo_screenheight() / 2 + 100) / 2
        ))

        # Variáveis dinâmicas:
        self.__automatic_writing: StringVar = StringVar()

        # Fotos que serão utilizadas no programa:
        self.__one_key: PhotoImage = PhotoImage(file="images/keys_02_72px.png")
        self.__new_profile: PhotoImage = PhotoImage(file="images/new_profile_02_32px.png")
        self.__remove_profile: PhotoImage = PhotoImage(file="images/remove_profile_02_32px.png")
        self.__exit: PhotoImage = PhotoImage(file="images/exit_01.png")

        # Chamando todas as funções responsáveis por desenhar os ítens necessários na tela:
        self.__make_frames()
        self.__make_labels()
        self.__make_buttons()

        # Chamando as animações da tela:
        self.__effects()

    def __make_frames(self) -> None:
        """Método responsável por desenhar as molduras (frames)."""
        self.__top_frame: Frame = Frame(master=self.__main_window)
        self.__top_frame.configure(relief="groove", borderwidth=1, width=663, height=170)  # flat, groove, raised, ridge, solid, or sunken
        self.__top_frame.grid(row=0, column=0, padx=10, pady=10)

        self.__bottom_frame: Frame = Frame(master=self.__main_window)
        self.__bottom_frame.configure(relief="groove", borderwidth=1, width=663, height=160)
        self.__bottom_frame.grid(row=1, column=0, padx=10, pady=5)

    def __make_labels(self) -> None:
        """Método responsável por desenhar os rótulos (labels)."""
        Label(master=self.__top_frame, image=self.__one_key).place(x=280, y=20)
        Label(master=self.__top_frame, text="Seja bem-vindo ao SinglePass", font=("Corbel Bold", 15, "underline"), foreground="#DAA520").place(x=190, y=100)
        self.__animated_label: Label = Label(master=self.__top_frame)
        self.__animated_label.configure(font=("Ink Free", 15), textvariable=self.__automatic_writing, foreground="#000080")
        self.__animated_label.place(x=6, y=130)
        self.__created_by: Label = Label(master=self.__main_window, text="Criado por: Paulo Andrade", foreground="#4F4F4F", font=("Segoe UI Black", 10))
        self.__created_by.place(x=7, y=356)
        self.__github: Label = Label(master=self.__main_window, text="Meu Github", foreground="#363636", font=("Segoe UI Black", 10))
        self.__github.bind("<Enter>", lambda event: Animations.change_cursor(self.__github, 1))
        self.__github.bind("<Leave>", lambda event: Animations.change_cursor(self.__github, 0))
        self.__github.bind("<Button-1>", Animations.redirect)
        self.__github.place(x=595, y=356)

    def __make_buttons(self) -> None:
        """Método responsável por desenhar os botões (buttons)."""
        Button(master=self.__bottom_frame, image=self.__new_profile, text="Criar Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=170, cursor="hand1").place(x=230, y=10)
        if Validator().check_username(): Button(master=self.__bottom_frame, image=self.__remove_profile, text="Remover Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=190, cursor="hand1").place(x=220, y=60)
        else: Button(master=self.__bottom_frame, image=self.__remove_profile, text="Remover Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=190, state="disabled", cursor="hand1").place(x=220, y=60)
        Button(master=self.__bottom_frame, image=self.__exit, text="Sair", font=("Ink Free", 15, "bold"), compound=LEFT, width=100, command=lambda: exit(0), cursor="hand1").place(x=265, y=110)

    def __effects(self):
        """Método responsável por chamar todas as animações que ocorrem na tela principal"""
        Animations(self.__main_window, self.__automatic_writing, self.__github)

    def execute(self) -> None:
        """Método responsável por iniciar a execução da janela principal."""
        self.__main_window.mainloop()
