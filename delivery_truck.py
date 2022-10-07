# Truck class
class DeliveryTruck:

    # Constructor
    def __init__(self, truck_id, packages, departure_time):
        self.truck_id = truck_id
        self.packages = packages
        self.departure_time = departure_time
        self.package_queue = []
        self.speed = 18
        self.miles_traveled = 0
        self.truck_capacity = 16
        self.current_location = 0

    def append_to_queue(self, package):
        self.package_queue.append(package)


    def __str__(self):
        return "Truck ID: " + str(self.truck_id) + "\nDeparture Time: " + str(self.departure_time) + "\nCurrent Location: " + str(self.current_location) + "\n" + \
               "Miles Traveled: " + str(self.miles_traveled) + "\n" + "Driver: " + str(self.driver) + "\n" + \
               "Packages: " + str(self.package_queue)