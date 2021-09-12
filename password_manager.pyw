# Módulo responsável por chamar a tela inicial do programa.
from models.user_interface.welcome_screen import WelcomeScreen

run: WelcomeScreen = WelcomeScreen()
run.run()
