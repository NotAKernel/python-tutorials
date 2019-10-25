username = input("Enter your name: ")

file_name = 'guest.txt'

with open('guest.txt','a') as file_object:
    file_object.write(f"\n{username}")