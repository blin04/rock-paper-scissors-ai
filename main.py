def winner(player1, player2):
    # igrac moze odigrati: "rock", "paper", "scissors"
    # moguci ishodi: 1, 2, 0
    if player1 == player2:
        # nereseno
        return 0
    if player1 == "rock":
        if player2 == "paper":
            # pobedio je igrac 2
            return 2
        else:
            # pobedio je igrac1
            return 1
    elif player1 == "paper":
        if player2 == "scissors":
            return 2
        else:
            return 1
    else:
        if player2 == "rock":
            return 2
        else:
            return 1


print(winner("rock", "paper"))
