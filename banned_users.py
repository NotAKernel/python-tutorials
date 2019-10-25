banned_users = ['andrew','carolina','david']
users = ['marie','tom', 'edward']

if users not in banned_users:
    for user in users:
        print(f"\n{user.title()}, you can post a response if you wish.")