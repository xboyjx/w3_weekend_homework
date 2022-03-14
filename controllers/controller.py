from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route('/<player1_choice>/<player2_choice>')
def winner_page(player1_choice, player2_choice):
    player1 = Player("Jacob", player1_choice)
    player2 = Player("John", player2_choice)
    winner = Game.get_winner(player1, player2)
    return render_template('index.html', title='Home', winner = winner)