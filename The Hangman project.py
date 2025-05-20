import random
images = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# List words as city names 
words = ["barcelona","newyork","kansas","hyderabad"]
Random_word = random.choice(words)#Picking a random word from the words list 
print (Random_word)

# Declaring the placeholder variable empty because it can go through the word and generate
# as many blanks the rand word as 
Place_holder = ""

word_len = len(Random_word)
#Using For loop to generate as many blanks as letter in word
for x in range(word_len):
    Place_holder +=" _" 
print(Place_holder)


#setting game over variable as False 
game_over = False
lives = 6
# Creating a list called guess_letters to keep track of the guessed letter in the display
guess_letters = []
# Using while loop to ask the user to guess the correct word till there lives == 0
while not game_over:
    display = ""
    # Asking the user to guess a word
    guess = input("Guess a [letter to save a man: ").lower()
    #Using for loop to go through evert letter in Random_word variable
    for letters in Random_word:
        if letters == guess: #if user guess the letter correct the letter will add to the display
            display += letters
            guess_letters.append(guess)
        elif letters in guess_letters: # Checking if the letters are matching with the guess_letters values
            display += letters # If they match it will keep track of the previous guess letter by user
        else :
            display += " _"

    print(display)
    if guess not in Random_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You lose")

    elif " _" not in display:
        game_over = True
        print("You win.")

    print(images[lives])

