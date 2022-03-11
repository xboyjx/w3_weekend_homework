
def get_winner(player1_choice, player2_choice):
    winner = "player 2"

    if player1_choice == player2_choice:
        winner = None
    if player1_choice == "rock" and player2_choice == "scissors":
        winner = "player 1"
    if player1_choice == "scissors" and player2_choice == "paper":
        winner = "player 1"
    if player1_choice == "paper" and player2_choice == "rock":
        winner = "player 1"

    return winner
