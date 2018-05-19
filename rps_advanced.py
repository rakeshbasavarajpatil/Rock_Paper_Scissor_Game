from random import randint
player_wins = 0
computer_wins = 0
win_score = 2 #best of games

while player_wins < win_score and computer_wins < win_score:
	print(f"computer score: {computer_wins}...player score: {player_wins}")
	print("rock")
	print("paper")
	print("scissors")
	print("Game begins!!!")


	player = input("Make your move: ").lower()
	if player=="quit" or player=="q":    #just in case you don't want to play
		break

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
			computer_wins += 1
		elif computer == "scissors":
			print("Player wins!!!")
			player_wins += 1

	elif player == "paper":
		if computer == "scissors":
			print("Computer wins!!!")
			computer_wins += 1
		elif computer == "rock":
			print("Player wins!!!")
			player_wins += 1

	elif player == "scissors":
		if computer == "rock":
			print("Computer wins!!!")
			computer_wins += 1
		elif computer == "paper":
			print("Player wins!!!")
			player_wins += 1

	else:
		print("Please make a choice according to the game!!!")

if computer_wins< player_wins:
	print("Great job!! Well played you defeated the computer....Congrats.")
elif computer_wins==player_wins:
	print("It's a draw")
else:
	print("You lost!!! Come again and make better choices.")
