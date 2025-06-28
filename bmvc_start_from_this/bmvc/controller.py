class Controller:
    def __init__(self, request):
        self.request = request

    def view(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
