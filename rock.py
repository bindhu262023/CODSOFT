import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type rock, paper, or scissors to play.")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score ➤ You: {user_score} | Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🎉 Final Score ➤ You:", user_score, "| Computer:", computer_score)
            print("Thanks for playing!")
            break

        round_number += 1


play_game()
