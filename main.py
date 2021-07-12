import random

main = ['rock', 'paper', 'scissors']

while True:
    user_input = input('User: ').lower()
    computer = random.choice(main)

    if user_input == computer:
        print(f'Computer: {computer}')
        print('---------- Tie ----------')
    elif user_input == 'rock':
        if computer == 'paper':
            print(f'Computer: {computer}')
            print('---------- Computer Win ----------')
        else:
            print(f'Computer: {computer}')
            print('---------- You Win ----------')
    elif user_input == 'paper':
        if computer == 'scissors':
            print(f'Computer: {computer}')
            print('---------- Computer Win ----------')
        else:
            print(f'Computer: {computer}')
            print('---------- You Win ----------')
    elif user_input == 'scissors':
        if computer == 'rock':
            print(f'Computer: {computer}')
            print('---------- Computer Win ----------')
        else:
            print(f'Computer: {computer}')
            print('---------- You Win ----------')
    
    if user_input == 'stop' or user_input == 'exit':
        break
