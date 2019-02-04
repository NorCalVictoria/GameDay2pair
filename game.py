'''A number guessing game '''

from random import randint

print('Let\'s play a game !')

name = input('What is your name ? ')

def guess_num():
    play_again = 'y'
    best_score = 10000000000
    max_tries = 10

    while play_again == 'y':

        number = randint(1,100)
        # print(number) #TEST


        i = 0
        guess = int()

        while i < max_tries:
            i+=1

            while True:
                try:
                    guess = int(input('Guess my number between 1 and 100' ))
                    
                    break

                except ValueError:
                    print("That's not an INT ! Please enter a valid one")


            if guess > 100 or guess< 1:
                print('Try again . Only between 1 and 100 .')

            elif guess > number:
                print('Too high. Try a lower number.')

            elif guess < number:
                print('Too low. Try a higher number')

            else: 
                  print('Well done {} ! You found it in {} tries.'.format(name,i))
                  if i < best_score:
                      best_score = i
                  print('Your current best is {} tries.'.format(best_score))
                  break
        if i == max_tries:
            print("Too many attempts")
        play_again = input('Wanna give it another go ? (Y) or (N) ? ')


guess_num()

