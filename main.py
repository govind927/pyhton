import random

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "stone" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "stone"):
        return "Hurrah! , You win!!!"
    else:
        return "Oops! , Computer wins!!!"

# Options for the game
options = ["stone", "paper", "scissors"]

# Game loop
while True:
    print("\nStone Paper Scissors Game")
    print("Type 'stone', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")

    # User input
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice == "exit":
        print("Thank you for playing! Goodbye!")
        break
    
    if user_choice not in options:
        print("Invalid choice. Please choose 'stone', 'paper', or 'scissors'.")
        continue

    # Computer's choice
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
