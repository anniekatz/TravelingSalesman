# Location class
class Location:
    # constructor for location class
    def __init__(self, id, name, address, zip, city, state):
        self.id = id
        self.name = name
        self.address = address
        self.zip = zip
        self.city = city
        self.state = state

    # show location attributes if necessary
    def __str__(self):
        return "Location ID: " + self.id + " | Name: " + self.name + " | Address: " + self.address + " | Zip: " + self.zip + " | City: " + self.city + " | State: " + self.state
