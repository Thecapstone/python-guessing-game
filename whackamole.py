import random

h1 = "🕳️"
h2 = "🕳️"
h3 = "🕳️"
h4 = "🕳️"


mole_holes = ['h1', 'h2', 'h3', 'h4']
mole = '🐀'

no_of_plays = 0
max_tries = 5

user_guide = "select the hole you think the mole is in i.e, h1, h2, h3, h4."
print(user_guide)

while no_of_plays != max_tries:
    user_move = input('Whack the mole: ')
    no_of_plays += 1
    lives = max_tries - no_of_plays
    mole_current_position = random.choice(mole_holes)
    if user_move == mole_current_position:
        print('You squashed the mole')
        print(f'Lives: {lives} left')
    else:
        print('Try again')
        print(f'Lives: {lives} left')

else:
    print('Game Over')