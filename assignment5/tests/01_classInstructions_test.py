#this is a test for the Student reading assignment instructions

def test_isEnrolled():

    print("\nchecking if student is enrolled in course database...")

    database_check = 12530123

    person_id = enterId()

    assert database_check == person_id
