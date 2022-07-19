
# Importing required module
from geopy.geocoders import Nominatim
 
# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")
 
# Zipcode input
zipcode = int(input("Enter your zipcode ~ "))
 
# Using geocode()
location = geolocator.geocode(zipcode)
 
# Displaying address details
print("Zipcode:",zipcode)
print("Details of the Zipcode:")
print(location)