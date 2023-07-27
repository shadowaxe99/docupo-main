from src.user_registration import user_data
from src.driver_matching import matchDriver
from src.real_time_tracking import trackLocation
from src.payment_integration import processPayment

class RideBooking:
    def __init__(self):
        self.ride_data = {}

    def bookRide(self, user_id, pickup_location, dropoff_location, ride_type):
        # Validate user
        if user_id not in user_data:
            return "User not found."

        # Match driver
        driver_id = matchDriver(pickup_location, ride_type)
        if not driver_id:
            return "No drivers available."

        # Estimate fare
        estimated_fare = self.estimateFare(pickup_location, dropoff_location, ride_type)

        # Create ride data
        self.ride_data = {
            "user_id": user_id,
            "driver_id": driver_id,
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "ride_type": ride_type,
            "estimated_fare": estimated_fare
        }

        # Track driver location
        trackLocation(driver_id)

        return "Ride booked successfully."

    def estimateFare(self, pickup_location, dropoff_location, ride_type):
        # This is a placeholder function. In a real-world application, this would involve complex calculations
        # based on distance, traffic, ride type, and possibly other factors.
        return 10.00

    def getRideData(self):
        return self.ride_data

    def makePayment(self, user_id, payment_method):
        # Process payment
        payment_status = processPayment(user_id, self.ride_data["estimated_fare"], payment_method)

        if payment_status == "Payment successful.":
            self.ride_data["payment_status"] = "Paid"
        else:
            self.ride_data["payment_status"] = "Not paid"

        return payment_status
