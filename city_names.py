prompt = "City Name: "
prompt_2 = "Country Name: "
def city_country(city_name, country_name):
    """Displays a city in a country."""
    place_name = f"{city_name}, {country_name}"
    return place_name.title()

while True:
    print("enter 'q' anytime to quit")
    city = input(prompt)
    if city.lower() == 'q':
        break
    
    country = input(prompt_2)
    if country.lower() == 'q':
        break

    area_name = city_country(city, country)
    print(area_name)
    