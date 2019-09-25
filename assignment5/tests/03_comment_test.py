#this is a test for the Student adding a comment

def test_isEnrolled():

    print("\nchecking if comment exceeds maximum length...")

    #len(string) function

    charLength = getCommentLength()

    assert charLength < 300