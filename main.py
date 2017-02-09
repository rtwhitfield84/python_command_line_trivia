import requests
import random
from values import *

def trivia():
	question_key = random.randrange(9000,10000)

	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'.format(question_key), headers=headers)

	for k,v in r.json().items():
		print(k,v)
	# print(r.json().keys())


trivia()