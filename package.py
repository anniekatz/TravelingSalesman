# Package class for package objects
from datetime import datetime, timedelta


class Package:
    def __init__(self, id, location_id, address, city, state, zipcode, deadline, weight, notes, status):
        self.id = id
        self.location_id = location_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.departure_dt = timedelta(hours=0, minutes=0, seconds=0)
        self.delivered_dt = timedelta(hours=0, minutes=0, seconds=0)

    # Return package attributes
    def __str__(self):
        return "Package ID: " + self.id + " | Location ID: " + self.location_id + " | Address: " + self.address + " | City: " + self.city + " | State: " + self.state + " | Zip: " + self.zipcode + " | Deadline: " + self.deadline + " | Weight: " + self.weight + " | Notes: " + self.notes + " | Departure Time: " + str(self.departure_dt)

    def get_package_status(self, time):
        if time >= self.delivered_dt:
            return 'DELIVERED AT ' + str(self.delivered_dt)
        if time >= self.departure_dt:
            return 'ON THE TRUCK'
        else:
            return 'AT HUB'

