"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from utilities import *


def new_game(highscore, debug):
    current_guess = 0
    print("\n--- Let's Begin ---")
    print(f"The current highscore is {highscore}")

    to_number = get_to_number()
    winning_number = create_new_number(to_number)
    if debug:
        print(winning_number)

    while True:
        current_guess += 1
        player_guess = get_guess(current_guess, to_number)
        if player_guess == winning_number:
            print(f"Congratulations You Got it! The number was {winning_number} and it took you {current_guess} guesses")
            current_score = current_guess
            return current_score
        else:
            player_feedback(winning_number, player_guess)


def start_game(debug_state):
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    highscore = 0
    keep_playing = True

    player = welcome()

    while keep_playing:
        current_score = new_game(highscore, debug_state)
        highscore = check_highscore(highscore, current_score)

        play_again = input(f"\n{player} - Would you like to play again? Yes to continue anything else to exit: ")
        if play_again.lower() == "yes" or play_again.lower() == "y":
            print("\n")

        else:
            end_game()


# Kick off the program by calling the start_game function.
start_game(debug_state=True)

