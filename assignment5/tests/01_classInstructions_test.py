from testedCode.classInstructions import *
import pytest

#this is a test for the Student reading assignment instructions, student must be enrolled in course to access

def test_isEnrolled():

    print("\nchecking if student is enrolled in course database...")

    database_check = 12530123

    person_id = enterId()

    assert database_check == person_id


def test_isEnrolledFAIL():

    print("\nchecking if student is enrolled in course database...")

    database_check = 12530123

    person_id = enterIdFAIL()

    #the submitted student ID does not match anything in the database
    assert database_check == person_id
