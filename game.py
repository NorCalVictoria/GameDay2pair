"""A number-guessing game."""
print('Hello !')

input('What is your name?')

import random

rand = random.randint(1, 100)

user_guess = input("Guess a number.")

counter = 0

while user_guess != rand:
    try: 
        type(user_guess) != int or user_guess < 0 or user_guess > 100

        user_guess = input("Please enter a valid number between 1 and 100.")
        
        

#        if type(user_guess) != int:
#            print("I said a number please")
#        user_guess = int(input("Guess a number."))

    except:
        print("It's an exception.")
        break
'''    if  type(user_guess) != int:
        print("I said a number please")
        user_guess = int(input("Guess a number."))
    if user_guess > 100 or user_guess < 1:
        print("Enter a number between 1 and 100")
        user_guess = int(input("Guess a number."))

    elif user_guess < rand:
        print("choose a higher number")
        counter += 1
        user_guess = int(input("Guess a number."))

    elif user_guess > rand:
        print("choose a lower number")
        counter += 1
        user_guess = int(input("Guess a number."))


#if user_guess == rand:
print("Awesome ! You guessed it !")

print(counter)'''
