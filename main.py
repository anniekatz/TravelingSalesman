# Ann Katz
# C950 WGUPS Traveling Salesman Project
# Student ID: 010458098

import os
import csv
from datetime import datetime
from delivery_truck import DeliveryTruck
from hash_table import ManualHashTable
from location import Location
from package import Package


# Use csv reader to get location data
def make_location_list():
    # for every row in csv_resources/address_table.csv, make a new location and add to list
    addresses = []
    with open('csv_resources/address_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            new_location = Location(row[0], row[1], row[2], row[3], row[4], row[5])
            addresses.append(new_location)
    return addresses


# create location list
location_list = make_location_list()



# get distance between 2 location IDs by reading in CSV file
def get_distance_between(loc1, loc2):
    with open('csv_resources/distance_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == loc1:
                dist_float = float(row[loc2 + 1])
                return dist_float

# read in package CSV data
def make_package_table():
    with open('csv_resources/package_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        package_table = ManualHashTable()
        package_list = []
        for row in csv_reader:
            package_id = row[0].replace('\ufeff', '')
            location_id = row[1]
            for location in location_list:
                if location_id == location.id:
                    location_zip = location.zip
                    location_address = location.address
                    location_city = location.city
                    location_state = location.state
            new_package = Package(package_id, location_id, location_address, location_city, location_state, location_zip, str(row[2]),
                                  row[3], row[4], "AT HUB")
            package_table.insert(int(package_id), new_package)
            package_list.append(new_package)
    return package_table

# create package hash table
package_table = make_package_table()


# Load delivery trucks manually
truck1 = DeliveryTruck(1, [4, 13, 14, 15, 16, 19, 20, 21, 34, 39, 40], '08:00')
truck2 = DeliveryTruck(2, [2, 3, 8, 9, 10, 11, 12, 17, 18, 23, 27, 28, 33, 35, 36, 38], '10:20')
truck3 = DeliveryTruck(3, [1, 5, 6, 7, 22, 24, 25, 26, 29, 30, 31, 32, 37], '09:05')

def nearest_neighbor_delivery(delivery_truck):
    tbd = []
    for package in delivery_truck.packages:
        package = package_table.search(package)
        tbd.append(package)

    # while there are still packages to deliver, use nearest neighbor algorithm to find next package to deliver
    while len(tbd) > 0:
        # initialize nearest neighbor to first package in list
        next_loc = 100
        next_pkg = tbd[0]
        for package in tbd:
            # use distance to find nearest neighbor
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

    # return to hub after all packages have been delivered
    if len(tbd) == 0:
        distance = get_distance_between(delivery_truck.current_location, 0)
        # add distance and time to get back to hub
        delivery_truck.miles_traveled += distance
        delivery_truck.time += distance / delivery_truck.speed
        # set current location to hub
        delivery_truck.current_location = 0
        delivery_truck.returned_to_hub = True



# interface for user to see status of packages
def user_interface():
    print("Traveling Salesman Package Delivery System")
    print("You can: \n"
          "* Enter '0' to see total miles traveled by all trucks on route \n"
          "* Enter '1' to see status of particular package \n"
          "* Enter '2' to see status of all packages at a specified time \n")
    user_input = input("Enter 0, 1, or 2: ")
    if user_input == '0':
        # total mileage of route
        print("Total miles traveled by all trucks on route: ", truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled)
    elif user_input == '1':
        # status of a particular package
        user_input = input("Enter package ID: ")
        if package_table.search(user_input) is None:
            print("Package not found.")
        else:
            package = package_table.search(user_input)
            print(package.__str__())
    elif user_input == '2':
        # status of all packages at a specified time
        user_input = input("Enter time in 24hr (military time) format (HH:MM): ")
        # check if user input is a valid time
        try:
            user_input = datetime.strptime(user_input, '%H:%M')
            for package in package_table.table:
                if package is not None:
                    if package.departure_dt <= user_input <= package.delivered_dt:
                        print(package.__str__())
        except ValueError:
            print("Invalid time format. Please try again.")
    else:
        print("Invalid entry. Please try again using 0, 1, or 2.")

class Main:
        if __name__ == '__main__':
            # run program
            # nearest_neighbor_delivery(truck1)
            # nearest_neighbor_delivery(truck3)
            # Ensure truck 1 has returned and that it's before 10:20
            # if truck1.returned_to_hub is True and truck1.time <= truck2.departure_time:
            #    nearest_neighbor_delivery(truck2)


            #user_interface()
            #tbd = []
            #for package_id in truck1.packages:
            #    package = package_table.search(package_id)
            #    tbd.append(package)
            #print(len(tbd))
            #print(tbd)


            for i in range (len(package_table.table) ):
                print((package_table.search(i)).__str__())
            #    print(package_table[i].__str__())




            #for i in range (len(location_list)):
             #   print(location_list[i].__str__())

