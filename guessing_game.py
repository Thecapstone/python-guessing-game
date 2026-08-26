
import random
import shutil
import subprocess
from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-l", 
    "--lives", 
    dest="lives",
    type=int,
    help="Remaining chances a player has",
    default=3
)
(options, args) = parser.parse_args()


def initialize():
    print(
                "This is a 2d game. \n"
                "It was built to understand terminal integration with simple code \n"
                "The user is expected to guess numbers at random \n"
            )
    
    image="/mnt/c/Users/HP/Downloads/question_mark.jpg"
    width=80

    if not shutil.which("jp2a"):
        print("Error: 'jp2a' command not found. Please install it on your os first.")
        return
    try:
        cmd = ["jp2a", f"--width={width}", image]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running jp2a: {e.stderr}")
    except Exception as e:
        return f"An unexpected error occurred {str(e)}"

def play():

    secret_number = random.randint(1, 10) 
    plays_made = 0
    max_tries = options.lives

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
    

if not args:
    parser.error("You must provide a command: either init or play")

command = args[0]

if command == "init":
    initialize()
elif command == "play":
    play()
else:
    parser.error(f"Unknown command: {command}")