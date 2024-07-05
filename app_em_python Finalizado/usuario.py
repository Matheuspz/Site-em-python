from database import inserir_usuario

class Usuario:
    def __init__(self, nome, email, senha, data_nasc):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc

    def salvar_no_banco(self):
        inserir_usuario(self.nome, self.email, self.senha, self.data_nasc)

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Data de Nascimento: {self.data_nasc}"
