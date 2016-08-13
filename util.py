from random import randint
import random 

def easy_addition():
	a = randint(1,20)
	b = randint(1,20)
	question = 'Add the numbers ' + str(a) + ' and ' + str(b)
	answer = a + b 
	option1 = answer + randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer + randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) , 'param1' : a , 'param2' : b } 
	return dict 

def easy_subtraction():
	a = randint(20,50)
	b = randint(1,20)
	question = 'Subtract the numbers' + str(a) + ' and ' + str(b)
	answer = a - b 
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) ,'param1' : a , 'param2' : b } 
	return dict 

def easy_multiply(): 
	a = randint(1,20)
	b = randint(1,20)
	question = 'Multiply the numbers' + str(a) + ' and ' + str(b)
	answer = a * b 
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) , 'param1' : a , 'param2' : b } 
	return dict 

def easy_divide(): 
	a = randint(1,20)
	b = randint(40,60)
	answer = b/a
	question = 'Divide the numbers' + str(a) + ' and ' + str(b)
	while(b%a != 0):
		answer = b/a
		a = a + 1
	option1 = answer - randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer - randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) , 'param1' : a , 'param2' : b } 
	return dict 


def medium_operation():
	dic_add = easy_addition()
	dic_sub = easy_subtraction()
	question = 'Solve the  expression ' + str(dic_add['param1'])  + ' + ' + str(dic_add['param2']) + ' - ' + str(dic_sub['param1']) + ' - ' + str(dic_sub['param2']) 
	answer = dic_add['param1'] + dic_add['param2'] - dic_sub['param1'] - dic_sub['param2']
	param1 = dic_add['param1'] + dic_add['param2'] 
	param2 = dic_sub['param1'] - dic_sub['param2']
	option1 = answer + randint(1,3) 
	option2 = answer + randint(3,5) 
	option3 = answer + randint(5,7) 
	option4 = answer + randint(8,11)
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 , 'option4' : option4 , 'answer' : str(answer) , 'param1' : dic_add , 'param2' : dic_sub } 
	return dict 

'''
def advacned_operation():
	dic_mult = easy_multiply()
	dic_div = easy_divide()
	dic_add = easy_addition()
	dic_sub = easy_subtraction()
	#question = 'Solve the expression ' + str(med_add['param1']) + ' + '+  str(med_add['param2']) 
	#return question	


def linear_easy():
	a = randint(1,5)
	b = 1
	c = 0
	d = randint(1,5)
	e = randint(1,5)
	f = randint(1,5)
	question = 'Subtract the numbers' + str(a) + ' and ' + str(b)
	answer_1 = b*f
	answer_2 = e*c
	answer_3 = e*a
	answer_4 = b*d
	final_answer = (answer_1 - answer_2) / (answer_3 - answer_4)



def linear_medium():
	a = randint(1,5)
	b = 1
	c = randint(1,5)
	d = randint(1,5)
	e = randint(1,5)
	f = randint(1,3)


def linear_hard():
	a = randint(1,5)
	b = randint(1,5)
	c = randint(2,10)
	d = randint(1,5)
	e = randint(1,5)
	f = randint(1,5)


def quad_easy(): 


def quad_medium(): 


def quad_expert():

def trigo_easy(): 

def trigo_medium(): 

def trigo_hard():  
	'''