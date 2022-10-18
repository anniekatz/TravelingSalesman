# Truck class
from datetime import timedelta


class DeliveryTruck:

    # Constructor for DeliveryTruck
    def __init__(self, truck_id, packages, departure_time):
        self.truck_id = truck_id
        self.packages = packages
        self.departure_time = departure_time
        self.package_queue = []
        self.speed = 18
        self.time = 0
        self.miles_traveled = 0
        self.truck_capacity = 16
        self.current_location = 0
        self.returned_to_hub = False
        self.return_time = timedelta(hours=0, minutes=0, seconds=0)

# Return truck attributes
    def __str__(self):
        return "Truck ID: " + str(self.truck_id) + "\nDeparture Time: " + str(self.departure_time) + "\nCurrent Location: " + str(self.current_location) + "\n" + \
               "Miles Traveled: " + str(self.miles_traveled) + "\n" + "\n" + \
               "Packages: " + str(self.package_queue)