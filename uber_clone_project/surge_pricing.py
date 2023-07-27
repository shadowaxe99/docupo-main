import datetime
from src.ride_booking import ride_data

def calculateSurgePricing():
    current_time = datetime.datetime.now().time()
    peak_hours = [datetime.time(7, 0), datetime.time(9, 0), datetime.time(17, 0), datetime.time(19, 0)]

    if any([current_time > start and current_time < end for start, end in zip(peak_hours[::2], peak_hours[1::2])]):
        surge_multiplier = 1.5
    else:
        surge_multiplier = 1.0

    for ride in ride_data:
        ride['estimated_fare'] *= surge_multiplier

    return ride_data
