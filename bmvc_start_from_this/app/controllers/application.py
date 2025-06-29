from app.models.usuario import Usuario
from bmvc.controller import Controller

class Application(Controller):
    def cadastrar(self):
        if self.request.method == "POST":
            nome = self.request.forms.get("nome")
            idade = self.request.forms.get("idade")
            try:
                idade_int = int(idade)
                if idade_int < 18:
                    return "Erro: É necessário ter 18 anos ou mais para se cadastrar"
            except ValueError:
                return "Erro: Idade inválida. Digite apenas números."

            email = self.request.forms.get("email")

            for u in self.usuarios_cadastrados:
                if u.email == email:
                    return "Erro: Já existe um usuário com esse e-mail"

            senha = self.request.forms.get("senha")
            genero = int(self.request.forms.get("genero"))
            interesses = self.request.forms.get("interesses")
            descricao = self.request.forms.get("descricao")
            opcao_sexual = int(self.request.forms.get("opcao_sexual"))

            novo_usuario = Usuario(
                email=email,
                senha=senha,
                nome=nome,
                idade=idade_int,
                genero=genero,
                interresses=interesses,
                descricao=descricao,
                opcao_sexual=opcao_sexual
            )

            self.usuarios_cadastrados.append(novo_usuario)

            return self.view("app/views/html/sucesso.html")  # redireciona para página de sucesso
        else:
            return self.view("app/views/html/index.html")
