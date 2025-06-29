class Controller:
    def __init__(self, request, usuarios_cadastrados):
        self.request = request
        self.usuarios_cadastrados = usuarios_cadastrados

    def view(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
