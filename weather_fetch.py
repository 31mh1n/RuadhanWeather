import requests
import pandas as pd

# Base API URL
BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


def fetch_weather_data(lat: float, lon: float, year: int) -> pd.DataFrame:
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m",
        "format": "json",
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return data["hourly"]["time"], data["hourly"]["temperature_2m"]


def fetch_all_weather_data(lat: float, lon: float, start_year:int, end_year:int) -> pd.DataFrame:

    all_data = []

    for year in range(start_year, end_year + 1):
        print(f"Fetching data for {year}...")
        timestamps, temperatures = fetch_weather_data(lat=lat, lon=lon, year=year)


        df = pd.DataFrame({"timestamp": timestamps, "temperature": temperatures})
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date


        daily_stats = df.groupby("date")["temperature"].agg(["min", "max", "mean"]).reset_index()
        daily_stats.columns = ["date", "min_temp", "max_temp", "avg_temp"]

        all_data.append(daily_stats)


    return pd.concat(all_data)

