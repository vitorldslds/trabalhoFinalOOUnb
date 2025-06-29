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
            senha = self.request.forms.get("senha")
            genero = self.request.forms.get("genero")
            interesses = self.request.forms.get("interesses")
            descricao = self.request.forms.get("descrição")
            opção_sexual = self.request.forms.get("opção_sexual")

            print("📥 Novo cadastro recebido:")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"E-mail: {email}")
            print(f"Senha: {senha}")
            print(f"Gênero: {genero}")
            print(f"Interesses: {interesses}")

            # Simulação de banco de dados: salvando em arquivo
            with open("dados_cadastrados.txt", "a", encoding="utf-8") as f:
                f.write(f"{nome};{idade_int};{email};{senha};{genero};{interesses};{descricao};{opção_sexual}\n")

            return self.view("app/views/html/sucesso.html")  # redireciona para página de sucesso
        else:
            return self.view("app/views/html/index.html")
