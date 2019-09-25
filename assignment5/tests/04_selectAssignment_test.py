from testedCode.selectAssignment import *
import pytest

#this is a test for the student selecting an assignment to submit to
#the assignment must exist to submit to it

def test_checkAssignment():

    print("\nchecking if selected assignment exists...")

    cources = ["assignment1", "assignment2", "assignment3"]

    chosenAssignment = assignmentChosen()

    flag = False

    for x in cources:
        if x == chosenAssignment:
            flag = True

    assert flag == True

def test_checkAssignmentFAIL():

    print("\nchecking if selected assignment exists...")

    cources = ["assignment1", "assignment2", "assignment3"]

    chosenAssignment = assignmentChosenFAIL()

    #if no such assignmnet exists, test will fail

    flag = False

    for x in cources:
        if x == chosenAssignment:
            flag = True

    assert flag == True