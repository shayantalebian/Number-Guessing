import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():

        

    art = r"""
    ___                                                               _               
    / _ \_   _  ___  ___ ___   _ __ ___  _   _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
    / /_\/ | | |/ _ \/ __/ __| | '_ ` _ \| | | | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\| |_| |  __/\__ \__ \ | | | | | | |_| | | | | | |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/ |_| |_| |_|\__, | |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                        |___/                                         
    """
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()