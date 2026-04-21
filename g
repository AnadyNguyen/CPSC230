def password_guessing():
    # 1. Predefined password
    password = "bat"   # Example: b (consonant), a (vowel), t (consonant)
    user_guess = "123"

    print("\nWelcome to the Password Guessing Game!")
    print("You have 5 attempts to guess a 3-letter password. Each digit represents a hidden letter.\n")
    print("Password placeholder for now:", user_guess)

    attempts = 5
    for attempt in range(1, attempts + 1):
        attempts -= 1
        print(f"\nAttempt #{attempt}:")
        position = input("Which position (1, 2, or 3) do you want to guess? ")
        if position not in ['1','2','3']:
            continue

        index = int(position) - 1
        letter = input("Guess the letter for position {}: ".format(position)).lower()

        if letter == password[index]:
            # Use replace() to update the guessed password
            user_guess = user_guess.replace(position, letter)
            print("Correct! Letter revealed.")
        else:
            print("Incorrect.")

        print("Password:", user_guess)

        # Win condition
        if user_guess == password:
            print("\nCongratulations! You guessed the password:", password)
            return True

    # Lose condition
        
    if attempts == 0:
        print("\nSorry, out of attempts! The password was:", password)
        return False

# To run the game:
password_guessing()