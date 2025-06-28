from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response

app = Bottle()

# Rota para a página inicial
@app.route('/')
@app.route('/index.html')
def index():
    return static_file('index.html', root='./html')

# Rotas específicas
@app.route('/pagina', method=['GET'])
def action_pagina():
    ctl = Application(request)
    return ctl.render('pagina')

@app.route('/helper')
def helper():
    ctl = Application(request)
    return ctl.render('helper')

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

# Rota para servir arquivos estáticos da pasta html (deve ficar por último)
@app.route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./html')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
