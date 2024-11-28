import random as r
options = ("rock","paper","scissors")
running = True

while running:
    computer = r.choice(options)
    player = None
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors): ")

    print(f"player-->{player}")
    print(f"computer-->{computer}")

    if player == computer:
        print("It's a tie!!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")
    play_again = input("Do you want to play again??(Y/N)").upper()
    if not play_again == "Y":
        running = False

print("Thanks For Playing!")