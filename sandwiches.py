def sandwich(*items):
    """Prints a summary of the sandwich"""
    print(f"\nHere is your sandwich:")
    for item in items:    
        print(f"- {item.title()}")

sandwich('ham','cheese','butter', 'chicken', 'mayo')
