# Importando o Flask
from flask import Flask, render_template
# render_template serve para carregar as páginas

from controllers import routes

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')
# template_folder é a pasta em que as páginas estão

routes.init_app(app)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# Para deixar o seu projeto disponivel na rede, trocar o 'localhost' por '0.0.0.0' e disponibilizar o ip da sua máquina para quem quiser acessar
