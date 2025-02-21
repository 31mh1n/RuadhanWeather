from geopy.geocoders import Nominatim


def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="geoapi_explorer")
    location_data = geolocator.geocode(location)

    if location_data:
        return location_data.latitude, location_data.longitude
    else:
        return None


# Example: Get coordinates for Dublin, Ireland
# location = "Grange, Co. Sligo, Ireland"
# coordinates = get_location_coordinates(location)
# long = coordinates[0]
# lat = coordinates[1]
#
# if coordinates:
#     print(f"{long}, {lat}")
#     print(f"Latitude and Longitude of {location}: {coordinates}")
# else:
#     print("Location not found.")
