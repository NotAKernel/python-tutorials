user_0 = user_0

if user_0.login_attempts == True:
    user_0.greet_user()
else:
    print("profile_locked")
    reset = input("Enter 'yes' to proceed: ")
    if reset == 'yes':
        login_attempts=0
        user_0.increment_login_attempts()
    else:
        print("Shutting Down")