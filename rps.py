import random

while True:
	print('Камень, ножницы, бумага!')
	print('1. Играть')
	print('2. Инфо')
	x = int(input('Введите число: '))
	if x == 1:
		while True:
			print('!!!Просьба писать с заглавной буквы!!!')
			userchoice = input('Камень, ножницы или бумага? ')
			if userchoice == 'Камень' or 'Ножницы' or 'Бумага':
				cc = ['Камень', 'Ножницы', 'Бумага']
				computercoice = random.choice(cc)
				if userchoice == computercoice:
					print('Ничья!')
				elif userchoice == 'Камень' and computercoice == 'Бумага':
					print('Проигрыш, компьютер выбрал', computercoice)
				elif userchoice == 'Камень'and computercoice == 'Ножницы':
					print('Победа, компьютер выбрал', computercoice)
				elif userchoice == 'Ножницы' and computercoice == 'Камень':
					print('Проигрыш, компьютер выбрал', computercoice)
				elif userchoice == 'Ножницы' and computercoice == 'Бумага':
					print('Победа, компьютер выбрал', computercoice)
				elif userchoice == 'Бумага' and computercoice == 'Ножницы':
					print('Проигрыш, компьютер выбрал', computercoice)
				elif userchoice == 'Бумага' and computercoice == 'Камень':
					print('Победа, компьютер выбрал', computercoice)
			else:
				print('Неправильно введён выбор, попробуйте заново')
	elif x == 2:
		print('О игре:')
		print('Камень, ножницы, бумага — популярная игра на руках, известная во многих странах мира.')
		print('Часто используется как способ жеребьёвки для определения очерёдности хода в других играх.')
		print('О программе:')
		print('Данная программа имеет открытый исходный код, использует открытые источники информации и имеет свой репозиторий на гитхабе.')
		print('Made with love by Edges!')
		print('Источники:')
		print('Wikipedia: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C,_%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B,_%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0')
