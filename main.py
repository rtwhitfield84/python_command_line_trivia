import requests
import random
import os


def trivia():
	'''
		Main trivia gameplay function

		Vars:
			question_key - generates random number 
			realted to question primary key

			i - relates index number to correct answer and user choice

			r - api call to get trivia question

	'''
	question_key = random.randrange(9000,10000)
	i = 1
	r = requests.get('https://nugacityquestions.firebaseio.com/{}.json'
					.format(question_key))

	print("\n""************************* \n"  
		"Command Line Trivia Time! \n" 
		"*************************")

	print('Enter 9 to exit \n')

	for k,v in r.json().items():
		'''sets necessary gameplay values from json obj'''
		if str(k) == 'answer':
			correct_answer = v
		if str(k) == 'question':
			question = v
		if str(k) == 'choices':
			choices = v 
	print('Q: ' + question + '\n')


	for i, j in enumerate(choices):
		'''sets input value for correct answer'''
		if str(j) == correct_answer:
			correct_number = i + 1
			print('Choices:')

		'''prints answer choices'''
	for x,y in enumerate(choices):
	    print(x + 1, y + '\n')


	while True:
		'''enables continuous gameplay until user exits'''
		try:
			'''controls error'''
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
	'''clears terminal and alerts user of correct answer'''
	os.system("clear")
	os.system('say -v "Good News" "correct" -r 300')
	print("CORRECT! \n")
	trivia()
	
def wrong():
	'''clears terminal and alerts user of incorrect answer'''
	os.system("clear")
	os.system('say -v Deranged "wrong"')
	print("WRONG \n")
	trivia()
	
def quit():
	'''exits program'''
	os.system('say -v Zarvox "Goodbye" -r 300')
	exit

def welcome():
	'''voice prompt welcoming user to cl quiz'''
	os.system('say -v Zarvox "Welcome to command line trivia time" -r 300')

welcome()
trivia()