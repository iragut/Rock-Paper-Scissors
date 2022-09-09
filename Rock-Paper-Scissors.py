import random

game_words = ["rock", "paper", "scissors"]


dict_names = {}
with open("rating.txt") as f:
    for line in f:
        (key, val) = line.split()
        dict_names[key] = val

name = input("Enter your name:")        # take the name for rating if name in file take from there
print(f"Hello, {name}")
if name in dict_names:
    rating = int(dict_names[name])
else:
    rating = 0

winning_list = None
more_words = input().split(',')

if more_words != ['']:
    game_words = more_words

print("Okay, let's start")

while True:
    player_choose = input()
    if player_choose == '!exit':    # the game
        break
    elif player_choose == '!rating':
        print(f"Your rating: {rating}")

    elif player_choose not in game_words:
        print("Invalid input")

    elif player_choose in game_words:       # create the winning list
        calculator_move = random.choice(game_words)
        winning_list = game_words[game_words.index(player_choose) + 1:]
        winning_list += game_words[:game_words.index(player_choose)]
        winning_list = winning_list[:len(winning_list) // 2]

        if calculator_move in winning_list:      # conclusion of the game
            print(f"Sorry, but the computer chose {calculator_move}")
        elif player_choose == calculator_move:
            print(f"There is a draw ({player_choose})")
            rating += 50
        else:
            print(f"Well done. The computer chose {calculator_move} and failed")
            rating += 100
print("Bye!")
