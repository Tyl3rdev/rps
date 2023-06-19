import random

def get_user_choice():
    """Get the user's choice (rock, paper, or scissors)"""
    while True:
        user_choice = input("Choose rock (r), paper (p), or scissors (s): ")
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_ai_choice():
    """Generate the AI's choice (rock, paper, or scissors)"""
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, ai_choice):
    """Determine the winner based on the choices made"""
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == 'r' and ai_choice == 's') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a round of rock-paper-scissors"""
    user_choice = get_user_choice()
    ai_choice = get_ai_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {ai_choice}")
    print(determine_winner(user_choice, ai_choice))

play_game()
