import Numberguessart 
import random

numbers = list(range(1,101))
def starting_over():
    print(Numberguessart.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm Thinking of a number between 1 and 100. ")

def play_game(attempts):
    """
    This function runs the main number guessing game.
    It picks a random number between 1 and 100 and gives the player
    a certain number of attempts (based on difficulty) to guess it.

    For each guess:
    - It tells the player if the guess is too high, too low, or correct.
    - If the guess is right, it ends the game and shows a success message.
    - If the player runs out of attempts, it tells them the game is over.

    It also prints how many attempts are left after each wrong guess.
    Simple and fun logic to keep the game interactive!
    """
    random_number = random.choice(numbers)
   
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it the answer is {guess}")
            return
        elif guess < random_number:
            print("Too Low")
        else:
            print("Too High")
            
        attempts -=1
            
        if attempts > 0 :
            print("Guess again")
        else:
            print("You've run out of guess.Refresh the page to run again.")
            
starting_over()
difficulty = input("Choose a Difficulty . Type 'easy' or 'hard': ").lower()
if difficulty == 'easy': 
    play_game(10)
else:
    play_game(5)
