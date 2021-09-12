from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Checkbutton,
    IntVar
)
from models.sqlite.database import DataBase
from tkinter.messagebox import showinfo


class NewProfile:
    def __init__(self):
        """Construtor da classe. Responsável por atribuir as características da janela principal (__main_window)."""
        self.__main_window: Tk = Tk()
        self.__main_window.title("SinglePass")
        self.__main_window.configure(background="#DAA520")  # #DAA520
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.resizable(width=0, height=0)
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (
            self.__main_window.winfo_screenwidth() / 2 - 100,
            self.__main_window.winfo_screenheight() / 2 - 30,
            self.__main_window.winfo_screenwidth() / 2 - (self.__main_window.winfo_screenwidth() / 2) / 2,
            self.__main_window.winfo_screenheight() / 2 - (self.__main_window.winfo_screenheight() / 2 + 100) / 2
        ))

        # Eixo X de todos os elementos da tela:
        self.__X_axis = 110

        # Chamando todas as funções responsáveis por desenhar os ítens necessários na tela:
        self.__make_labels()
        self.__make_entrys()
        self.__make_button()
        self.__make_check_buttons()

    def __make_labels(self):
        """Método responsável por desenhar os rótulos (labels)."""
        Label(master=self.__main_window, text="Nome de usuário:", font=("Courier New", 15, "bold"), background="#DAA520").place(x=self.__X_axis, y=50)
        Label(master=self.__main_window, text="Senha:", font=("Courier New", 15, "bold"), background="#DAA520").place(x=self.__X_axis, y=150)

    def __make_entrys(self):
        """Método responsável por desenhar os campos de entrada (entrys)."""
        self.__username = Entry(master=self.__main_window)
        self.__username.configure(font=("Courier New", 15), width=30)
        self.__username.place(x=self.__X_axis, y=80)
        self.__pass_entry: Entry = Entry(master=self.__main_window)
        self.__pass_entry.configure(font=("Courier New", 15), width=30, show="•")
        self.__pass_entry.bind("<Return>", self.__insert_record)
        self.__pass_entry.place(x=self.__X_axis, y=180)

    def __make_button(self):
        """Método responsável por desenhar os botões (buttons)."""
        Button(master=self.__main_window, text="Registrar", font=("Courier New", 14, "bold"), cursor="hand1", command=self.__insert_record, background="#d7d7d7").place(x=self.__X_axis, y=270)
        Button(master=self.__main_window, text="Voltar", font=("Courier New", 14, "bold"), width=10, cursor="hand1", command=self.__welcome_screen, background="#d7d7d7").place(x=self.__X_axis + 245, y=270)

    def __make_check_buttons(self):
        state: IntVar = IntVar()
        Checkbutton(master=self.__main_window, activebackground="#DAA520", background="#DAA520", text="Mostar senha", font=("Courier New", 10, "bold"), variable=state, command=lambda: self.__pass_entry.configure(show="") if state.get() == 1 else self.__pass_entry.configure(show="•")).place(x=self.__X_axis - 5, y=210)

    def __welcome_screen(self):
        self.__main_window.destroy()
        from models.user_interface.welcome_screen import WelcomeScreen
        WelcomeScreen().run()

    def __insert_record(self, event=None):
        if len(self.__username.get()) != 0 and len(self.__pass_entry.get()) != 0:
            DataBase().insert_record_user(self.__username.get(), self.__pass_entry.get())
            self.__welcome_screen()
        else:
            showinfo("Aviso", "Preencha todos os campos antes de se registrar")

    def run(self):
        """Método responsável por rodar a aplicação."""
        self.__main_window.mainloop()


if __name__ == "__main__":
    NewProfile().run()
