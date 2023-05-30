import random

difficulty = 22

while True:
	a = random.randint(1, 9) * difficulty
	b = random.randint(1, 9) * difficulty

	answer = input(f'{a} + {b}? ')

	if(int(answer) == int(a + b)):
		print('Correct!')
	else:
		print('Wrong!')