#puzzle south backwards
import random
def greeting():
    global user_name, user_lives, user_coins

    print("Welcome to the Adventure Game!")
    user_name = input("What is your name? ")

    # Initialize stats
    user_lives = 4
    user_coins = 0

    print(f"\nHello {user_name}! You start with {user_lives} lives and {user_coins} coins.\n")


def puzzleS_backwards():
    global user_lives, user_coins, user_name

    print("\n--- Puzzle South: BACKWARDS ---")
    print(f"{user_name}, you will be shown a random 4-letter word.")
    print("Your task is to type that word BACKWARD.\n")

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Generate random 4-letter word
    word = ""
    for _ in range(4):
        word += random.choice(alphabet)

    print(f"The word is:  {word}")

    # Ask user for input
    answer = input("Type the word backward: ").strip().lower()

    # Compute the correct backward version
    correct_backward = word[::-1]

    # Check correctness
    if answer == correct_backward:
        print("\nCorrect! You gain 5 coins.")
        user_coins += 5
        print(f"Coins: {user_coins}")
        return True
    else:
        print("\nIncorrect!")
        print(f"The correct backward version was: {correct_backward}")
        user_coins -= 5
        user_lives -= 1
        print("You lose 5 coins and 1 life.")
        print(f"Lives left: {user_lives}")
        print(f"Coins left: {user_coins}")
        return False
    

greeting()
puzzleS_backwards()