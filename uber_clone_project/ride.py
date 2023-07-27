class Ride:
    def __init__(self, pickup_location, dropoff_location):
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.status = 'Booked'

    def start_ride(self):
        self.status = 'In Progress'

    def end_ride(self):
        self.status = 'Completed'

    def get_status(self):
        return self.status

    def get_pickup_location(self):
        return self.pickup_location

    def get_dropoff_location(self):
        return self.dropoff_location