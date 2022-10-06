# Package class for package objects

class Package:
    def __init__(self, id, status, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.status = status
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

