#importando o Flask
from flask import Flask

# Carregando o Flask na variavel app
app = Flask(__name__)

#Criando a Primeira Rota do Site
@app.route('/')

#Criando funcion no Python
def home():
    return '<h1>Hello World!</h1>'


#Iniciando o servidor no localhost
if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)
