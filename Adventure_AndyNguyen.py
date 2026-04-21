# Andy Nguyen Final Project
# CPSC230

import random
import sys

# Global player variables
user_name = ""
user_lives = 4
user_coins = 0


# Greeting function
def greeting():
    global user_name, user_lives, user_coins

    print("Welcome to the Adventure Game!")
    user_name = input("What is your name? ")

    user_lives = 4
    user_coins = 0

    print(f"\nHello {user_name}! You start with {user_lives} lives and {user_coins} coins.\n")

# Hint logic for password game
def give_hints(guess, correct_letter, vowels, alphabet):
    if correct_letter in vowels:
        print("Hint: It is a vowel.")
    else:
        print("Hint: It is a consonant.")

    guess_is_vowel = guess in vowels
    correct_is_vowel = correct_letter in vowels

    if guess_is_vowel == correct_is_vowel:
        idx = alphabet.index(correct_letter)
        if idx == 0:
            print("Hint: It is the first letter of the alphabet.")
        else:
            left_letter = alphabet[idx - 1]
            print(f"Hint: It is next to '{left_letter}' in the alphabet.")
    else:
        print("No additional hint this round.")


# PASSWORD GAME
def get_password():
    global user_lives, user_coins, user_name

    vowels = "aeiou"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = "can"
    user_guess = "123"
    
    print("Welcome to the Password Guessing Game!")
    print("You have 5 attempts to guess the 3-letter password.")
    print("Password format:", user_guess)

    attempts = 5

    while attempts > 0:
        print("Attempts remaining:", attempts)
        print("Current guess:", user_guess)

        position = input("Which letter position (1, 2, 3) do you want to guess?: ")
        if position not in ["1", "2", "3"]:
            print("Please enter a number of 1, 2, or 3.")
            continue

        position = int(position) - 1

        while True:
            guess = input("Enter your guessed letter: ").lower().strip()
            if guess == "" or len(guess) != 1 or not guess.isalpha():
                print("Enter ONE valid letter.")
                continue
            break

        if guess == password[position]:
            print("Correct letter!")
            user_guess = user_guess.replace(user_guess[position], guess, 1)
        else:
            print("Incorrect letter.")
            give_hints(guess, password[position], vowels, alphabet)

        if user_guess == password:
            print("You guessed the password:", password)
            return True

        attempts -= 1

    print("You failed the password game.")
    return False


# Puzzle North – Dice Game
def puzzleN_dice():
    global user_lives, user_coins, user_name

    print("\nPuzzle North: Dice Rolling")
    print(f"{user_name}, guess the number on a 12-sided die.")

    correct = random.randint(1, 12)

    while True:
        guess = input("Enter your guess (1-12): ").strip()
        if not guess.isdigit():
            print("Enter a number from 1 to 12.")
            continue

        guess = int(guess)
        if not (1 <= guess <= 12):
            print("Enter a valid number from 1 to 12.")
            continue

        break

    diff = abs(guess - correct)
    print("The die rolled:", correct)

    if diff <= 4:
        coins_gained = 5 - diff
        user_coins += coins_gained
        print(f"You earned {coins_gained} coins.")
        return True
    else:
        user_coins -= 5
        user_lives -= 1
        print("Too far off. You lose 5 coins and 1 life.")
        return False


