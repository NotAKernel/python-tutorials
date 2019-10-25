import json

def prompt_number():
    """Ask the user for their favourite number."""
    
    username = input("Enter your favourite number: ")
    filename = 'fav_number.json'
    
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def show_number():
    """Displays the user's favourite number."""
    filename = 'fav_number.json'
    with open(filename) as f:
        number = str(json.dump(f))
    print(f"Your favourite number is: {number}")

if prompt_number():
    show_number()