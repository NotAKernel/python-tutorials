words = {'list': 'a group of items that can be changed or added to', 'tuple': 'a list that cannot be changed individually or added to', 'loop': 'a way to list through a group of items'}

for word, definition in sorted(words.items()):
    print(f"{word.title()}: \n{definition}")