import requests
import random
from values import *

def trivia():
	question_key = random.randrange(9000,10000)

	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'.format(question_key), headers=headers)

	print(r.text)


trivia()