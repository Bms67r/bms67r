from testedCode.login import *
import pytest

def test_login():
	
	print("\nchecking if student is enrolled in course database... ")

	#add FAIL to the end of the functions to do fail condition

	user = getUser()
	pswd = getPass()

	#user = getUserFAIL()
        #pswd = getPassFAIL()

	assert user != ""
	assert pswd != ""

