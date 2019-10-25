print("Enter two numbers.\n'q' to quit.")

while True:
    try:
        number_0 = input("First Number: ")
        number_1 = input("Second Number: ")
        result = int(number_0) + int(number_1)
        if number_0.lower() == 'q':
            break
        if number_1.lower() == 'q':
            break

    except ValueError:
        print("Enter numbers only please.")
    else:
        print(result)