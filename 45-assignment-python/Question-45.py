# Function to store car information
def build_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    
    # Add the extra information (like color or optional features) to the car dictionary
    for key, value in car_info.items():
        car[key] = value
    
    return car

# Call the function with required and optional information
car1 = build_car('Tesla', 'Model 3', color='red', autopilot=True)
car2 = build_car('Ford', 'Mustang', color='blue', year=2022)

# Print the returned car objects
print(car1)
print(car2)
