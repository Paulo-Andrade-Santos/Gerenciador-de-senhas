from tkinter import (
    Tk,
    Frame,
    Label,
    Button,
    PhotoImage,
    StringVar,
    LEFT
)
from tkinter.ttk import (
    Separator,
    Treeview,
    Style
)
from models.user_interface.log_into import LogInto
from tkinter.messagebox import showinfo
from models.effects.animations import Animations
from models.sqlite.validator import Validator
from models.user_interface.add_new_profile import NewProfile
from models.sqlite.database import DataBase


class WelcomeScreen:
    """Classe resposável por exibir a janela inicial do programa."""
    def __init__(self) -> None:
        """Construtor da classe. Responsável por atribuir as características da janela principal (__main_window)."""
        self.__main_window: Tk = Tk()
        self.__main_window.title("SinglePass")
        self.__background_color = StringVar(value="#D7D7D7")
        self.__main_window.configure(background=self.__background_color.get())
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.resizable(width=0, height=0)
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (
            self.__main_window.winfo_screenwidth() / 2,
            self.__main_window.winfo_screenheight() / 2,
            self.__main_window.winfo_screenwidth() / 2 - (self.__main_window.winfo_screenwidth() / 2) / 2,
            self.__main_window.winfo_screenheight() / 2 - (self.__main_window.winfo_screenheight() / 2 + 100) / 2
        ))

        # Eixo X dos botões presentes no segundo frame (bottom_frame):
        self.__X_axis = 100

        # Variáveis dinâmicas:
        self.__automatic_writing: StringVar = StringVar()

        # Fotos que serão utilizadas no programa:
        self.__one_key: PhotoImage = PhotoImage(file="images/keys_02_72px.png")
        self.__new_profile: PhotoImage = PhotoImage(file="images/new_profile_02_32px.png")
        self.__remove_profile: PhotoImage = PhotoImage(file="images/remove_profile_02_32px.png")
        self.__exit: PhotoImage = PhotoImage(file="images/exit_01.png")

        # Chamando todas as funções responsáveis por desenhar os ítens necessários na tela:
        self.__make_frames()
        self.__make_separators()
        self.__make_labels()
        self.__make_treeview()
        self.__make_buttons()

        # Chamando as animações da tela:
        self.__effects()

    def __make_frames(self) -> None:
        """Método responsável por desenhar as molduras (frames)."""
        self.__top_frame: Frame = Frame(master=self.__main_window)
        self.__top_frame.configure(relief="sunken", borderwidth=1, width=663, height=170)  # flat, groove, raised, ridge, solid, or sunken
        self.__top_frame.grid(row=0, column=0, padx=10, pady=10)

        self.__bottom_frame: Frame = Frame(master=self.__main_window)
        self.__bottom_frame.configure(relief="sunken", borderwidth=1, width=663, height=160)
        self.__bottom_frame.grid(row=1, column=0, padx=10, pady=5)

    def __make_labels(self) -> None:
        """Método responsável por desenhar os rótulos (labels)."""
        Label(master=self.__top_frame, image=self.__one_key).place(x=280, y=20)
        Label(master=self.__top_frame, text="Seja bem-vindo ao SinglePass", font=("Corbel Bold", 15, "underline"), foreground="#DAA520").place(x=190, y=100)
        if not Validator().check_username():
            self.__animated_label: Label = Label(master=self.__top_frame)
            self.__animated_label.configure(font=("Ink Free", 15), textvariable=self.__automatic_writing, foreground="#000080")
            self.__animated_label.place(x=6, y=130)
        else:
            self.__animated_label: Label = Label(master=self.__top_frame)
            self.__animated_label.configure(font=("Ink Free", 15), textvariable=self.__automatic_writing, foreground="#000080")
            self.__animated_label.place(x=25, y=130)
        self.__created_by: Label = Label(master=self.__main_window, text="Criado por: Paulo Andrade", foreground="#898989", font=("Segoe UI Black", 10), background=self.__background_color.get())
        self.__created_by.place(x=7, y=356)
        self.__github: Label = Label(master=self.__main_window, text="Github", foreground="#898989", font=("Segoe UI Black", 10), background=self.__background_color.get())
        self.__github.bind("<Enter>", lambda event: Animations.change_cursor(self.__github, 1))
        self.__github.bind("<Leave>", lambda event: Animations.change_cursor(self.__github, 0))
        self.__github.bind("<Button-1>", Animations.redirect)
        self.__github.place(x=625, y=356)

    def __make_buttons(self) -> None:
        """Método responsável por desenhar os botões (buttons)."""
        Button(master=self.__bottom_frame, image=self.__new_profile, text="Criar Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=170, cursor="hand1", command=self.__add_new_profile).place(x=self.__X_axis - 35, y=5)
        if Validator().check_username():
            Button(master=self.__bottom_frame, image=self.__remove_profile, text="Remover Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=190, cursor="hand1", command=self.__delete_profile).place(x=self.__X_axis - 45, y=55)
        else:
            Button(master=self.__bottom_frame, image=self.__remove_profile, text="Remover Perfil", font=("Ink Free", 15, "bold"), compound=LEFT, width=190, state="disabled", cursor="hand1").place(x=self.__X_axis - 45, y=55)
            Button(master=self.__bottom_frame)
        if Validator().check_username():
            Button(master=self.__bottom_frame, text="Entrar", font=("Ink Free", 14, "bold"), cursor="hand1", command=self.__login_into).place(x=55, y=106)
        else:
            Button(master=self.__bottom_frame, text="Entrar", font=("Ink Free", 14, "bold"), cursor="hand1", state="disabled").place(x=55, y=106)
        Button(master=self.__bottom_frame, image=self.__exit, text="Sair", font=("Ink Free", 15, "bold"), compound=LEFT, width=100, command=lambda: exit(0), cursor="hand1").place(x=self.__X_axis + 45, y=105)

    def __make_separators(self) -> None:
        """Método responsável por desenhar os separadores."""
        Separator(self.__bottom_frame, orient="vertical").place(x=320, y=0, height=160)

    def __make_treeview(self) -> None:
        """Método responsável por desenhar a árvore de informações."""
        style: Style = Style()
        style.theme_use("clam")
        style.configure('Treeview.Heading', font=("Courier New", 13, "bold"), foreground="#363636")
        style.configure('Treeview', font=("Courier New", 14))

        self.__registered_users: Treeview = Treeview(master=self.__bottom_frame, columns=(1,), show="headings")
        self.__registered_users.heading("#1", text="Perfis Registrados")
        self.__registered_users.column("#1", anchor="center")

        for record in DataBase().all_records():
            self.__registered_users.insert("", "end", values=[record])
        self.__registered_users.place(x=325, y=0, width=335, height=158)

    def __effects(self) -> None:
        """Método responsável por chamar todos os efeitos que ocorrem na tela inicial"""
        if not Validator().check_username():
            text = "Antes de armazenar as suas senhas, crie um perfil para ter mais segurança"
            Animations(self.__main_window, self.__automatic_writing, self.__github, text).automatic_writing()
        else:
            text = "O gerenciador de senhas feito para quem quer segurança e simplicidade"
            Animations(self.__main_window, self.__automatic_writing, self.__github, text).automatic_writing()

    def __add_new_profile(self) -> None:
        """Método responsável por chamar a tela de novo usuário."""
        self.__main_window.destroy()
        NewProfile().run()

    def __delete_profile(self) -> None:
        """Método responsável por deletar um usuário da tabela 'users' e da árvore de informações da tela inicial."""
        try:
            DataBase().delete_records(self.__registered_users.item(self.__registered_users.selection(), "values")[0].lower())
            self.__registered_users.delete(self.__registered_users.selection())
            self.__make_buttons()
        except IndexError:
            showinfo("Aviso", "Antes de remover um perfil, você deve selecioná-lo no campo 'perfis registrados'")

    def __login_into(self) -> None:
        """Método responsável por chamar a tela de login para entrar num perfil específico."""
        try:
            # noinspection PyStatementEffect
            self.__registered_users.item(self.__registered_users.selection(), "values")[0]
            LogInto(selected_user=self.__registered_users.item(self.__registered_users.selection(), "values")[0], root=self.__main_window).execute()
        except IndexError:
            showinfo("Aviso", "Antes de entrar em um perfil, você deve selecioná-lo no campo 'perfis registrados'")

    def run(self) -> None:
        """Método responsável por iniciar a execução da janela principal."""
        self.__main_window.mainloop()
