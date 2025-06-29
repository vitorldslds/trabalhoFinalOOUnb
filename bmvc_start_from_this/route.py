from app.controllers.application import Application
from bottle import Bottle, run, request, static_file

app = Bottle()

# Rota para a página inicial
@app.route('/')
@app.route('/index.html')
def index():
    return static_file('index.html', root='./app/views/html')

# Formulário de cadastro
@app.route('/application/cadastrar', method=['POST'])
def cadastrar_usuario():
    ctl = Application(request)
    return ctl.cadastrar()

# Rotas específicas de páginas (se precisar)
@app.route('/pagina', method=['GET'])
def action_pagina():
    ctl = Application(request)
    return ctl.render('pagina')

@app.route('/helper')
def helper():
    ctl = Application(request)
    return ctl.render('helper')

# Rota para arquivos estáticos (css, js, etc)
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/login', method=['GET'])
def login_form():
    return static_file('login.html', root='./app/views/html')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
