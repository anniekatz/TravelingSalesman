# Package class for package objects

class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.package_status = "AT HUB"
        self.delivered_time = None

