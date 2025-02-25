# Importando o Flask
from flask import Flask, render_template
# render_template serve para carregar as páginas

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')
# template_folder é a pasta em que as páginas estão

# Criando a primeira rota do site


@app.route('/')
# Criando função no Python
def home():
    return render_template('index.html')

# Rota de games
# Dicionario em Python = Objeto


@app.route('/games')
def games():
    game = {
        'titulo': 'CS-GO',
        'ano': 2012,
        'categoria': 'FPS Online'
    }
    titulo = 'CS-GO'
    ano = 2012
    categoria = 'FPS Online'
    jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
                 'Quemario', 'Trop', 'Aspax', 'maxxdiego']
    jogos = ['Fortnite', 'Minecraft', 'Stray',
             'The Legend of Zelda: Breath of The Wild', 'Baldurs Gate 3', 'Taiko no Tatsujin']
    return render_template('games.html',
                           game=game,
                           jogadores=jogadores,
                           jogos=jogos)


# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# Para deixar o seu projeto disponivel na rede, trocar o 'localhost' por '0.0.0.0' e disponibilizar o ip da sua máquina para quem quiser acessar
