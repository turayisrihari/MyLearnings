#v1
from random import choice


print("...........Welcome to the Game............")
print("...Rock.....")
print("...Paper.....")
print("...Scissor.....")

print("Please select Mode of playing: \n 1.Friends 2.Computer\n")

modeplay = input("Please enter the choise 1 or 2:  ").lower()

if int(modeplay) == 1:
	print("You are Player1\nYour Friend is Player2")
else:
	print("You are Player1\nComputer is Player2")

if int(modeplay) == 1:
	Player1 = input("Please enter your choise Player1:\t").lower()
	while Player1 not in ['rock','paper','scissor']:
		Player1 = input("you entered wrong choise, Please enter your choise Player1:\t").lower()

	Player2 = input("Please enter your choise Player2:\t").lower()
	while Player2 not in ['rock','paper','scissor']:
		Player2 = input("you entered wrong choise, Please enter your choise Player2:\t").lower()

else:
	Player1 = input("Please enter your choise Player1:\t").lower()
	while Player1 not in ['rock','paper','scissor']:
		Player1 = input("you entered wrong choise, Please enter your choise Player1:\t").lower()

	Player2 = choice(['Rock','Paper','Scissor']).lower()
	print("Please enter your choise Player2:\t" + Player2)


if Player1 == Player2:
	print("its a tie!")
elif Player1 == "rock":
	if Player2 == "paper":
		print("Player2 Wins!")
	else:
		print("Player1 Wins!")
elif Player1 == "paper":
	if Player2 == "rock":
		print("Player1 Wins!")
	else:
		print("Player2 Wins!")
elif Player1 == "scissor":
	if Player2 == "paper":
		print("Player1 Wins!")
	else:
		print("Player2 Wins!")
else:
	print("Something went wrong")

		

