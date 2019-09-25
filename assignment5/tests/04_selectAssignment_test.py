#this is a test for the Student selecting an assignment to submit to
#the assignment must exist to submit to it

def test_isEnrolled():

    print("\nchecking if selected class exists")

    cources = ["assignment1", "assignment2", "assignment3"]

    chosenAssignment = assignmentChosen()

    flag = False

    for x in cources:
        if x == chosenAssignment:
            flag = True

    assert flag == True