import requests
import random
from values import *


def trivia():
	question_key = random.randrange(9000,10000)
	# score = 0
	i = 1
	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'
					.format(question_key), headers=headers)

	print(" ************************ \n "  
		"Command Line Quiz Time! \n " 
		"************************")
	# print('Score ' + str(score))
	print('Enter 9 to exit')

	for k,v in r.json().items():
		if str(k) == 'answer':
			correct_answer = v
		if str(k) == 'question':
			question = v
		if str(k) == 'choices':
			choices = v 
	print(question + '\n')
	print(correct_answer)
	print(choices)

	for i, j in enumerate(choices):
		if str(j) == correct_answer:
			correct_number = i + 1
			print(correct_number)

	for x,y in enumerate(choices):
	    print(x + 1, y + '\n')


	while True:
		try:
			user_answer=int(input("Enter answer: "))

			if user_answer==correct_number:
				right()
				break
			elif user_answer!=correct_number:
				wrong()
				break
			elif user_answer==9:
				quit()
			else:
				print("Please enter a valid choice")
		except ValueError:
				print("Please enter a valid choice")
	exit
def right():
	print("correct!")
	# score += 100
	trivia()
def wrong():
	print("wrong")
	# score -= 100
	trivia()
def quit():
	exit

trivia()