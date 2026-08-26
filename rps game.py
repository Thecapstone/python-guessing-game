import random

computer = ['rock', 'paper', 'scissors']
computer_choices = random.choice(computer)
max_tries = 4
no_of_plays = 0
lives = max_tries
score = 0

while lives != 0:
    user_choice = input('your turn: ')
    no_of_plays += 1
    lives -= no_of_plays
    if user_choice != computer_choices and lives != 0:
        print('try again')
        print(f'you have {lives} tries left')

    elif user_choice != computer_choices and lives == 0:
        print('you lose')
        break
    elif user_choice == computer_choices:
        score += 1
        print('Nice guess')
    print(f'you won {score}')
else:
    print('Game over')
