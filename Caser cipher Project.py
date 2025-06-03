import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# created a function called caser and gave three inputs
def caser(original_text, shift_amount,encode_or_decode):
    cipher_text = ""
    #Using the if statement to check its encode or decode 
    if encode_or_decode =='decode':
        shift_amount *= -1 # Used the logic of if any positive number multiple with negative 1 it will give a negative value
    # Using for loop to go through each letter of user text and adding it to cipher_text
    for letter in original_text:
        # Using if statement to check if the letter entered is not in the alphabet list or not  &
        #if letter is not there it will directly adds the letter to cipher text 
        if letter not in alphabet:
            cipher_text += letter
        else:
        #Using shifted position to store the index and  to get the index of user text and 
        #using shift_amount to shift the index of user choice
            shifted_position = alphabet.index(letter) + shift_amount
            #Using module to stay in the len of alphabets
            shifted_position %= len(alphabet)
            #Adding the values of the the shifted_position to cipher_text
            cipher_text += alphabet[shifted_position] 
    print(f"Here is the {encode_or_decode}d result:{cipher_text}")


caser(original_text=text,shift_amount=shift,encode_or_decode=direction)
gameover = True
while gameover :
    user_input = input("Do you want to play this game again if yes type'yes' if no type'no':")
    if user_input == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caser(original_text=text,shift_amount=shift,encode_or_decode=direction)
    else:
        gameover = False
        print("Thank for playing the game ")
    


