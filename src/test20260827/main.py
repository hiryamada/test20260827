import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

WEATHER_CONDITIONS = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Partly Cloudy"]


class WeatherResponse(BaseModel):
    city: str
    condition: str
    max_temp: int
    min_temp: int


@app.get("/weather/{city}", response_model=WeatherResponse)
def get_weather(city: str) -> WeatherResponse:
    min_temp = random.randint(-10, 25)
    max_temp = random.randint(min_temp + 1, 40)
    return WeatherResponse(
        city=city,
        condition=random.choice(WEATHER_CONDITIONS),
        max_temp=max_temp,
        min_temp=min_temp,
    )
