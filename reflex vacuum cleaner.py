#import the "random" module to generate random numbers.
import random

#initializes the dictionary "location_condition" with two locations, A and B,
# each initially set to '0', which represents a clean condition.
location_condition = {'A' : '0' , 'B' : '0'}

location_condition['A'] = random.randint(0,1)
location_condition['B'] = random.randint(0,1)
vacuum_location = random.randint(0,1)


if vacuum_location == 0:
    print("Vacuum is randomly placed at Location A.")
    if location_condition['A'] == 1:
        print("Location A is Dirty")
        location_condition['A']= 0
        print("Location A has been Cleaned.")
    else:
        print("Location A is already clean")
    print("Moving to location B")
    if location_condition['B'] == 1:
        print("Location B is Dirty ")
        location_condition['B'] = 0
        print("Location B has been Cleaned.")
    else:
        print("Location B is already clean ")
    print("Environment is clean!")

elif vacuum_location == 1:
    print("Vacuum is randomly placed at Location B.")
    if location_condition['B'] == 1:
        print("Location B is Dirty.")
        location_condition['B'] = 0
        print("Location B has been Cleaned.")
    else:
        print("Location B is already clean")
    print("Moving to location A ")

    if location_condition['A'] == 1:
        print("Location A is Dirty ")
        location_condition['A'] = 0
        print("Location A has been Cleaned.")
    else:
        print("Location A is already clean")

    print("Environment is clean!")
