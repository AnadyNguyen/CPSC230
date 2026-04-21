player1_choice = input("Player 1, enter your choice (Rock, Paper, Scissors): ")
player2_choice = input("Player 2, enter your choice (Rock, Paper, Scissors): ")

# Define winning combinations as tuples
winning_pairs = [
    ("Rock", "Scissors"),
    ("Scissors", "Paper"),
    ("Paper", "Rock")
]

# Check for a tie
if player1_choice == player2_choice:
    print("It's a tie. One more time!")
# Check if Player 1 wins
elif (player1_choice, player2_choice) in winning_pairs:
    print(f"Player 1 wins! {player1_choice} beats {player2_choice}!")
# Otherwise, Player 2 wins
else:
    print(f"Player 2 wins! {player2_choice} beats {player1_choice}!")