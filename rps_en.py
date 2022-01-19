import random

while True:
	print('Rock, paper, scissors!')
	print('1. Play')
	print('2. Info')
	x = int(input('Enter nubmer: '))
	if x == 1:
		while True:
			userchoice = input('Rock, paper, scissors? ')
			userchoice = userchoice.lower()
			if userchoice == 'rock' or 'scissors' or 'scissors':
				cc = ['rock', 'paper', 'scissors']
				computercoice = random.choice(cc)
				if userchoice == computercoice:
					print('draw!')
				elif userchoice == 'rock' and computercoice == 'paper':
					print('lose, the computer has chosen paper')
				elif userchoice == 'rock'and computercoice == 'scissors':
					print('Win, computercoice chose scissors')
				elif userchoice == 'scissors' and computercoice == 'rock':
					print('loss, the computer has chosen rock')
				elif userchoice == 'scissors' and computercoice == 'paper':
					print('Win, computercoice chose paper')
				elif userchoice == 'paper' and computercoice == 'scissors':
					print('loss, computercoice chose scissors')
				elif userchoice == 'paper' and computercoice == 'rock':
					print('Win, the computer has chosen rock')
			else:
				print('Wrong choice entered, try again')
	elif x == 2:
		print('About the game:')
		print('Rock, paper, scissors is a popular hand game known in many countries around the world.')
		print('Often used as a way to draw lots to determine the order of turns in other games.')
		print('About:')
		print('This program is open source, uses open source information, and has its own repository on the github.')
		print('Made with love by Edges!')
		print('Sources:')
		print('Wikipedia: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C,_%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B,_%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0')



Translated with www.DeepL.com/Translator (free version)
