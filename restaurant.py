class Restaurant:
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes.""" 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
            """Prints the attributes"""
            print(f"\n\nThe restaurant is called: {self.restaurant_name.title()}")
            print(f"The type of cuisine is: {self.cuisine_type.title()}")

    def open_restaurant(self):
            """Prints that the restaurant is open."""
            print(f"\n{self.restaurant_name.title()} is now open!")

    def close_restaurant(self):
        """Prints that the restaurant is closed."""   
        print(f"\n{self.restaurant_name.title()} is closed.")

restaurant_0 = Restaurant('taikichi', 'japanese')
restaurant_1 = Restaurant('Milano', 'pizza')
restaurant_2 = Restaurant('Volcano wings', 'chicken wings')

restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_1.close_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()