import random


def welcome():
    player = input("What is your name? ")
    print(f"Welcome to the Number Guessing Game {player}!")
    return player


def create_new_number(to_number):
    number = random.randint(1, to_number)
    return number


def get_to_number():
    while True:
        try:
            to_number = int(input(f"Please select the max number for the guessing range (between 1 and __):  "))
            break
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
    return to_number


def check_highscore(highscore, current_score):
    if highscore == 0 or current_score < highscore:
        highscore = current_score
    return highscore


def get_guess(current_guess, to_number):
    while True:
        try:
            player_guess = int(input(f"Current Guess: {current_guess}      Guess a number between 1 and {to_number}:  "))
            if player_guess < 1 or player_guess > to_number:
                raise ValueError
            break
        except ValueError as e:
            print(f"Error: Invalid input. Please enter a number between 1 and {to_number}")
    return player_guess


def player_feedback(winning_number, player_guess):
    if player_guess < winning_number:
        print(f"The answer is HIGHER than your guess of {player_guess}")
    if player_guess > winning_number:
        print(f"The answer is LOWER than your guess of {player_guess}")


def end_game():
    print(f"Thanks for playing! Goodbye")
    exit()

