from behave import *
from features.pages.Login import Login
from features.pages.Dashboard import Dashboard
import time


@given(u'que eu esteja na pagina de login')
def step_impl(context):
    Login(context).navigate_to()

@given(u'insira a matricula do usuário {matricula}')
def step_impl(context, matricula):
    Login(context).inserir_login(matricula)

@given(u'insira a senha do usuário {senha}')
def step_impl(context, senha):
    Login(context).inserir_senha(senha)

@given(u'clico no botão de login')
def step_impl(context):
    Login(context).clicar_botao_login()

@then(u'eu verifico que entrei no AVA')
def step_impl(context):
    Dashboard(context).verificar_elemento()