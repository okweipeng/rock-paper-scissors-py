import random

# Function to get a valid player choice
def get_player_choice():
    while True:
        choice = input("Choose Rock, Paper, or Scissor: ").lower()
        if choice in ['rock', 'paper', 'scissor']:
            return choice
        print("Invalid choice! Try again.")

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if (player == 'rock' and computer == 'scissor') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissor' and computer == 'paper'):
        return "You win!"
    return "You lose!"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissor!")

    while True:
        player_choice = get_player_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissor'])

        print(f"You chose {player_choice}.")
        print(f"The computer chose {computer_choice}.\n")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result != "It's a tie!":
            break

if __name__ == "__main__":
    play_game()

