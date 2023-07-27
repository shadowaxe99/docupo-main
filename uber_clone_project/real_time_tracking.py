import time
from src.mapping_service import get_current_location

class RealTimeTracking:
    def __init__(self, ride_data):
        self.ride_data = ride_data
        self.driver_id = ride_data['driver_id']
        self.pickup_location = ride_data['pickup_location']
        self.dropoff_location = ride_data['dropoff_location']

    def trackLocation(self):
        driver_current_location = get_current_location(self.driver_id)
        return driver_current_location

    def calculateETA(self):
        driver_current_location = self.trackLocation()
        # Assuming we have a function get_distance() that calculates the distance between two points
        distance_to_pickup = get_distance(driver_current_location, self.pickup_location)
        # Assuming an average speed of 40 km/h
        average_speed = 40
        eta = distance_to_pickup / average_speed
        return eta

    def start_tracking(self):
        while True:
            eta = self.calculateETA()
            print(f"Driver's current location: {self.trackLocation()}")
            print(f"Estimated time of arrival: {eta} hours")
            time.sleep(5)  # Update every 5 seconds
