def make_car(make, model, **options):
    """We are building a dictionary of cars"""
    car_dict = {
        'make': make.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
    
    return car_dict


my_subaru = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_subaru)

my_truck = make_car('ram', '1500', trim='limited',  body_type='pickup', bed_length='long bed', engine='5.7 hemi', color='patriot blue')
print(my_truck)