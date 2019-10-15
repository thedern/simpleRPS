from random import randint
player_score = 0
computer_score = 0


print("###################################################")
print("### ROCK PAPER SCISSORS ###########################")
print("###################################################\n")

# game is a loop and continues until user decides to quit
while True:
    # step 1: get player's choice from input
    player1 = input("enter rock(r), paper(p), scissors(s), or 'end' to quit: \n")

    # step 2: determine if user input is valid
    if player1 not in ['r', 'p', 's', 'end']:
        print("please enter a valid choice from displayed options\n")

    # step 3:  assign r, p, s, to words
    else:
        if player1 == 'r':
            player1 = 'rock'
        elif player1 == 'p':
            player1 = 'paper'
        elif player1 == 's':
            player1 = 'scissors'

        print("you entered '{}'  \n".format(player1))

        # step 4: check if player entered 'end', quit game
        if player1 == "end":
            break
        else:
            # step 5:  use random number generator to get computer pick
            num = randint(0,2)
            if num == 0:
                computer = 'rock'
            elif num == 1:
                computer = 'paper'
            elif num == 2:
                computer = 'scissors'

            print("the computer chose '{}' \n".format(computer))
       
            # step 6:  compare user and compter input and update score

            # player wins statements
            if player1 == 'rock' and computer == 'scissors':
                player_score +=1
                print("rock smashes scissors!, you win!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score)) 

            elif player1 == 'scissors' and computer == 'paper':
                player_score +=1
                print("scissors cuts paper!, you win!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score))

            elif player1 == 'paper' and computer == 'rock':
                player_score +=1
                print("paper covers rock!, you win!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score))

            # computer wins statements
            elif player1 == 'scissors' and computer == 'rock':
                computer_score +=1
                print("rock smashes scissors!, you loose!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score))

            elif player1 == 'paper' and computer == 'scissors':
                computer_score +=1
                print("scissors cuts paper!, you loose!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score))

            elif player1 == 'rock' and computer == 'paper':
                computer_score +=1
                print("paper covers rock!, you loose!")
                print("your score: {}, computer score {}\n".format(player_score, computer_score))
            
            # draw game statements
            elif player1 == 'paper' and computer == 'paper': 
                print("its a draw!!!!\n")

            elif player1 == 'scissors' and computer == 'scissors':
                print("its a draw!!!!\n")

            elif player1 == 'rock' and computer == 'rock':
                print("its a draw!!!!\n")


















