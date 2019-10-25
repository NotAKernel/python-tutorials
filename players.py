items = ['milk','bread','water','crisps','sweets']
print("The first three items in the list are:")
for item in items[:3]:
    print(item.title())

print("\nThree items from the mddle of the list are:")
for item in items[1:4]:
    print(item.title())

print("\nThe last three items on the list are:")
for item in items[2:]:
    print(item.title())