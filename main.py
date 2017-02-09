import requests
import random
from values import *

def trivia():
	question_key = random.randrange(9000,10000)

	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'
					.format(question_key), headers=headers)

	print(" ************************ \n "  
		"Command Line Quiz Time! \n " 
		"************************")
	# print("1. Moo something kind")
	# print("2. Moo something mean")
	# print("3. Moo something weird")
	# print("4. Moo something funny")
	# print("5. Moo your fortune")
	# print("6. Quit")

	for k,v in r.json().items():
		if str(k) == 'answer':
			answer = v
		if str(k) == 'question':
			question = v
		if str(k) == 'choices':
			choices = v 
	print(question)
	print(choices)
	print(answer)
	# print(r.json().keys())


trivia()