import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/david/Documents/Courses/Udacity/Programming Foundations with Python/prank")
    os.chdir(r"/Users/david/Documents/Courses/Udacity/Programming Foundations with Python/prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        print "Old name -- " + file_name
        print "New name -- " + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()