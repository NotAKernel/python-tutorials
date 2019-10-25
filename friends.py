favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
friends = ['phil', 'sarah']
for name in sorted(favourite_languages.keys()):
    print(name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favourite_languages.keys():
    print("\n\n\nErin, please take our poll!")
