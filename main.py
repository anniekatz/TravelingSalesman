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
                return row[loc2 + 1]


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
            new_package = Package(package_id, location_address, location_city, location_state, location_zip, row[2],
                                  row[3], row[4])
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
        package.package_status = 'ON TRUCK'

   # nearest neighbor algorithm using get_distance_between method
    while len(tbd) > 0:
        truck_distance = 0
        for package in tbd:
            distance = get_distance_between(delivery_truck.current_location, package.location_id)
            if distance != '':
                truck_distance += float(distance)
        print(truck_distance)
        for package in tbd:
            distance = get_distance_between(delivery_truck.current_location, package.location_id)
            if distance != '':
                if float(distance) < truck_distance:
                    truck_distance = float(distance)
                    delivery_truck.packages.remove(package.id)
                    delivery_truck.packages.append(package.id)
                    delivery_truck.location_id = package.location_id
                    tbd.remove(package)
                    print(package.id)
                    print(package.location_id)
                    print(truck_distance)
                    print(delivery_truck.packages)
                    print(delivery_truck.location_id)
                    print(tbd)

# greedy alg for delivery -- nearest neighbor
# maybe load trucks manually after greedy alg has been determined?
# like maybe the 3 with the farthest distances in between are where trucks separate idk

# interface for user to see status of packages
# if csv is addresses:
# make address dictionary
# make dict for address_table
