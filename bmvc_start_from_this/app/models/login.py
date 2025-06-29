from abc import ABC, abstractmethod

class Autenticavel(ABC):
    def __init__(self, email: str, senha: str):
        self.email = email
        self.senha = senha

    @abstractmethod
    def verificar_credenciais(self, email: str, senha: str) -> bool:
        pass
