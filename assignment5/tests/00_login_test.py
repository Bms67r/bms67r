from testedCode.login import *
import pytest

def test_login():
	
	print("\nchecking if username and password is in system database... ")

	#add FAIL to the end of the functions to do fail condition

	user = getUser()
	pswd = getPass()

	assert user != ""
	assert pswd != ""

def test_login_Fail():

	print("\nchecking if username and password is in system database... ")

	user = getUserFAIL()
	pswd = getPassFAIL()

	assert user != ""
	assert pswd != ""
