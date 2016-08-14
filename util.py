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
	dict = { 'question': question , 'option1' : option1 , 'option2' : option2 , 'option3' : option3 ,  'answer' : str(answer) , 'param1' : dic_add , 'param2' : dic_sub } 
	return dict 


def advacned_operation():
	dic_mult = easy_multiply()
	dic_div = easy_divide()
	dic_add = easy_addition()
	dic_sub = easy_subtraction()
	question = 'Solve the expression ( %s + %s )  + ( %s - %s ) + ( %s * %s ) + ( %s / %s )' %(dic_add["param1"], dic_add['param2'],dic_sub['param1'],dic_sub['param2'],dic_mult['param1'],dic_mult['param2'],dic_div['param1'],dic_div['param2']) 
	answer = (int(dic_add[param1]) + int(dic_add[param2])) + (int(dic_sub[param1]) - int(dic_sub[param2])) + (int(dic_mult[param1]) * int(dic_mult)[param2]) + ( int(dic_div[param1])/int(dic_div[param2]) )
	option1 = answer + 3
	option2 = answer + 5
	option3 = answer + 8
	array = [option1 , option2 ]
	array.insert(answer , randint(0,2))
	dict =  { }
	return dict
	#question = 'Solve the expression ' + str(med_add['param1']) + ' + '+  str(med_add['param2']) 
	#return question	


def linear_easy():
	a = randint(4,6)
	b = 1
	c = 1
	d = randint(1,4)
	e = randint(1,4)
	f = randint(5,10)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = 0 #e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = 0 #d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.23))  + ", " + ("{:.2f}".format(final_answer_2+0.23))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.57))  + ", " + ("{:.2f}".format(final_answer_2+0.57))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.73))  + ", " + ("{:.2f}".format(final_answer_2+0.73))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3, 'param1' : a , 'param2' : b, 'param3' : c, 'param4' : d, 'param5' : e, 'param6' : f}
	return dict


def linear_medium():
	a = 1
	b = randint(1,4)
	c = randint(-4,-1)
	d = 3
	e = randint(1,4)
	f = randint(-5,-1)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.34))  + ", " + ("{:.2f}".format(final_answer_2+0.34))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.53))  + ", " + ("{:.2f}".format(final_answer_2+0.53))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.77))  + ", " + ("{:.2f}".format(final_answer_2+0.77))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3, 'param1' : a , 'param2' : b, 'param3' : c, 'param4' : d, 'param5' : e, 'param6' : f}
	return dict

def linear_hard():
	a = randint(1,5)
	b = randint(1,5)
	c = randint(2,10)
	d = randint(1,5)
	e = randint(1,5)
	f = randint(1,5)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = 0 #e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = 0 #d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.3))  + ", " + ("{:.2f}".format(final_answer_2+0.3))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.4))  + ", " + ("{:.2f}".format(final_answer_2+0.4))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.5))  + ", " + ("{:.2f}".format(final_answer_2+0.5))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3, 'param1' : a , 'param2' : b, 'param3' : c, 'param4' : d, 'param5' : e, 'param6' : f}
	return dict


def quad_easy(): 


def quad_medium(): 


def quad_expert():

def trigo_easy(): 

def trigo_medium(): 

def trigo_hard():  
	'''