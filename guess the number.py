import random

print('Greetings! hooman, im frosty, What is your name?', end='')
name = input()
print('Lets play a game, ' + name + ' guess my age between 1 and 10 in less than 3 tries!')
age = random.randint(1, 10)
for guessNumber in range(1, 4):
    print('take a guess:', end='')
    guess = int(input())
    if guess > age:
        print(str(guess) + ' is a little high')
    elif guess < age:
        print(str(guess) + ' is a little low')
    else:
        print('congratulations hooman u guessed it right ' + str(age))
        break
if age != guess:
    print('Nooo hooman!!! the number was: ' + str(age))

print('you took total of ' + str(guessNumber) + ' guesses!')
