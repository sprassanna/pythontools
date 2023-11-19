#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

finalNum = random.randint(1, 100)

level = input('Choose difficulty level: Easy or Hard: ').lower()

guessCount = 0

if (level == 'easy'):
    guessCount = 5
elif (level == 'hard'):
    guessCount = 10

print(guessCount)


# acual logic
def calculate(guessCount, finalNum):
    print(f'guess {guessCount} : finalNum {finalNum}')
    count = guessCount
    print(f'Starting count {count}')
    while (count > 0):
        userGuessedNum = int(input('Guess a Number between 1 to 100: '))
        if (userGuessedNum == finalNum):
            print("You guessed it right!")
            count = 0
        else:
            if (userGuessedNum < finalNum):
                print("Too low.")
            else:
                print('Too high')
            count = count - 1
            if (count == 0):
                print('You have used your life . You can crack it next time')
            print(f'Guess Again {count}')


calculate(guessCount, finalNum)
print(f'The Number was {finalNum}')
