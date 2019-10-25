class User:
    """Username and information."""

    def __init__(self, first_name, last_name, login_attempts, *args):
        """Initialises attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.args = args
        self.full_name = f"{first_name} {last_name}"
        self.login_attempts = login_attempts
    
    def describe_user(self):
        """Prints the information."""
        print(f"\nFirst Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Additional Information: {self.args}")

    def greet_user(self):
        """Prints a personalised greeting."""
        print(f"Hello {self.full_name.title()}, how are you today?")

    def increment_login_attempts(self, login_attempts=0):
        """Counts login attempts and quits after 3 unsuccessful attempts."""
        login_attempts = True
        while login_attempts:
            login = input("Please enter the password: ")
            if login != '0;k86hf42s':
                print("Incorrect password")
                login_attempts += 1
            else:
                print("Welcome to PC-1")
                continue
            if login_attempts == 4:
                break

user_0 = User('james', 'fairbairn', 24, 'software engineer', "6'1")


class Admin(User):
    """Gains more privilges."""
    def __init__(self, first_name, last_name, priviliges=0, login_attempts=None, *args):
        super().__init__(first_name, last_name, priviliges, login_attempts, *args)
        self.priviliges = ["can add posts", "can delete posts", "can ban users"]
        self.login_attempts = login_attempts
        
    def show_privilges(self):
            print(self.privilges)
           
        
admin = Admin('daniel', 'yermak')   
admin.show_privilges() 