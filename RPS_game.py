#!usr/local/bin
import random
import os

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    choices= {"player": player_choice.lower(), "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, the computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock, you lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "scissors cuts paper, you lose!"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors, you lose!"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
