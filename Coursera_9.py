def convert_distance(km):
    m= km * 1000
    return m

my_trip_kilometers = 55
my_trip_meters = convert_distance(my_trip_kilometers)
print("The distance in meters is: " + str(my_trip_meters))