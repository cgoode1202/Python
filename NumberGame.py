from random import randint
secret = randint(1,50)

print('Welcome!')

guess = 0
count = 0
max_allowed = 5

while guess != secret:
    if count == max_allowed:
        print("You've reached the maximum number of guesses.")
        print("The secret number is %d" % (secret))
        break
    guess = int(input('Please enter a number between 1 and 50: '))

    if guess == secret:
        print('You win!')
        break

    elif guess > secret:
        count += 1
        print('Your guess was too high.')

    else:
        count += 1
        print('Your guess was too low.')

print('Game over!')
