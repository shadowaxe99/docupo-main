import json
from geopy.distance import geodesic

# Load driver data
with open('driver_data.json', 'r') as file:
    driver_data = json.load(file)

def matchDriver(user_location, ride_type):
    """
    Function to match a driver to a passenger based on location, driver ratings, and traffic conditions.
    """
    available_drivers = [driver for driver in driver_data if driver['status'] == 'available' and driver['ride_type'] == ride_type]

    if not available_drivers:
        return "No drivers available at the moment."

    # Sort drivers based on distance from user and driver ratings
    sorted_drivers = sorted(available_drivers, key=lambda driver: (geodesic(user_location, driver['location']).miles, -driver['rating']))

    # Select the best match
    best_match = sorted_drivers[0]

    # Update driver status
    best_match['status'] = 'engaged'

    # Save updated driver data
    with open('driver_data.json', 'w') as file:
        json.dump(driver_data, file)

    return best_match
