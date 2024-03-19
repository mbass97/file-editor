import os

def file_reader(filename):
    file_object = open(filename, "r")
    contents = file_object.read()
    file_object.close()
    return contents

def file_writer(filename, writings):
    file_object = open(filename, 'w')
    file_object.write(writings)
    file_object.close()

def file_appender(filename, appendings):
    file_object = open(filename, 'a')
    file_object.write(appendings)
    file_object.close()

file_appender('final.txt', 'you can do it!')

# print(os.listdir())