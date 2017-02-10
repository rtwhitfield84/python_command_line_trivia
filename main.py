import requests
import random
import os

# need to persist score
# perhaps write to text file

def trivia(score):
	question_key = random.randrange(9000,10000)
	i = 1
	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'
					.format(question_key))

	print(" ************************ \n "  
		"Command Line Quiz Time! \n " 
		"************************")
	print('Score ' + str(score))
	print('Enter 9 to exit \n')

	for k,v in r.json().items():
		if str(k) == 'answer':
			correct_answer = v
		if str(k) == 'question':
			question = v
		if str(k) == 'choices':
			choices = v 
	print('Q: ' + question + '\n')


	for i, j in enumerate(choices):
		if str(j) == correct_answer:
			correct_number = i + 1
			print('Choices:')

	for x,y in enumerate(choices):
	    print(x + 1, y + '\n')


	while True:
		try:
			user_answer=int(input("Enter answer: "))

			if user_answer==correct_number:
				right()
				break
			elif user_answer==9:
				quit()
				break
			elif user_answer!=correct_number:
				wrong()
				break
			else:
				print("Please enter a valid choice")
		except ValueError:
				print("Please enter a valid choice")
	exit
	
def right():
	os.system("clear")
	os.system('say -v "Good News" "correct" -r 300')

	print("CORRECT! \n")
	trivia( 100)
	
def wrong():
	os.system("clear")
	os.system('say -v Deranged "wrong"')
	print("WRONG \n")
	trivia( -100)
	
def quit():
	exit

def welcome():
	os.system('say -v Zarvox "Welcome to the command line quiz" -r 300')

welcome()
trivia(0)