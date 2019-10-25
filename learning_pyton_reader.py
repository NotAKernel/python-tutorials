file_name = 'learning_python.txt'
with open(file_name) as file_object:
    contents = file_object.readlines()
    print(contents)