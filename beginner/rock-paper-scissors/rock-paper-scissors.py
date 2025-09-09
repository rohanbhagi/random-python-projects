import random
quit_list = ["quit", "q"]
playable_list = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0


def check_winner():
    if user_score == computer_score: print("It's a draw")
    if user_score > computer_score: 
        print("Congratulations YOU WIN!!!")
    
    else: print("Computer wins, better luck next time.")

def quit():
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")
    #check_winner()
    return 

while True:
    user_input = input("Enter rock, paper, scissors to play a turn or quit: ").lower()
    if user_input in quit_list:
        quit()
    elif user_input in playable_list:
        computer_input = random.choices(playable_list)
        print(f"Computer played: {computer_input}")
        print(f"User played: {user_input}")
        if ((user_input == "rock") and (computer_input == "paper")):
            computer_score += 1
        elif ((user_input == "paper") and (computer_input == "scissors")):
            computer_score += 1
        elif ((user_input == "scissors") and (computer_input == "rock")):
            computer_score += 1
        elif ((user_input == "rock") and (computer_input == "scissors")):
            user_score += 1
        elif ((user_input == "paper") and (computer_input == "rock")):
            user_score += 1
        elif ((user_input == "scissors") and (computer_input == "paper")):
            user_score += 1
        else:
            print("same option selected")
    else:
        print("Invalid input")

    
    

