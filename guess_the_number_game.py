import random
# Test

print('----------Guess the Number Game----------')

# Prompt a user to enter the both minimal and maximum numbers
min_num = int(input('Enter your minimal number\n>>> '))
max_num = int(input('Enter your maximum number\n>>> '))

# Check the requirment of min and max numbers (min_num <= max_num)
while max_num < min_num:
    print('Your maximum number should be greater than or equal to the minimal number')
    max_num = int(input('Enter your maximum number again\n>>> '))

# Generate the random number betwenn min_num and max_num
random_num = random.randint(min_num, max_num)

# Ask a user to enter the number he/she guesses
guess_num = int(input('Next, guess the number betwenn ' + str(min_num) + ' and ' + str(max_num) + "\n>>> "))

# Check whether guess_num is equal to random_num. A use has a three opportunities to answer.
for i in range(3):
    if (guess_num == random_num):
        print('Your won the game. Congratulations!')
        break
    elif (i == 2):
        print('You lose the game...')
    else:
        print('Your guess is incorrect. Remained opportunity: ' + str(2 - i))
        guess_num = int(input('Guess the number again\n>>> '))