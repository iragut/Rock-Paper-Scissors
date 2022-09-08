import random

game_words = ["rock", "scissors", "paper"]

dict_names = {}
with open("rating.txt") as f:
    for line in f:
        (key, val) = line.split()
        dict_names[key] = val

name = input("Enter your name:")
print(f"Hello, {name}")
if name in dict_names:
    rating = int(dict_names[name])
else:
    rating = 0


while True:
    calculator_move = random.choice(game_words)
    player_move = input()
    if player_move not in game_words and player_move != "!exit" and player_move != "!rating":
        print("Invalid input")
    elif player_move == "!exit":
        break
    elif player_move == "!rating":
        print(f"Your rating: {rating}")
    else:
        if player_move == calculator_move:
            print(f"There is a draw ({player_move})")
            rating += 50

        elif player_move == "scissors" and calculator_move == "rock":
            print("Sorry, but the computer chose rock")
        elif player_move == "scissors" and calculator_move == "paper":
            print("Well done. The computer chose paper and failed")
            rating += 100

        elif player_move == "rock" and calculator_move == "paper":
            print("Sorry, but the computer chose paper")
        elif player_move == "rock" and calculator_move == "scissors":
            print("Well done. The computer chose scissors and failed")
            rating += 100

        elif player_move == "paper" and calculator_move == "scissors":
            print("Sorry, but the computer chose scissors")
        elif player_move == "paper" and calculator_move == "rock":
            print("Well done. The computer chose rock and failed")
            rating += 100
print("Bye!")
