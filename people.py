info = {
    'jim': {
        'birth date': '08/10/1990',
        'country': 'new zealand',
        'occupation': 'software',
        },
    
    'daniel': {
        'birth date': '20/05/2004',
        'country': 'belarus',
        'occupation': 'student',
        },

    'connor': {
        'birth date': '30/12/1998',
        'country': 'ireland',
        'occupation': 'none',
        },

    'shane': {
        'birth date': '16/7/1992',
        'country': 'ireland',
        'occupation': 'messing up the internet'
        },
    }

for name, details in info.items():
    print(f"\nName: {name.title()}")
   
    birth_date = details['birth date']
    country = details['country']
    occupation = details['occupation']

    print(f"Date of Birth: {birth_date}")
    print(f"Country: {country.title()}")
    print(f"Occupation: {occupation.title()}")