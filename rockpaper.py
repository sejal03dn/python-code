import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, or scissors (or 'q' to quit)")
        user = input("Your choice: ").lower()

        if user == 'q':
            print("Thanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

        if user not in options:
            print("Invalid choice. Try again.")
            continue
        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")

play_game()

