# Truck class
class DeliveryTruck:

    # Constructor
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.package_queue = Queue() # or []
        self.speed = 18
        self.miles_traveled = 0
        self.truck_capacity = 16
        self.current_location = 0
        self.driver = None