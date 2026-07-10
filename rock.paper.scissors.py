import random


def get_choices():
    player_choice = input("enter a choice (rock, paper, scissor:) ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissor! You win!"
        else:
            return "paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You win"
        else:
            return "scissor cuts paper! You lose!"
    elif player == "scissor":
        if computer == "paper":
            return "scissor cuts paper! You win!"
        else:
            return "rock smashes scissor! You lose!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
