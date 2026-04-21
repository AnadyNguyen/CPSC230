#puzzle east
import random
def greeting():
    global user_name, user_lives, user_coins

    print("Welcome to the Adventure Game!")
    user_name = input("What is your name? ")

    # Initialize stats
    user_lives = 4
    user_coins = 0

    print(f"\nHello {user_name}! You start with {user_lives} lives and {user_coins} coins.\n")


def puzzleE_sumdigits():
    global user_lives, user_coins, user_name

    print("\n--- Puzzle East: Sum of Digits ---")
    print(f"{user_name}, you will be shown a 4-digit number with no repeated digits.")
    print("Your task is to calculate the SUM of its digits.\n")

    # Generate a 4-digit number with NO repeated digits
    digits = list("0123456789")
    random.shuffle(digits)

    # Make sure the first digit isn't 0 (must be 1000–9999)
    if digits[0] == "0":
        digits[0], digits[1] = digits[1], digits[0]

    number_str = "".join(digits[:4])   # take the first 4 unique digits
    print("The number is:", number_str)

    # Calculate the sum using a FOR LOOP
    total_sum = 0
    for digit in number_str:
        total_sum += int(digit)        # add each digit to the sum

    # Ask the player for the answer
    while True:
        guess = input("What is the sum of its digits? ").strip()

        if not guess.isdigit():
            print("Please enter a NUMBER.")
            continue

        guess = int(guess)
        break

    # Check correctness
    if guess == total_sum:
        print("\nCorrect! You gain 5 coins.")
        user_coins += 5
        print("Coins:", user_coins)
        return True
    else:
        print("\nIncorrect!")
        print(f"The correct sum was: {total_sum}")
        user_coins -= 5
        user_lives -= 1
        print("You lose 5 coins and 1 life.")
        print("Lives left:", user_lives)
        return False
    
