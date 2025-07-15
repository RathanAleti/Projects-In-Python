import random
from game_data import data
from Higher_or_Lower_Art import logo ,vs
# This function just prints the logo from Higher_or_Lower_Art module at the start of the game
def display(): 
    print(logo)
# This function picks a random person (dictionary) from the data list
def gets_random_person():
    return random.choice(data)
'''
This function prints the formatted info of a person
It includes the label (A or B), name, description, and country
'''
def format_data(person,label):
    name = person['name']
    description = person['description']
    country = person['country']
    print(f"Compare {label}: {name}, a {description} from {country}")
    
# This is the main game function
def game():
    score = 0 # This keeps track of how many correct guesses the user made
    game_over = False # this will control the game while loop
    person_a = gets_random_person() # This will be choosing random person for Compare A
    display()  # This shows the logo before the game starts
    # This while loop runs until the user makes a wrong guess
    while not game_over:
        person_b = gets_random_person()  # It chooses another random person for Compare B
        # This loop makes sure person B is not the same as person A 
        while person_b == person_a:
            person_b = gets_random_person()
         # This will show both people's information to the user by using the format_data function
        format_data(person_a,'A')
        print(vs)
        format_data(person_b,'B')
         # This will ask the user to guess who has more followers 
        user_input = input("who has more followers? Type 'A' or 'B':").lower()
        # Gets the follower counts for both persons
        followers_a = person_a['follower_count']
        followers_b = person_b['follower_count']
        '''
        This line is creating a variable called 'is_correct' which will be either True or False.
        It checks if the user's input ('a' or 'b') matches the person who has more followers.
        If the user typed 'a', then it will be checking:
        if person A's follower count greater than person B's?
        If yes, then the user's guess is correct ,so 'is_correct' becomes True.
        
        OR, if the user typed 'b', then it will check:
        is person B's follower count greater than person A's?
        If yes, then the user's guess is correct ,so 'is_correct' becomes True.

        If neither of those conditions are true, then the guess was wrong,
        and `is_correct` becomes False.

       This variable helps us decide in the next step whether to:
       continue the game and increase the score (if 'is_correct' is True) then it will continue
       or it ends the game (if 'is_correct' is False)

        '''
        is_correct = (
                (user_input == 'a' and followers_a > followers_b) or
                (user_input == 'b' and followers_b > followers_a)
        )
        if is_correct :
            score +=1
            print(f"You're right! Current score: {score}\n")
            person_a = person_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


game()