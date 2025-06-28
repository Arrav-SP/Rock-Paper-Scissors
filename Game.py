import random

humanPoints = 0
compPoints = 0
points = input("Enter the number of points needed to win\n")
points = int(points)

while(humanPoints < points and compPoints < points):
    compTurn = random.choice(['R', 'P', 'S'])
    humanTurn = input("Enter your choice -\nR for Rock \nP for paper\nS for scissors\n").upper()

    # Print computer's choice
    print("Computer chose: " + compTurn)

    if (compTurn == humanTurn):
        pass  # tie, do nothing
    elif (compTurn == 'R' and humanTurn == 'P'):    
        humanPoints += 1
    elif (compTurn == 'S' and humanTurn == 'R'):
        humanPoints += 1
    elif (compTurn == 'P' and humanTurn == 'R'):
        compPoints += 1
    elif (compTurn == 'R' and humanTurn == 'S'):
        compPoints += 1
    elif (compTurn == 'S' and humanTurn == 'P'):
        compPoints += 1
    elif (compTurn == 'P' and humanTurn == 'S'):
        humanPoints += 1

    print("Your points: " + str(humanPoints))
    print("Computer points: " + str(compPoints))

if(compPoints>humanPoints):
    print("Better Luck Next Time 😊")
else:
    print("Congratulations!!!\nYou Won!!!🥳")
