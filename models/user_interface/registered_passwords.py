from tkinter import(
    Tk,
    Label,
    Button,
    StringVar,
    Entry
)
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from models.sqlite.database import DataBase
from tkinter.messagebox import showinfo


class RegisteredPasswords:
    """Classe resposável por exibir o perfil do usuário selecionado."""
    def __init__(self, username: str) -> None:
        """Construtor da classe."""
        self.__username = username
        self.__main_window = Tk()
        self.__main_window.title("SinglePass")
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (
            self.__main_window.winfo_screenwidth() / 2 + 100,
            self.__main_window.winfo_screenheight() / 2 + 100,
            self.__main_window.winfo_screenwidth() / 2 - (self.__main_window.winfo_screenwidth() / 2) / 2 - 100,
            self.__main_window.winfo_screenheight() / 2 - (self.__main_window.winfo_screenheight() / 2 + 100) / 2 - 50
        ))

        # Contador:
        self.__contador = 0

        # Variáveis dinâmicas:
        self.__welcome_user = StringVar()

        # Chamando métodos responsáveis por desenhar os widgets:
        self.__make_label()
        self.__make_tree()
        self.__make_buttons()

    def __make_label(self) -> None:
        """Método responsável por desenhar os rótulos (labels)."""
        Label(master=self.__main_window, text=f"Olá, {self.__username}", font=("Courier New", 16, "bold", "underline"), foreground="#DAA520").place(x=12, y=5)
        Label(master=self.__main_window, text="Abaixo, encontram-se suas informações de cadastro:", font=("Courier New", 14), foreground="#000080").place(x=12, y=43)

    def __make_tree(self) -> None:
        """Método responsável por desenhar a árvore de informações (Treeview)."""
        style = Style()
        style.theme_use("clam")
        style.configure('Treeview.Heading', font=("Courier New", 13, "bold"), foreground="#363636")
        style.configure('Treeview', font=("Courier New", 14))
        self.__tree = Treeview(master=self.__main_window, columns=("#1", "#2", "#3"), show="headings")

        self.__tree.heading("#1", text="Plataforma")
        self.__tree.heading("#2", text="Usuário/E-mail")
        self.__tree.heading("#3", text="Senha")

        self.__tree.column("#1", anchor="center")
        self.__tree.column("#2", anchor="center")
        self.__tree.column("#3", anchor="center")

        for accounts in DataBase().show_accounts():
            self.__tree.insert("", "end", values=[accounts[0], accounts[1], accounts[2]])
            print(accounts)

        self.__tree.place(x=12, y=70, width=760, height=350)

    def __make_buttons(self) -> None:
        """Método responsável por desenhar os botões."""
        Button(master=self.__main_window, text="Adicionar", font=("Courier New", 13), width=18, command=self.__insert).place(x=50, y=430)
        Button(master=self.__main_window, text="Remover", font=("Courier New", 13), width=18, command=self.__remove).place(x=300, y=430)
        Button(master=self.__main_window, text="Voltar", font=("Courier New", 13), width=18, command=self.__to_back).place(x=550, y=430)

    def __insert(self) -> None:
        """Método responsável por desenhar uma caixa de diálogo para receber as informações do novo registro."""

        def data(event=None, **kwargs):
            if len(platform.get()) != 0 and len(username.get()) != 0 and len(password.get()) != 0:
                DataBase().insert_new_account(platform.get().title(), username.get(), password.get())
                self.__make_tree()
                new_record.destroy()
            else:
                new_record.destroy()
                showinfo(title="Aviso", message="Preencha todos os campos")
                self.__insert()

        new_record = Tk()
        new_record.title("Novo Registro")
        new_record.iconbitmap("icons/key_icon_2.ico")
        new_record.resizable(width=0, height=0)
        new_record.geometry("%dx%d+%d+%d" % (540, 300, 400, 200))
        Label(master=new_record, text="Plataforma:", font=("Courier New", 13)).place(x=60, y=10)
        Label(master=new_record, text="Nome de usuário:", font=("Courier New", 13)).place(x=60, y=80)
        Label(master=new_record, text="Senha:", font=("Courier New", 13)).place(x=60, y=150)
        platform = Entry(master=new_record, font=("Courier New", 13), width=40)
        platform.place(x=60, y=40)
        username = Entry(master=new_record, font=("Courier New", 13), width=40)
        username.place(x=60, y=110)
        password = Entry(master=new_record, font=("Courier New", 13), width=40)
        password.bind("<Return>", data)
        password.place(x=60, y=180)
        Button(master=new_record, text="Registrar", font=("Courier New", 13), command=lambda: data(service=platform.get(), user=username.get(), passw=password.get())).place(x=60, y=240)
        Button(master=new_record, text="Cancelar", font=("Courier New", 13), width=10, command=lambda: new_record.destroy()).place(x=205, y=240)
        new_record.mainloop()

    def __remove(self) -> None:
        """Método responsável por apagar os registros do usuário do banco de dados e da árvore de informações."""
        try:
            DataBase().delete_account(self.__tree.item(self.__tree.selection(), "values")[1])
            self.__tree.delete(self.__tree.selection())
        except IndexError:
            showinfo(title="Aviso", message="Selecione o registro antes de deletá-lo")
            self.run()

    def __to_back(self) -> None:
        """Método responsável por sair desta tela e voltar para a tela inicial."""
        from models.user_interface.welcome_screen import WelcomeScreen
        self.__main_window.destroy()
        WelcomeScreen().run()

    def run(self) -> None:
        """Método responsável por rodar esta tela."""
        self.__main_window.mainloop()
