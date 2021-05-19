#language: pt

Funcionalidade: Realizar login no ava

    @Login
    Esquema do Cenário: realizar login na página do AVA com sucesso - ambos usuário e senha estarão corretos

        Dado que eu esteja na pagina de login
        E insira a matricula do usuário <matricula>
        E insira a senha do usuário <senha>
        E clico no botão de login
        Então eu verifico que entrei no AVA

            Exemplos:
            | matricula   | senha       |
            | 2018B010070 | 70279754400 |