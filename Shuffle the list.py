from random import shuffle

def shuffle_list(mylist):
    '''
    shuffles my list
    '''
    shuffle(mylist)
    return mylist

def players_guess():
    guess = ''
    while guess not in [0,1,2]:
        guess = int(input("Pick a number: 0, 1, or 2:  "))
    return guess

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
        print(mylist)
    else:
        print('Wrong! Better luck next time')
        print(mylist)

# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = players_guess()

# Check User's Guess
check_guess(mixedup_list,guess)
