# Package class for package objects

class Package:
    def __init__(self, package_id, location_id, address, city, state, zip, deadline, weight, notes, status):
        self.id = package_id
        self.location_id = location_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.package_status = status
        self.departure_dt = None
        self.delivered_dt = None


    def __str__(self):
        return "Package ID: " + self.id + "Location ID: " + self.location_id +  " Address: " + self.address + " City: " + self.city + " State: " + self.state + " Zip: " + self.zip + " Deadline: " + self.deadline + " Weight: " + self.weight + " Notes: " + self.notes + " Status: " + self.package_status + " Departure Time: " + self.departure_dt + " Delivered Time: " + str(self.delivered_dt)

    def get_package_status(self, time):
        if time >= self.delivered_dt:
            return 'DELIVERED AT ' + str(self.delivered_dt)
        if time >= self.departure_dt:
            return 'ON THE TRUCK'
        else:
            return 'AT HUB'

