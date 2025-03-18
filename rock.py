import random
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
user = input("play your choice: ").strip().lower()

print(f"you threw {user}, computer threw {computer} : ", end='')
if user not in  choice:
    print("invalid choice")
elif computer == user:
    print("its a draw" )
elif user == "rock" and computer == "scissors":
    print("user wins")
elif user == "scissors" and computer == "rock":
    print("computer wins")
elif user == "rock" and computer == "paper":
    print("computer wins")
elif user == "paper" and computer == "rock":
    print("user wins")
elif user == "scissors" and computer == "paper":
    print("user wins")
elif user == "paper" and computer == "scissors":
    print("computer wins")