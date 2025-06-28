from bmvc.controller import Controller

class Application(Controller):
    def cadastrar(self):
        if self.request.method == "POST":
            nome = self.request.get_field("nome")
            idade = self.request.get_field("idade")
            email = self.request.get_field("email")
            senha = self.request.get_field("senha")
            genero = self.request.get_field("genero")
            interesses = self.request.get_field("interesses")

            print("📥 Novo cadastro recebido:")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"E-mail: {email}")
            print(f"Senha: {senha}")
            print(f"Gênero: {genero}")
            print(f"Interesses: {interesses}")

            # Simulação de banco de dados: salvando em arquivo
            with open("dados_cadastrados.txt", "a", encoding="utf-8") as f:
                f.write(f"{nome};{idade};{email};{senha};{genero};{interesses}\n")

            return self.view("html/sucesso.html")  # redireciona para página de sucesso
        else:
            return self.view("html/index.html")
