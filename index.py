import random

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

#TODO - Create a list containg 1 to 100, and with random chosse a number.
numbers = []
for num in range(1, 101):
    numbers.append(num)
chosen_number = random.choice(numbers)

#TODO - Ask the level (easy 10 chance | hard 5 chance)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Wrong input")

#TODO - Print attempts and get a guess, check the higher or lower or exact number and reduce attempts
while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You guessed it, my number was: {chosen_number}")
        break
    elif guess > chosen_number:
        print("Too high.")
        attempts -= 1
    elif chosen_number > guess:
        print("Too low.")
        attempts -= 1
    if attempts == 0:
        print("You have run out of guesses. Refresh the terminal to play again.")
        print(f"The choosen number was {chosen_number}")