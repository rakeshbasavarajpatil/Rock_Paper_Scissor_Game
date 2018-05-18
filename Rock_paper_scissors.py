from random import randint

player = input("Make your move: ").lower()

random_number = randint(0,2)
if random_number==0:
	computer = "rock"
elif random_number==1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer selects {computer}")

if computer == player:
	print("It's a draw")

elif player == "rock":
	if computer == "paper":
		print("Computer wins!!!")
	elif computer == "scissors":
		print("Player wins!!!")

elif player == "paper":
	if computer == "scissors":
		print("Computer wins!!!")
	elif computer == "rock":
		print("Player wins!!!")

elif player == "scissors":
	if computer == "rock":
		print("Computer wins!!!")
	elif computer == "paper":
		print("Player wins!!!")

else:
	print("Please make a choice according to the game!!!")
