def password_guessing(lives=3):
    # -------------------------------------
    # PREDEFINED PASSWORD (no randomness)
    # Must be consonant + vowel + consonant
    # -------------------------------------
    password = "bat"   # example: b (consonant), a (vowel), t (consonant)

    vowels = "aeiou"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    user_guess = "123"
    attempts = 5

    print("\nWelcome to the Password Guessing Game!")
    print("You have 5 attempts to guess the password.")
    print("Password placeholder:", user_guess)

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        print("Current guess:", user_guess)

        # Ask which position to guess
        pos = input("Which letter do you want to guess? (1, 2, or 3): ")

        if pos not in ["1", "2", "3"]:
            print("Invalid choice. Choose 1, 2, or 3.")
            continue

        pos = int(pos) - 1

        # Ask for the actual letter guess
        guess = input("Enter your guessed letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter.")
            continue

        # -----------------------------
        # CORRECT GUESS
        # -----------------------------
        if guess == password[pos]:
            print("Correct!")

            # update the masked password using replace()
            user_guess = user_guess.replace(user_guess[pos], guess, 1)

            print("Updated password:", user_guess)

            # Check win condition
            if user_guess == password:
                print("\n🎉 You guessed the password:", password)
                print("You move to the next game!")
                return True

        else:
            # WRONG GUESS → give hints
            print("Incorrect guess.")

            # Hint 1: vowel or consonant
            if password[pos] in vowels:
                print("Hint: The correct letter is a vowel.")
            else:
                print("Hint: The correct letter is a consonant.")

            # Hint 2: letter to the left in alphabet
            idx = alphabet.index(password[pos])
            if idx > 0:
                print(f"Hint: It is next to '{alphabet[idx - 1]}' in the alphabet.") or print(f"Hint: It is next to '{alphabet[idx + 1]}' in the alphabet.")

            attempts -= 1

    # -------------------------------------
    # FAILED ALL ATTEMPTS
    # -------------------------------------
    print("\n❌ You failed to guess the password:")
    print(f"You currently have {lives} lives.")

    retry = input("Do you want to try again? (yes/no): ").lower()

    if retry == "yes":
        lives -= 1
        print(f"You lost 1 life. Lives remaining: {lives}")

        if lives <= 0:
            print("No lives remaining. Goodbye!")
            exit()

        return password_guessing(lives)

    else:
        lives -= 2
        print(f"You lost 2 lives. Lives remaining: {lives}")

        if lives <= 0:
            print("No lives remaining. Goodbye!")
            exit()

        print("Proceeding to next game...")
        return False
password_guessing(lives=3)