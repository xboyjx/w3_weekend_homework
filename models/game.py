class Game:
    def get_winner(player1, player2):
        winner = "player 2"

        if player1.choice == player2.choice:
            winner = None
        if player1.choice == "rock" and player2.choice == "scissors":
            winner = "player 1"
        if player1.choice == "scissors" and player2.choice == "paper":
            winner = "player 1"
        if player1.choice == "paper" and player2.choice == "rock":
            winner = "player 1"

        return winner
