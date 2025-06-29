from app.models.login import Autenticavel

class Usuario(Autenticavel):
    def __init__(self, email: str, senha: str, nome: str, idade: int,  genero: int, interresses: str,descricao: str, opcao_sexual: int):
        super().__init__(email, senha)
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.interesses = interresses
        self.descricao = descricao
        self.opcao_sexual = opcao_sexual

    def verificar_credenciais(self, email: str, senha: str) -> bool:
        return self.email == email and self.senha == senha
