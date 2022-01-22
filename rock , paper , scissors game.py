import random
while True:

    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper , or scissors ? ").lower()

    if player == computer :
       print("computer - ",computer)
       print("player - ",player)
       print("TIE!!!!")

    elif player == "rock":
       if computer == "paper":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU LOSE!")
       if computer == "scissors":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU WIN !!")

    elif player == "scissors":
       if computer == "rock":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU LOSE!")
       if computer == "paper":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU WIN !!")

    elif player == "paper":
       if computer == "scissors":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU LOSE!")
       if computer == "rock":
        print("computer - ",computer)
        print("Player - ",player)
        print("YOU WIN !!")

    play_again = input("Play Again ? (yes/no) = ").lower()

    if play_again != "yes":
        break
print("bye")