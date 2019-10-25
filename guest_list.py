while True:
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    username = f"{f_name.title()} {l_name.title()}"

    file_name = 'guest_list.txt'

    with open('guest_list.txt','a') as file_object:
        file_object.write(f"{username}\n")

    print("Next name")