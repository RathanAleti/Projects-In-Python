import random
import hangman_art
import hangman_words

# Importing the Hangman words file and assign it to words 
words = hangman_words.word_list
images = hangman_art

#Importing the logo from hangman_art.py and print it at the start of the game
print(hangman_art.logo)

#Picking a random word from the words list
Random_word = random.choice(words)
print(Random_word)

# Declaring the placeholder variable empty because it can go through the word and generate
# as many blanks the rand word as 
Place_holder = ""

word_len = len(Random_word)
#Using For loop to generate as many blanks as letter in word
for x in range(word_len):
    Place_holder +=" _" 
print("Word to guess: " + Place_holder)
 
game_over = False #setting game over variable as False 
lives = 6 #Declaring lives variable and assign the value of 6
guess_letters = []# Creating a list called guess_letters to keep track of the guessed letter in the display

# Using while loop to ask the user to guess the correct word till there lives == 0
while not game_over:
    
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    # Asking the user to guess a word
    guess = input("Guess a letter to save a man: ").lower()
    
    # If the user guessed the letter twice , letting them know and also they don't lose there lives
    if guess in guess_letters:
        print(f"You've already guessed {guess}")
    
    display = ""
    #Using for loop to go through evert letter in Random_word variable

    for letters in Random_word:
        #if user guess the letter correct the letter will add to the display
        if letters == guess: 
            display += letters
            guess_letters.append(guess)
        # Checking if the letters are matching with the guess_letters values
        elif letters in guess_letters: 
            display += letters # If they match it will keep track of the previous guess letter by user

        else :
            display += " _"

    print("Word to guess: " + display)
    
    if guess not in Random_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"*********************** The Word is {Random_word} YOU LOSE**********************")

    if " _" not in display:
        game_over = True
        print("You win.")
    
    images = hangman_art.stages
    print(images[lives])

