from features.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Dashboard(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url = self.url + ""


    locators = {
        "nome_usuario": (By.XPATH, '//*[@id="action-menu-toggle-0"]/span/span[1]')
    }


    def verificar_elemento(self):
        self.nome_usuario.text == "Vitor Pimentel Barbosa ."