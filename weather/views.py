# views.py
import json
from django.utils import timezone 
from statistics import StatisticsError, mode
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from .models import TemperatureRecord
from django.db.models import Max, Min, Avg

# Global variables for thresholds
temperature_threshold = 31  # Initial threshold
update_count_threshold = 2  # Initial consecutive count

# Dictionary to keep track of the last recorded temperatures
last_temperatures = {}
exceeding_cities = []

def set_threshold(request):
    global temperature_threshold, update_count_threshold

    if request.method == 'POST':
        data = json.loads(request.body)
        temperature_threshold = int(data.get('temperature_threshold', 35))  # Default to 35 if not provided
        update_count_threshold = int(data.get('update_count_threshold', 2)) # Default to 2 if not provided
        
        return JsonResponse({"message": "Threshold updated successfully."}, status=200)

    return JsonResponse({"message": "Invalid request method."}, status=400)

def home(request):
    return render(request, 'weather/home.html')

def fetch_weather_data(request):
    global last_temperatures, exceeding_cities  # Use global variables

    cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad"]
    weather_data = []

    exceeding_cities.clear()  # Clear the list at the start of each fetch

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]

            # Save the temperature record to the database
            TemperatureRecord.objects.create(city=city, temperature=temperature, description=description)

            weather_info = {
                "city": city,
                "temperature": temperature,
                "description": description,
            }
            weather_data.append(weather_info)

            # Check for alerts and track exceeding cities
            check_alerts(city, temperature)
    print(exceeding_cities)
    
    # Prepare the response data
    response_data = {
        "weather_data": weather_data,
        "exceeding_cities": exceeding_cities,
        "temperature_threshold": temperature_threshold,  # Current temperature threshold
        "update_count_threshold": update_count_threshold  # Current update count threshold
    }

    return JsonResponse(response_data)

def check_alerts(city, temperature):
    global last_temperatures, exceeding_cities, temperature_threshold, update_count_threshold

    # Initialize the city's temperature list if it doesn't exist
    if city not in last_temperatures:
        last_temperatures[city] = []

    # Append the current temperature for the city
    last_temperatures[city].append(temperature)

    # Maintain only the latest `update_count_threshold` temperatures
    if len(last_temperatures[city]) > update_count_threshold:
        last_temperatures[city].pop(0)

    # Check if the threshold count has been met
    if update_count_threshold == 1:
        # Directly check if the latest temperature exceeds the threshold
        if temperature > temperature_threshold:
            exceeding_cities.append(city)
            print(f"Alert: {city} has exceeded {temperature_threshold}°C!")
    elif len(last_temperatures[city]) == update_count_threshold:
        # Check if all recent temperatures exceed the threshold
        if all(temp > temperature_threshold for temp in last_temperatures[city]):
            exceeding_cities.append(city)
            print(f"Alert: {city} has exceeded {temperature_threshold}°C for {update_count_threshold} consecutive updates!")

def temperature_stats(request):
    # Get the current date
    today = timezone.now().date()
    
    # Filter records for the current day
    records = TemperatureRecord.objects.filter(recorded_at__date=today).values('city').annotate(
        max_temp=Max('temperature'),
        min_temp=Min('temperature'),
        avg_temp=Avg('temperature')
    )
    
    stats = []
    for record in records:
        # Retrieve all temperatures for the current city today
        temperatures = list(TemperatureRecord.objects.filter(city=record['city'], recorded_at__date=today).values_list('temperature', flat=True))
        
        # Calculate mode of temperatures
        try:
            record['mode_temp'] = mode(temperatures)
        except StatisticsError:
            record['mode_temp'] = None  # Handle cases where mode cannot be determined

        # Retrieve all descriptions for the current city today
        descriptions = list(TemperatureRecord.objects.filter(city=record['city'], recorded_at__date=today).values_list('description', flat=True))
        
        # Calculate mode of descriptions
        try:
            record['mode_description'] = mode(descriptions)
        except StatisticsError:
            record['mode_description'] = None  # Handle cases where mode cannot be determined
            
        # Get the most repeated description
        if descriptions:
            record['most_repeated_description'] = max(set(descriptions), key=descriptions.count)
        else:
            record['most_repeated_description'] = None

        stats.append(record)

    return JsonResponse({"temperature_stats": stats})
