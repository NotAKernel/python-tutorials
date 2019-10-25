file_path = '/Users/loaner/Documents/code/python-tutorials/text_files/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())