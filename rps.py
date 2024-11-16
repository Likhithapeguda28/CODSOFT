import random
player1=str(input("Rock, Paper, or Scissors?")).capitalize()
player2=random.randint(1,3)
if player2==1:
    player2="Rock"
elif player2==2:
    player2="Paper"
elif player2==3:
    player2="Scissors"

print("computer:", player2)
if player1==player2:
    print("it's a tie...!!")
elif (player1=="Rock" and player2=="Scissors") or (player1=="Paper" and player2=="Rock") or (player1=="Scissors" and player2=="Paper"):
    print("you Win...!!")
else:
    print("Computer wins...!!")            