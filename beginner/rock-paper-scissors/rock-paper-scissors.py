import random
quit_list = ["quit"]
playable_list = ["rock", "paper", "scissors"]
winning_rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
user_score = 0
computer_score = 0
computer_string = "computer"
user_string = "user"

def check_winner():
    if user_score == computer_score: print("It's a draw")
    elif user_score > computer_score: 
        print("Congratulations YOU WIN!!!")
    else: print("Computer wins, better luck next time.")

def quit_game():
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")
    check_winner()

def point_winner_print(point_winner: str):
    if point_winner == "computer":
        print("Point to computer")
    else: 
        print("Point to player")

def display_score():
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")
    print("\n")

while True:
    user_input = input("Enter rock, paper, scissors to play a turn or quit: ").lower()
    if user_input in quit_list:
        quit_game()
        break
    elif user_input not in playable_list:
        print("Invalid input")
        continue
    
    computer_input = random.choice(playable_list)
    print(f"Computer played: {computer_input}")
    print(f"User played: {user_input}")

    if user_input == computer_input:
        print("Same options selected")
    elif winning_rules[user_input] == computer_input:
        user_score += 1
        point_winner_print(user_string)
    else:
        computer_score += 1
        point_winner_print(computer_string)

    display_score()
        

    
    

