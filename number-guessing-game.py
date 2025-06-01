import random

max_attempts = 0
score = 1000
continue_game = True

def get_difficulty_level():
    try:
        print("Select the difficulty level from below options:")
        print("1. Easy : Number between 1-50")
        print("2. Moderate : Number between 1-100")
        print("3. Difficult : Number between 1-500")
        level = int(input("Enter the difficulty level: "))
        return level
    except:
        print("Invalid Input")
        return 0

def get_random_number(level):
    global max_attempts
    if level == 1:
        max_attempts = 4
        return random.randint(1, 50)
    elif level == 2:
        max_attempts = 8
        return random.randint(1, 100)
    elif level == 3:
        max_attempts = 10
        return random.randint(1, 500)
    else:
        return 0

def guess_the_number(rand_num):
    global max_attempts
    global score
    if max_attempts == 1:
        print(f"You have only {max_attempts} attempt")
    else:
        print(f"You have {max_attempts} attempts")
    try:
        num = int(input("Guess the number: "))

        if num > rand_num:
            max_attempts = max_attempts - 1
            score = score - 100
            print("The number guessed is higher")
        elif num < rand_num:
            max_attempts = max_attempts - 1
            score = score - 100
            print("The number guessed is lower")
        else:
            print("Yay! Congrats! The number guessed in correct!")
            record_score()
            continue_the_game()
    except:
        print("Invalid number")

def record_score():
    name = input("Enter your name: ")
    try:
        f = open("player-scores.txt", 'a')
        f.write(name + "|" + str(score) + "\n")
        f.close()
        print(f"The score for {name} is recorded successfully!")
    except FileNotFoundError as fnfe:
        print("File not found!")

def continue_the_game():
    global continue_game
    wish_to_continue = input("Do you wish to continue the game? (y/n): ").lower()
    if wish_to_continue == 'y':
        main()
    elif wish_to_continue == 'n':
        print("Thanks for playing the game!")
        continue_game = False
    else:
        print("Please enter y / n")
        continue_the_game()


def main():
    level = get_difficulty_level()
    if level in range(1, 4):
        random_num = get_random_number(level)
        while(continue_game):
            if max_attempts == 0:
                print("Your max attempts is over!")
                continue_the_game()
            else:
                guess_the_number(random_num)
    else:
        main()

print("Welcome to Number Guessing Game!")
main()