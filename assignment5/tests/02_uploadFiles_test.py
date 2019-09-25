#this is a test for the Student uploading a file

def test_isUploaded():

    print("\nchecking if file was successfully uploaded...")

    file_types = ["png", "jpg"]

    img_file = getSubmittedType()

    flag = False

    for x in file_types:
        if x == img_file:
            flag = True

    assert flag == True