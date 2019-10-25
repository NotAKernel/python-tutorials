usernames = ['user_0','user_1','user_2','user_3','admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome back admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in.")
else:
    print("No users in system.")