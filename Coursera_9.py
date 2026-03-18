#This is the basic code for a distance converter from km to m ...
def convert_distance(km):
    m= km * 1000
    return m

my_trip_kilometers = 34
my_trip_meters = convert_distance(my_trip_kilometers)
print("The distance in meters is: " + str(my_trip_meters))

