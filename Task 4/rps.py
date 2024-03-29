import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissor: ").lower()
        if user_choice in ['rock', 'paper', 'scissor']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissor.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"User's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"The {winner} wins!")

def play_again():
    return input("Do you want to play again? (y/n): ").lower() == 'y'

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"User's score: {user_score}")
        print(f"Computer's score: {computer_score}")

        if not play_again():
            print(f"User's score: {user_score}")
            print(f"Computer's score: {computer_score}")
            if user_score>computer_score:
                print("Congratulations! You won the game.")
            elif  user_score<computer_score:
                print("Better luck next time. The computer won this time.")
            else:
                print("It is a draw.")
            
            print("Bye Bye!")
            break

if __name__ == "__main__":
    main()
