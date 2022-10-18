# Ann Katz
# C950 WGUPS Traveling Salesman Project
# Student ID: 010458098

import csv
from datetime import datetime, timedelta, date, time
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
            # create new location object per row
            new_location = Location(row[0], row[1], row[2], row[3], row[4], row[5])
            addresses.append(new_location)
    return addresses


# create location list
location_list = make_location_list()



# get distance between 2 location IDs by reading in CSV file
def get_distance_between(loc1, loc2):
    if loc1 == loc2:
        return 0.0
    else:
        with open('csv_resources/distance_table.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # remove leading string and set to int
                location = int(row[0].replace('\ufeff', ''))
                if location == loc1:
                    dist_float = float(row[loc2 + 1])
                    # return distance as a float
                    return dist_float

# read in package CSV data
def make_package_table():
    with open('csv_resources/package_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        package_table = ManualHashTable()
        package_list = []
        # append each row into a package object
        for row in csv_reader:
            package_id = row[0].replace('\ufeff', '')
            location_id = row[1]
            # get location data from location list
            for location in location_list:
                if location_id == location.id:
                    location_zip = location.zip
                    location_address = location.address
                    location_city = location.city
                    location_state = location.state
            # create new package per row
            new_package = Package(package_id, location_id, location_address, location_city, location_state, location_zip, str(row[2]),
                                  row[3], row[4], "AT HUB")
            # create hash table of packages
            package_table.insert(int(package_id), new_package)
            package_list.append(new_package)
    return package_list

# create package hash table
package_table = make_package_table()


# Load delivery trucks manually and initialize departure times
truck1 = DeliveryTruck(1, [4, 13, 14, 15, 16, 19, 20, 21, 34, 39, 40], timedelta(hours=8, minutes=0, seconds=0))
truck2 = DeliveryTruck(2, [2, 3, 8, 9, 10, 11, 12, 17, 18, 23, 27, 28, 33, 35, 36, 38], timedelta(hours=10, minutes=20, seconds=0))
truck3 = DeliveryTruck(3, [1, 5, 6, 7, 22, 24, 25, 26, 29, 30, 31, 32, 37], timedelta(hours=9, minutes=5, seconds=0))

# Nearest neighbor algorithm has been tested to ensure all packages meet deadlines and additional requirements
def nearest_neighbor_delivery(delivery_truck):
    # create list of packages to be delivered TBD
    tbd = []
    for package in package_table:
        if int(package.id) in delivery_truck.packages:
            tbd.append(package)

    # while there are still packages to deliver, use nearest neighbor algorithm to find next package to deliver
    while len(tbd) > 0:
        # intialize location to unused num
        next_loc = 100.0
        # initialize nearest neighbor to first package in list
        next_pkg = tbd[0]
        # initialize distance to 0
        distance = 0.0
        for package in tbd:
            # use distance to find nearest neighbor
            if delivery_truck.current_location > int(package.location_id):
                distance = get_distance_between(delivery_truck.current_location, int(package.location_id))
            if delivery_truck.current_location < int(package.location_id):
                distance = get_distance_between(int(package.location_id), delivery_truck.current_location)
            if delivery_truck.current_location == int(package.location_id):
                distance = 0.0
            # set next package and get its location based on nearest neighbor
            if distance <= next_loc:
                next_loc = distance
                next_pkg = package

        delivery_truck.package_queue.append(next_pkg.id)
        tbd.remove(next_pkg)
        delivery_truck.miles_traveled += next_loc
        delivery_truck.current_location = int(next_pkg.location_id)
        delivery_truck.time += next_loc / delivery_truck.speed
        next_pkg.departure_dt = delivery_truck.departure_time
        next_pkg.delivered_dt = delivery_truck.departure_time + timedelta(hours=delivery_truck.time)

    # return to hub after all packages have been delivered
    if len(tbd) == 0:
        distance = get_distance_between(delivery_truck.current_location, 0)
        # add distance and time to get back to hub
        delivery_truck.miles_traveled += distance
        delivery_truck.time += distance / delivery_truck.speed
        # set current location to hub
        delivery_truck.current_location = 0
        delivery_truck.returned_to_hub = True
        delivery_truck.return_time = delivery_truck.departure_time + timedelta(hours=delivery_truck.time)



# interface for user to see status of packages
def user_interface():
    print("Traveling Salesman Package Delivery System")

    # get user input
    print("You can: \n"
          "* Enter '0' to see total miles traveled by all trucks on route \n"
          "* Enter '1' to see status of particular package \n"
          "* Enter '2' to see status of all packages at a specified time \n")
    user_input = input("Enter 0, 1, or 2: ")

    # determine what info user wants
    if user_input == '0':
        # print total mileage of route and truck return times
        print("Total miles traveled by all trucks on route: ", truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled)
        print("Truck 1 left the hub at " + str(truck1.departure_time) + " and returned to the hub at " + str(truck1.return_time))
        print("Truck 2 left the hub at " + str(truck2.departure_time) + " and returned to the hub at " + str(truck2.return_time))
        print("Truck 3 left the hub at " + str(truck3.departure_time) + " and returned to the hub at " + str(truck3.return_time))

    # print status of particular package upon end of day
    elif user_input == '1':
        # status of a particular package
        user_input = int(input("Enter package ID: ")) - 1
        if package_table[user_input] is None:
            print("Package not found.")
        else:
            package = package_table[user_input]
            print(package.__str__() + " | STATUS: " + package.get_package_status(truck2.return_time + timedelta(hours=1)))

    # print status of all packages at a user-specified time
    elif user_input == '2':
        # get time from user
        user_input = input("Enter time in 24hr (military time) format (HH:MM): ")
        # check if user input is a valid time
        try:
            user_input = datetime.strptime(user_input, '%H:%M')
            user_time = timedelta(hours=user_input.hour, minutes=user_input.minute, seconds=user_input.second)
            for package in package_table:
                if package is not None:
                        print(package.__str__() + " | STATUS: " + package.get_package_status(user_time))
        except ValueError:
            print("Invalid time format. Please try again.")

    # catch any invalid user input
    # restart user interface function if invalid input
    else:
        print("Invalid entry. Please try again using 0, 1, or 2.")
        user_interface()

# main class
class Main:
        if __name__ == '__main__':
            # run nearest neighbor algorithm for each delivery truck
            nearest_neighbor_delivery(truck1)
            nearest_neighbor_delivery(truck3)

            # Truck 2 runs at 10:20 AM or later. At 10:20, change package 9's delivery address according to notes
            for package in package_table:
                if package.id == "9":
                    package.location_id = "19"
                    package.address = "410 S State St"
                    package.city = "Salt Lake City"
                    package.zip = "84111"

            # Ensure truck 1 has returned
            if truck1.returned_to_hub is True and truck1.return_time <= timedelta(hours=10, minutes=20, seconds=0):
                # run nearest neighbor algorithm for truck 2 with a departure time of 10:20
                nearest_neighbor_delivery(truck2)
            else:
                # if truck 1 returns after 10:20, set a new departure time for truck 2
                truck2 = DeliveryTruck(2, [2, 3, 8, 9, 10, 11, 12, 17, 18, 23, 27, 28, 33, 35, 36, 38],
                                       truck1.return_time)
                nearest_neighbor_delivery(truck2)

            # run user interface
            user_interface()

