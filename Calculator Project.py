import calculatorart
print(calculatorart.logo)
# Creating an add function to do addition
def add(n1, n2):
    return n1 + n2
# Creating a sub function to do substraction
def sub(n1, n2):
    return n1 - n2
# Creating a mul function to do multiplication
def mul(n1, n2):
    return n1 * n2
# Creating a div functions to do Division
def div(n1, n2):
    return n1 /n2

# Creating dictionary to store all the operations
Operations = {""
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
game_over = True
# Using While loop to do repeated calculations
while game_over:
    previous_number = ""
    first_number =int(input("What's the first number? : ")).__float__()
    for symbol in Operations: # Using for loop to display the operators 
        print(symbol)
    math_operators =input("What's is a mathematical operator? : ")
    second_number = int(input("What's the next number? : ")).__float__()
    if math_operators in Operations: # Using the if to catch the operators 
        previous_value = Operations[math_operators](first_number, second_number) # Storing the values 
        print(previous_value)
        previous_number = previous_value
        Continue_or_not = input(f"Type 'y' to continue calculation {previous_number}, or 'n' to start new calculation ?: ").lower()
        if Continue_or_not == "n":
            print("\n"*20)
            print(calculatorart.logo)
        else:
            while Continue_or_not == 'y':
                second_number = int(input("What's the next number? : ")).__float__()
                in_use_number = (Operations["+"](previous_number,second_number))
                print(in_use_number)
                previous_number = in_use_number
                Continue_or_not = input(f"Type 'y' to continue calculation {previous_number}, or 'n' to start new calculation ?: ").lower()
                if Continue_or_not == 'n':
                    print("\n"*20)
                    print(calculatorart.logo)
                    game_over = True




