import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose rock/paper/scissors or 'q' to quit: ").lower()
    
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif (
        (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("Final Score:")
print(f"You: {user_wins} wins")
print(f"Computer: {computer_wins} wins")
print("Goodbye!")
