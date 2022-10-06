# Ann Katz
# C950 WGUPS Traveling Salesman Project
# Student ID: 010458098

import csv
from location import Location

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

def get_distance_between(loc1,loc2):
    with open('csv_resources/distance_table.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == loc1:
                return row[loc2 + 1]

# if csv is packages
# make package list

# Create packages and trucks and load them

# greedy alg for delivery -- nearest neighbor
# maybe load trucks manually after greedy alg has been determined?
# like maybe the 3 with the farthest distances in between are where trucks separate idk

# interface for user to see status of packages
# if csv is addresses:
# make address dictionary
# make dict for address_table



