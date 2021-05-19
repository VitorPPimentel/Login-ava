from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url + ""


    locators = {
        "input_login_name": (By.ID, "inputName"),
        "input_login_senha": (By.ID, "inputPassword"),
        "button_login": (By.ID, "submit")
    }

    def inserir_login(self, matricula):
        self.input_login_name.send_keys(matricula)

    def inserir_senha(self, senha):
        self.input_login_senha.send_keys(senha)

    def clicar_botao_login(self):
        self.button_login.click()