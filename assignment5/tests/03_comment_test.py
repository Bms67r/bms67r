from testedCode.comment import *
import pytest

#this is a test for the Student adding a comment, the comment has a max char limit

def test_acceptedLength():

    print("\nchecking if comment exceeds maximum length...")

    charLength = getCommentLength()

    assert charLength < 300

def test_isEnrolled():

    print("\nchecking if comment exceeds maximum length...")

    #the maximum amount of characters will be exceeded

    charLength = getCommentLengthFAIL()

    assert charLength < 300