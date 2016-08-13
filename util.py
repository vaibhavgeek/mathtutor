from random import randint

def easy_addition():
	a = randint(1,20)
	b = randint(1,20)
	question = 'Add the numbers' + str(a) + ' and ' + str(b)
	answer = a + b 
	option1 = answer + randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer + randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) } 
	return dict 

def easy_subtraction():
	a = randint(1,20)
	b = randint(1,20)
	question = 'Add the numbers' + str(a) + ' and ' + str(b)
	answer = a - b 
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) } 
	return dict 

def easy_multiply(): 
	a = randint(1,20)
	b = randint(1,20)
	question = 'Add the numbers' + str(a) + ' and ' + str(b)
	answer = a * b 
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) } 
	return dict 

def easy_divide(): 
	a = randint(1,20)
	b = randint(40,60)
	question = 'Add the numbers' + str(a) + ' and ' + str(b)
	while(b%a == 0):
		answer = b/a
		a = a + 1
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) } 
	return dict 


def medium_operation():


def advacned_operation


def linear_easy


def linear_medium 


def linear_hard 


def quad_easy 


def quad_medium 


def quad_expert 

def trigo_easy 

def trigo_medium 

def trigo_hard  