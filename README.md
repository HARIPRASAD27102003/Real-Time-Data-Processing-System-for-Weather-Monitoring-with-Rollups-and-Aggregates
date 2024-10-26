# Weather Dashboard Application

This Weather Dashboard Application is a Django-based project that provides real-time weather data, including temperature and description, for cities across the globe. Users can view daily weather statistics, toggle between temperature units (Celsius/Fahrenheit), and set threshold alerts for specific weather conditions.

---

## Features

- **Real-time Weather Data**: Fetches and displays current weather, daily summaries, and historical data.
- **Unit Toggle**: Switch between Celsius and Fahrenheit.
- **Daily Summaries**: Provides aggregated weather statistics for each city.
- **Threshold Alerts**: Receive alerts if temperature thresholds are crossed.
  
---

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (or another SQL database)
  
### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Database Configuration:**
    -Create a PostgreSQL (or other SQL) database and update DATABASES settings in settings.py

4. **Set up OpenWeatherMap API Key:**
   -Obtain your API key from [Visit OpenWeatherMap](https://openweathermap.org/).
   -Add it to settings.py as WEATHER_API_KEY.

5. **Apply Migrations:**
   ```bash
   python manage.py migrate

## API Endpoints

### 1. Home
- **URL:** `/`
- **Method:** GET
- **Description:** Loads the home page of the weather application.

### 2. Fetch Weather Data
- **URL:** `/fetch_weather_data/`
- **Method:** GET
- **Description:** Fetches current weather data from the OpenWeatherMap API for the specified cities and saves it to the database.

### 3. Temperature Statistics
- **URL:** `/temperature_stats/`
- **Method:** GET
- **Description:** Retrieves temperature statistics (e.g., max, min, average, and mode) for each city from the weather data and returns them in JSON format.

### 4. Set Temperature Threshold
- **URL:** `/set_threshold/`
- **Method:** POST
- **Description:** Allows the user to set temperature thresholds for monitoring weather conditions, which are saved to the database. The thresholds are used in the weather application to flag extreme weather conditions.
  
## Folder Structure

   <img width="633" alt="Screenshot 2024-10-26 at 18 38 02" src="https://github.com/user-attachments/assets/9b8073a4-bdf2-40b5-a9c7-f53cf77ffa68">

## Screen Shorts

<img width="1470" alt="Screenshot 2024-10-26 at 18 42 26" src="https://github.com/user-attachments/assets/fce294f3-5611-4505-9469-54f9ced7bb1f">


## Application Functionalities

1. **Current Weather Data Retrieval**
   - The application fetches real-time weather data for specified cities from the OpenWeatherMap API and displays it on the home page.

2. **Temperature Statistics Calculation**
   - It calculates various temperature statistics, including maximum, minimum, average, and mode temperatures, for the fetched weather data.

3. **Threshold Management**
   - Users can set and manage temperature thresholds for specific cities, allowing the application to monitor and alert on extreme weather conditions.

4. **Dynamic User Interface**
   - The application features a responsive UI that updates weather data and temperature statistics dynamically without requiring a full page refresh.

5. **Data Persistence**
   - Weather data and user-defined thresholds are stored in a SQLite database, ensuring that data is retained between application sessions.

6. **Statistical Display**
   - The application presents temperature statistics in a structured table format, providing users with easy access to important weather information.

