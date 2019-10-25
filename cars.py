def make_car(make, model, **kwargs):
    """Makes a custom car"""
    print(f"Make: {make.title()} \nModel: {model.title()} \nDetails: {kwargs}")

make_car('Mclaren', 'P1', colour='chrome blue', tow_package=True)