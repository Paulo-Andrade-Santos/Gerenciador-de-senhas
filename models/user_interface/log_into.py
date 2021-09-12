from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Checkbutton
)
from models.sqlite.database import DataBase
from tkinter.messagebox import showerror
from models.user_interface.registered_passwords import RegisteredPasswords


class LogInto:
    def __init__(self, selected_user: str, root):
        self.__root = root
        self.__selected_user = selected_user
        self.__main_window = Tk()
        self.__main_window.title("Aviso")
        self.__main_window.configure()
        self.__state = 0
        self.__main_window.iconbitmap("icons/key_icon_2.ico")
        self.__main_window.resizable(width=0, height=0)
        self.__main_window.geometry(newGeometry="%dx%d+%d+%d" % (275, 140, 500, 200))

        # Funções responsáveis por desenhar os itens na tela:
        self.__make_label()
        self.__make_entry()
        self.__make_checkbutton()
        self.__make_buttons()

    def __make_label(self):
        Label(master=self.__main_window, text="Informe a senha", font=("Courier New", 13)).place(x=10, y=10)

    def __make_entry(self):
        self.__password = Entry(master=self.__main_window)
        self.__password.configure(font=("Courier New", 12), width=25, show="•")
        self.__password.focus_force()
        self.__password.bind("<Return>", self.__log_into)
        self.__password.place(x=10, y=40)

    def __make_checkbutton(self):
        Checkbutton(master=self.__main_window, text="Mostrar senha", command=self.__check).place(x=5, y=67)

    def __make_buttons(self):
        self.__btn_entry = Button(master=self.__main_window, text="Entrar", font=("Courier New", 11), command=self.__log_into)
        self.__btn_entry.bind("<Return>", self.__log_into)
        self.__btn_entry.place(x=10, y=100)
        Button(master=self.__main_window, text="Cancelar", font=("Courier New", 11), command=lambda: self.__main_window.destroy()).place(x=110, y=100)

    def __check(self):
        if self.__state == 1:
            self.__on()
        elif self.__state == 0:
            self.__off()

    def __on(self):
        self.__state = 0
        self.__password.configure(show="•")

    def __off(self):
        self.__state = 1
        self.__password.configure(show="")

    def __log_into(self, event=None):
        if DataBase().check_password(self.__password.get()):
            self.__root.destroy()
            self.__main_window.destroy()
            RegisteredPasswords(username=self.__selected_user).run()
        else:
            showerror("Erro", "Senha inválida")
            self.__main_window.destroy()
            LogInto(self.__selected_user, self.__root).execute()

    def execute(self):
        self.__main_window.mainloop()
