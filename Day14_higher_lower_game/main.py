from art import logo, vs
from game_data import data
import os
import numpy as np


# print(len(data))
# print(data[1])
# dic_A = data[1]
# print(dic_A["name"])

def end_game(user_score):
    # clear the terminal
    os.system("cls")
    print(logo)
    print(f"Sorry that's wrong. Final score: {user_score}")

def gameboard(user_score, dic_A, dic_B):
    # clear the terminal
    os.system("cls")
    print(logo)
    if user_score>0:
        print(f"You are right ! Current_score: {user_score}")
    # print(dic_A)
    # print(dic_B)
    # print(f'Compare A: {dic_A["name"]}, a {dic_A["description"]}, from {dic_A["country"]}, followers {dic_A["follower_count"]}.')
    print(f'Compare A: {dic_A["name"]}, a {dic_A["description"]}, from {dic_A["country"]}.')
    print(vs)
    # print(f'Compare B: {dic_B["name"]}, a {dic_B["description"]}, from {dic_B["country"]}, followers {dic_B["follower_count"]}.')
    print(f'Compare B: {dic_B["name"]}, a {dic_B["description"]}, from {dic_B["country"]}.')
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    return user_guess

def play(user_guess, user_score):
    # print(f"user_score before guess {user_score}")
    if user_guess == "A":
        user_type = dic_A["follower_count"]
        comp_type = dic_B["follower_count"]
    else:
        user_type = dic_B["follower_count"]
        comp_type = dic_A["follower_count"]

    if user_type > comp_type:
        user_score += 1
        # print(f"user_score after guess {user_score}")
        is_game_finished = False
    else:
        is_game_finished = True
    return user_score, is_game_finished

def finish_the_game(user_score):
    # clear the terminal
    os.system("cls")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {user_score}")

is_game_finished = False
user_score = 0

while is_game_finished == False:
    if user_score == 0:
        pos_A = np.random.randint(0, len(data))
        # print(f"Pos_A = {pos_A}")
        data.pop(pos_A)
        # print(f"Data length: {len(data)}")
        pos_B = np.random.randint(0, len(data))
        # print(f"Pos_B = {pos_B}")
        dic_A = data[pos_A]
        dic_B = data[pos_B]
        # print(f"Data length: {len(data)}")        
    else:
        dic_A = dic_B
        pos_B = np.random.randint(0, len(data))
        dic_B = data[pos_B]
        
    data.pop(pos_B)
    # print(dic_A["name"])
    # guess = input("STOP")

    user_guess = gameboard(user_score, dic_A, dic_B)
    user_score, is_game_finished = play(user_guess, user_score)
    # print(user_score)
    # print(is_game_finished)

finish_the_game(user_score)
# print("The game is finished!")