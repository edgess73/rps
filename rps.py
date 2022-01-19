import random

# Меню
	print('Камень, ножницы, бумага!')
	print('1. Играть')
	print('2. Инфо')
	x = int(input('Введите число: '))
	
	if x == 1: # Игра
		while True:
			userchoice = input('Камень, ножницы или бумага? ')
			userchoice = userchoice.lower()
			if userchoice == 'камень' or 'ножницы' or 'бумага':
				cc = ['камень', 'ножницы', 'бумага']
				computercoice = random.choice(cc)
				if userchoice == computercoice:
					print('Ничья!')
				elif userchoice == 'камень' and computercoice == 'бумага':
					print('Проигрыш, компьютер выбрал бумага')
				elif userchoice == 'камень'and computercoice == 'ножницы':
					print('Победа, компьютер выбрал ножницы')
				elif userchoice == 'ножницы' and computercoice == 'камень':
					print('Проигрыш, компьютер выбрал камень')
				elif userchoice == 'ножницы' and computercoice == 'бумага':
					print('Победа, компьютер выбрал бумага')
				elif userchoice == 'бумага' and computercoice == 'ножницы':
					print('Проигрыш, компьютер выбрал ножницы')
				elif userchoice == 'бумага' and computercoice == 'камень':
					print('Победа, компьютер выбрал камень')
			else:
				print('Неправильно введён выбор, попробуйте заново')
				
	elif x == 2: # Инфо
		print('О игре:')
		print('Камень, ножницы, бумага — популярная игра на руках, известная во многих странах мира.')
		print('Часто используется как способ жеребьёвки для определения очерёдности хода в других играх.')
		print('О программе:')
		print('Данная программа имеет открытый исходный код, использует открытые источники информации и имеет свой репозиторий на гитхабе.')
		print('Made with love by Edges!')
		print('Источники:')
		print('Wikipedia: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C,_%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B,_%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0')