# Puzzle South – Backwards Word
def puzzleS_backwards():
    global user_lives, user_coins, user_name

    print("\nPuzzle South: Backwards Word")
    print("Type the given word backwards.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = ""          # start with an empty string

    for i in range(4):     # loop 4 times
        word += random.choice(alphabet)

    print("Word:", word)

    answer = input("Backwards: ").strip().lower()
    correct = word[::-1]
    if answer.isalpha == False:
        print("Please type in letters only")
    if answer == correct:
        user_coins += 5
        print("Correct. You gain 5 coins.")
        return True
    else:
        user_coins -= 5
        user_lives -= 1
        print("Incorrect. You lose 5 coins and 1 life.")
        print("Correct backward version:", correct)
        return False


# Puzzle East – Sum of Digits
def puzzleE_sumdigits():
    global user_lives, user_coins, user_name

    print("\nPuzzle East: Sum of Digits")
    print("Calculate the sum of the digits.\n")

    digits = list("0123456789")
    random.shuffle(digits)

    if digits[0] == "0": 
        digits[0], digits[1] = digits[1], digits[0]

    num = "".join(digits[:4])
    print("Number:", num)

    total_sum = 0
    for d in num:
        total_sum += int(d)


    while True:
        guess = input("Sum of digits: ").strip()
        if not guess.isdigit():
            print("Enter a number.")
            continue
        guess = int(guess)
        break

    if guess == total_sum:
        user_coins += 5
        print("Correct. You gain 5 coins.")
        return True
    else:
        user_coins -= 5
        user_lives -= 1
        print("Incorrect. You lose 5 coins and 1 life.")
        print("Correct answer:", total_sum)
        return False


# Puzzle West – Treasure Chest
def puzzleW_treasure():
    global user_lives, user_coins, user_name

    print("\nPuzzle West: Maximize Your Treasure")
    print("Collect as much items as you can, without going over your total amount of coins.")
    print("To win the game, your total coins will have to be below the lowest item remaining in the chest.")

    inventory = {"sword": 40, "shield": 35, "potion": 25, "gold": 50, "gem": 60}
    treasures = []

    while True:
        print(f"\nCoins: {user_coins}")
        choice = input("Draw an item from the chest? (yes/no): ").lower().strip()

        if choice not in ["yes", "no"]:
            print("Type yes or no.")
            continue

        if choice == "yes":
            item = random.choice(list(inventory.keys()))
            value = inventory[item]
            print(f"You drew: {item} ({value} coins)")

            if user_coins >= value:
                user_coins -= value
                treasures.append(item)
                del inventory[item]

                if len(inventory) == 0:
                    print("You collected all items. You win Puzzle West.")
                    return True

            else:
                print("You cannot afford this. You lose 1 life.")
                user_lives -= 1
                return False

        else:
            lowest = min(inventory.values())

            if user_coins < lowest:
                print("You cannot afford anything else. You win Puzzle West.")
                return True
            else:
                print("You still have enough to buy something. You lose Puzzle West.")
                user_lives -= 1
                return False


# MAIN ADVENTURE GAME
def main():
    global user_lives, user_coins

    greeting()
#retry password
    result = get_password()

    while result is False:
        retry = input("Retry password game? (yes/no): ").lower()

        if retry not in ["yes", "no"]:
            print("Type yes or no.")
            continue

        if retry == "yes":
            user_lives -= 1
            print("You lost 1 life.")
            if user_lives <= 0:
                print("No lives remaining. Goodbye.")
                sys.exit()
            result = get_password()

        else:
            user_lives -= 2
            print("You lost 2 lives.")
            if user_lives <= 0:
                print("No lives remaining. Goodbye.")
                sys.exit()
            break
#after password game
    print("\nYou unlocked the Four Puzzles game.")
    user_coins += 100
    print("You received 100 coins.\n")

    puzzles_done = {"N": False, "S": False, "E": False, "W": False}

    while True:
        if user_lives <= 0:
            print("You lost all your lives. Goodbye.")
            sys.exit()

        if puzzles_done["N"] and puzzles_done["S"] and puzzles_done["E"]:
            print("\nOnly Puzzle West remains.")
            puzzleW_treasure()
            break

        direction = input("Choose a direction (N/S/E/W): ").upper().strip()

        if direction not in ["N", "S", "E", "W"]:
            print("Invalid direction.")
            continue

        if puzzles_done[direction]:
            print("You already completed that puzzle.")
            continue

        print(f"Lives: {user_lives}  Coins: {user_coins}")

        if direction == "N":
            puzzles_done["N"] = True
            puzzleN_dice()

        elif direction == "S":
            puzzles_done["S"] = True
            puzzleS_backwards()

        elif direction == "E":
            puzzles_done["E"] = True
            puzzleE_sumdigits()

        elif direction == "W":
            puzzles_done["W"] = True
            puzzleW_treasure()
            break

        print(f"Lives left: {user_lives}  Coins left: {user_coins}\n")

    print("\nAdventure Completed.")
    print("Final Lives:", user_lives)
    print("Final Coins:", user_coins)

#call main game function
main()


