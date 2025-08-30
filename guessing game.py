import random

secret_number = random.randint(1, 10)
plays_made = 0
max_tries = 3


while plays_made != max_tries:
    player_guess = int(input("guess: "))
    plays_made += 1
    chances_left = max_tries - plays_made
    if player_guess > secret_number:
        print("Too big, try a smaller number")
    elif player_guess < secret_number:
        print('Too small, try a bigger number')
    elif player_guess == secret_number:
        print('Nice guess, you win!')
        break
    print(f"You have {chances_left} tries left")
else:
    print('You lose, try again next time')
    #break
    
    