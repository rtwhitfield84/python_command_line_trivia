import requests
import random
from values import *

def trivia():
	question_key = random.randrange(9000,10000)
	i = 1
	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'
					.format(question_key), headers=headers)

	print(" ************************ \n "  
		"Command Line Quiz Time! \n " 
		"************************")

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


	# while True:
	# 	try:
	# 		user_answer=int(input("Enter answer: "))

	# 		if choice==1:
	# 			kind()
	# 			break
	# 		elif choice==2:
	# 			mean()
	# 			break
	# 		elif choice==3:
	# 			weird()
	# 			break
	# 		elif choice==4:
	# 			funny()
	# 			break
	# 		elif choice==5:
	# 			fortune()
	# 			break
	# 		elif choice==6:
	# 			quit()
	# 			break
	# 		else:
	# 			print("Please enter a valid choice")
	# 	except ValueError:
	# 			print("Please enter a valid choice")
	# exit


trivia()