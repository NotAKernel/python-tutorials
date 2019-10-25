favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

name = favourite_languages.keys()
language = favourite_languages.values()

if len(favourite_languages) < 2:
        print(f"{name.title()}'s favourite language is: ")
        print({language})
for name, languages in favourite_languages.items():
        print(f"\n{name.title()}'s favourite languages are:")
for language in languages:
        print(f"\t{language.title()}")