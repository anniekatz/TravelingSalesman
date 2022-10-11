# Ann Katz
# C950 WGUPS Traveling Salesman Project
# Student ID: 010458098

import csv
from datetime import datetime
from delivery_truck import DeliveryTruck
from hash_table import HashTable
from location import Location
from package import Package


# Use csv reader to get data
def make_location_list():
    # for every row in csv_resources/address_table.csv, make a new location and add to list
    with open('csv_resources/address_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        location_list = []
        for row in csv_reader:
            new_location = Location(row[0], row[1], row[2], row[3], row[4], row[5])
            location_list.append(new_location)
    return location_list


location_list = make_location_list()


def get_distance_between(loc1, loc2):
    with open('csv_resources/distance_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == loc1:
                dist_float = float(row[loc2 + 1])
                return dist_float


def make_package_table():
    with open('csv_resources/package_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        package_table = HashTable()
        for row in csv_reader:
            package_id = row[0].replace('\ufeff', '')
            location_id = row[1]
            for location in location_list:
                if location_id == location.id:
                    location_zip = location.zip
                    location_address = location.address
                    location_city = location.city
                    location_state = location.state
            new_package = Package(package_id, location_id, location_address, location_city, location_state, location_zip, row[2],
                                  row[3], row[4], "AT HUB")
            package_table.insert(package_id, new_package)
    return package_table


package_table = make_package_table()

# Load delivery trucks manually
truck1 = DeliveryTruck(1, [4, 13, 14, 15, 16, 19, 20, 21, 34, 39, 40], '8:00')
truck2 = DeliveryTruck(2, [2, 3, 8, 9, 10, 11, 12, 17, 18, 23, 27, 28, 33, 35, 36, 38], '10:20')
truck3 = DeliveryTruck(3, [1, 5, 6, 7, 22, 24, 25, 26, 29, 30, 31, 32, 37], '9:05')


def nearest_neighbor_delivery(delivery_truck):
    tbd = []
    for package_id in delivery_truck.packages:
        package = package_table.search(package_id)
        tbd.append(package)
        package.package_status = "ON THE TRUCK"

    while len(tbd) > 0:
        next_loc = 50
        next_pkg = None
        for package in tbd:
            distance = get_distance_between(delivery_truck.current_location, package.location_id)
            if distance <= next_loc:
                next_loc = distance
                next_pkg = package

        delivery_truck.package_queue.append(next_pkg.id)
        tbd.remove(next_pkg)
        delivery_truck.miles_traveled += next_loc
        delivery_truck.current_location = next_pkg.location_id
        delivery_truck.time += next_loc / delivery_truck.speed
        next_pkg.departure_dt = delivery_truck.departure_time
        next_pkg.delivered_dt = delivery_truck.time
        next_pkg.package_status = "DELIVERED"

    # return to hub
    if len(tbd) == 0:
        distance = get_distance_between(delivery_truck.current_location, 0)
        delivery_truck.miles_traveled += distance
        delivery_truck.time += distance / delivery_truck.speed
        delivery_truck.returned_to_hub = True


nearest_neighbor_delivery(truck1)
nearest_neighbor_delivery(truck3)
# Ensure truck 1 has returned and that it's before 10:20
if truck1.returned_to_hub is True and truck1.time <= truck2.departure_time:
    nearest_neighbor_delivery(truck2)

# interface for user to see status of packages
class Main:
    print("Traveling Salesman Package Delivery System")
    total_miles = truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled
    print("Overview of Route. Total miles traveled: " + str(total_miles))
    print("You may look up a package's status or view all packages at specified timestamp.")
    print("Type '1' and press Enter to look up a package's status or type '2' to view all packages at a specific time.")
    # Lookup function
    # UI for time


    print(package_table)