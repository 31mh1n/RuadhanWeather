from weather_fetch import fetch_all_weather_data
from location_fetch import get_location_coordinates
import pandas as pd

PLACE = "Grange"
COUNTY = "Sligo"
COUNTRY = "Ireland"


START_YEAR = 2021
END_YEAR = 2021


# DO NOT CHANGE ANYTHING BELOW THIS COMMENT
LOCATION = f"{PLACE}, Co. {COUNTY}, {COUNTRY}"
FILE_NAME = f"{PLACE}-{COUNTY}-{COUNTRY}_{START_YEAR}-{END_YEAR}"

lat, long = get_location_coordinates(LOCATION)

if long and lat is not None:
    all_data = fetch_all_weather_data(lat, long, START_YEAR, END_YEAR)
    all_data.to_csv(f"{FILE_NAME}.csv", index=False)
else:
    print(f"Was not able to fetch location: {LOCATION}")




