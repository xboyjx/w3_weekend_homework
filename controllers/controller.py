from flask import render_template, request
from app import app
from models.game import get_winner
from models.example_players import player1, player2


@app.route('/<player1_choice>/<player2_choice>')
def winner_page(player1_choice, player2_choice):
    winner = get_winner(player1_choice, player2_choice)
    return render_template('index.html', title='Home', winner = winner)