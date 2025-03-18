import random
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
user = input("play your choice: ").strip().lower()

print(f"you threw {user}, computer threw {computer} : ", end='')
if user not in  choice:
    print("invalid choice")
else:
    if computer == user:
        print("its a draw" )
    else:
        rp = ["rock", "paper"] #-> paper
        ps = ["paper", "scissors" ] #-> scissors 
        sr = ["scissors", "rock"] # -> rock 
        winner = None
        win = None
        if user in rp and computer in rp:
            win = "paper"
        elif user in ps and computer in ps:
            win = "scissors"
        elif user in sr and computer in sr:
            win = "rock"
        
        if win == computer:
            print("computer wins")
        else:
             print("you win")