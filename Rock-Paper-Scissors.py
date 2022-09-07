import random

game_words = ["rock", "scissors", "paper"]

while True:
    calculator_move = random.choice(game_words)
    player_move = input()
    if player_move not in game_words and player_move != "!exit":
        print("Invalid input")
    elif player_move == "!exit":
        break
    else:
        if player_move == calculator_move:
            print(f"There is a draw ({player_move})")
        elif player_move == "scissors" and calculator_move == "rock":
            print("Sorry, but the computer chose rock")
        elif player_move == "scissors" and calculator_move == "paper":
            print("Well done. The computer chose paper and failed")

        elif player_move == "rock" and calculator_move == "paper":
            print("Sorry, but the computer chose paper")
        elif player_move == "rock" and calculator_move == "scissors":
            print("Well done. The computer chose scissors and failed")

        elif player_move == "paper" and calculator_move == "scissors":
            print("Sorry, but the computer chose scissors")
        elif player_move == "paper" and calculator_move == "rock":
            print("Well done. The computer chose rock and failed")
print("Bye!")
