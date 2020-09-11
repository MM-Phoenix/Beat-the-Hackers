#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27  10:30:25 2020

@author: Phoenix
"""


import random
import sys

WELCOME = "\nWelcome to Password Generator\n"
START = "Enter \"OK\" to generate your unique password.\nEnter \"QUIT\" to exit the program.\n"
CONTINUE = ["ok", "okay", "yes", "yep", "yeah", "y", "continue", "c"]
EXIT = ["nope", "no", "n", "non", "ni", "exit", "e", "quit", "q"]
BYE = ["Bye Bye!", "See you soon!", "Goodbye!", "See ya!", "Take care"]
WRONG_COMAND = "\nI didn't understand your input.\n"
AGAIN = "Do you want to generate another password?\n"
CLICKS = "\nYou will get a strong password in a few clicks\n"
REMEMBER = "Remember, a strong password should be at least 16 characters long. "

ENTER1 = "Please, enter the desired length of your password. (16-50)\n"
ENTER2 = "Please, enter a length between 16 and 50\n"
ENTER3 = "Please, try again. "
WEAK = "Your password would be too weak! You don't want hackers to log in to your account."
NO_WAY = "No way! Length should be an integer number between 16 and 50."
LONG = "Okay you want a really strong password, but this is too much!"

DECORATION = "\n" + "~ " * 40 + "\n"
YOUR_PASS = "\nYour unique unbeatable password, {} charactes long:\n\n"

ALPHA = "qwertyuiopasdfghjklzxcvbnm"
SYM = "!@#$%^&*()-=_+[];',.<>?:{}"
NUMS = "1234567890"
#---------------------------------------------------------------------------------------------
def start():
    comand = (raw_input(START)).lower()
    while comand in CONTINUE:
        decorate(CLICKS)
        length = get_length(REMEMBER, ENTER1)
        check_length(length)
        print(AGAIN)
        start()
    if comand in EXIT:
        print(DECORATION)
        sys.exit(random.choice(BYE))
    else:
        print(WRONG_COMAND)
        start()
def decorate(to_decor):
    """
    Parameter : to_decor: string/function to be decorated
    Adds decorations before and after the string

    """
    print(DECORATION)
    print(to_decor)
    print(DECORATION)

def password_generator(L):
    """

    Parameters
    ----------
    L : integer: 16 <= x <= 50.

    Returns
    -------
    password : string YOUR_PASS + string password L characters long.
    
    >>> L = 30 ---> _:y:y=!2JH>DT56vG@dSEu-_C2_0eh (ex)

    """
    List = list(ALPHA + ALPHA.upper() + SYM + NUMS)
    password = ""
    for i in range (L):
      password += str(random.choice(List)) #random.choises only will return a list, we need to join it
    return YOUR_PASS.format(L) + password + "\n"

def get_length(string, enter):
    """
    

    Parameters
    ----------
    string : string to be printed.
    enter : string ask for user input.

    Returns
    -------
    length : string of user input, 
            NEEDS TO BE AN INTEGER BETWEEN 16 AND 50 
            (may be number, character, symbol, minor, major. this will be checked later).

    """
    print(string)
    length = raw_input(enter)
    return length

def check_length(L):
	"""
    

  Parameters
  ----------
  L : string length got from get_length.

  Checks that L is a number.
  Rounds L to the nearest integer.
  Checks that L is between 16 and 50.
  Will ask for user input again if not. (get_length)
  Will move to password_generator if L is a number between 16 and 50.
    
  >>> L = "20" ---> OK
  >>> decorate(password_generator(20)) ---> )b_WwlJ-#GG,&!CKJinc (ex)

  >>> L = "6" or L = "543" ---> TOO WEAK or TOO MUCH
  >>> ask user input againd and check it'
    
  >>> L = "43.9" ---> L = 44
    
  >>> L = "a9-" ---> EXEPTION
  >>> ask user input again and check it'
    
  """
	try:
		length = round(float(L))
		if length in range(16, 51):
			decorate(password_generator(int(length)))
    
		else:
			print(DECORATION)
			new_L = get_length(WEAK if length < 16 else LONG, ENTER2)
			check_length(new_L)
	except:
		print(DECORATION)
		new_L = get_length(NO_WAY, ENTER3)
		check_length(new_L)

def run():
    """
    main function. will run the program.

    """
    decorate(WELCOME)
    start()
    
run()     
