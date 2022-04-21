weather_c = {
    "monday": 12,
    "tuesday": 14,
    "wednesday": 15,
    "thursday": 16,
    "friday": 11,
    "saturday": 15,
    "sunday": 12,
}

weather_f = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}
print(weather_f)
print(weather_c)
