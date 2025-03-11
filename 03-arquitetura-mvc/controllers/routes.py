from flask import render_template, request

jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']


def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    # Rota de games
    # Dicionario em Python = Objeto

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = {
            'titulo': 'CS-GO',
            'ano': 2012,
            'categoria': 'FPS Online'
        }


        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))

        jogos = ['Fortnite', 'Minecraft', 'Stray',
                 'The Legend of Zelda: Breath of The Wild', 'Baldurs Gate 3', 'Taiko no Tatsujin']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
