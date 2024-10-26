# 🌦️ Weather Dashboard Application

Welcome to the **Weather Dashboard Application**—a user-friendly, Django-based weather platform offering real-time weather data for cities worldwide. With this intuitive interface, you can view current temperatures, daily summaries, historical data, and even set custom alerts for temperature thresholds.

---

## 🌟 Key Features

- **Real-Time Weather Updates**  
  Get accurate, up-to-date weather information, including temperature, conditions, and humidity.

- **Unit Toggle**  
  Easily switch between Celsius and Fahrenheit views with a simple toggle for a personalized experience.

- **Daily Summaries**  
  View aggregated daily statistics that keep you informed on temperature trends, rainfall, and other weather metrics.

- **Threshold Alerts**  
  Set custom temperature alerts, receiving notifications when temperatures exceed or drop below your specified limits.

---

## 🖼️ User Interface Overview

The **Weather Dashboard Application** is designed to be clean, responsive, and user-friendly. Here’s what you can expect:

- **Dashboard**  
  The central hub displaying real-time weather, recent trends, and unit toggle options.

- **City Search Bar**  
  Easily search for any city worldwide and instantly get its current weather.

- **Settings & Alerts**  
  Set threshold alerts and customize your preferred temperature units.

- **Responsive Design**  
  Works seamlessly across desktop, tablet, and mobile devices for weather updates on the go.

---

## 🚀 Installation Guide

Follow these steps to set up the Weather Dashboard Application:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/weather-dashboard.git
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

6. **Run Application**:

   ```bash
   python manage.py runserver

## 🌐 API Endpoints

---

### 1. **Home**
   - **URL:** `/`
   - **Method:** `GET`
   - **Description:** Loads the home page of the Weather Dashboard Application.

---

### 2. **Fetch Weather Data**
   - **URL:** `/fetch_weather_data/`
   - **Method:** `GET`
   - **Description:** Fetches current weather data from the OpenWeatherMap API for specified cities and stores it in the database.

---

### 3. **Temperature Statistics**
   - **URL:** `/temperature_stats/`
   - **Method:** `GET`
   - **Description:** Retrieves temperature statistics for each city, including maximum, minimum, average, and mode, from stored weather data. The data is returned in JSON format.

---

### 4. **Set Temperature Threshold**
   - **URL:** `/set_threshold/`
   - **Method:** `POST`
   - **Description:** Enables users to set temperature thresholds for monitoring. Thresholds are saved in the database and used to alert users of extreme weather conditions.

---

**These endpoints enable efficient interaction with the Weather Dashboard Application, offering both data retrieval and user-configurable alerts.**

  
## 📁 Folder Structure

   <img width="633" alt="Screenshot 2024-10-26 at 18 38 02" src="https://github.com/user-attachments/assets/9b8073a4-bdf2-40b5-a9c7-f53cf77ffa68">

## 📸 Screenshots

| Home Page                                          | Weather Data Overview                               |
|----------------------------------------------------|----------------------------------------------------|
| ![Home Page Screenshot](https://github.com/user-attachments/assets/fce294f3-5611-4505-9469-54f9ced7bb1f) | ![Weather Overview](https://github.com/user-attachments/assets/c9cea736-afa4-4a11-9bfd-ee845cf75949) |

| Temperature Statistics                             | Threshold Alert Settings                           |
|----------------------------------------------------|----------------------------------------------------|
| ![Temperature Statistics](https://github.com/user-attachments/assets/f3a7de99-d088-4cd1-ae3b-2778e2fcd45c) | ![Threshold Settings](https://github.com/user-attachments/assets/bba2206d-5bc9-44b3-b2ba-9f275436d9a6) |

Each screenshot highlights key features of the Weather Dashboard Application, from the main page to statistical displays and user-configurable alert settings.


## 🌟 Application Functionalities

---

1. **Current Weather Data Retrieval**
   - Retrieves and displays real-time weather data for specified cities via the OpenWeatherMap API on the home page.

---

2. **Temperature Statistics Calculation**
   - Calculates key temperature statistics, including maximum, minimum, average, and mode, for the current weather data.

---

3. **Threshold Management**
   - Enables users to set and manage temperature thresholds for specific cities, allowing the application to monitor and provide alerts for extreme weather conditions.

---

4. **Dynamic User Interface**
   - Features a responsive UI that dynamically updates weather data and statistics without requiring a full page refresh.

---

5. **Data Persistence**
   - Stores weather data and user-defined thresholds in a SQLite database, ensuring data retention across application sessions.

---

6. **Statistical Display**
   - Presents temperature statistics in a structured table format, providing clear and accessible weather information for users.

---

**These functionalities make the Weather Dashboard a robust tool for real-time weather tracking, data visualization, and alerting.**

### Notes:
- Ensure that you have a `LICENSE` file in your repository that contains the full text of the MIT License.
- Adjust any wording in the Contribution section as necessary to fit your project's workflow or guidelines.
