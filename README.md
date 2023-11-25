# Weather App

## Overview

The Weather App is a simple web application that allows users to retrieve weather information for a specific city using the OpenWeatherMap API. Users can input the city name, choose the temperature unit (metric, imperial, or standard), and provide an API key to get real-time weather data.

The web application is built using Flask, a lightweight web framework for Python.

## Functionality

- Users can input a city, select a temperature unit, and provide an OpenWeatherMap API key.
- The application retrieves weather data using the OpenWeatherMap API based on the user's input.
- If the data is successfully retrieved, the application displays the city name, temperature, and weather description.
- If there is an error or the data retrieval fails, an error message is displayed to the user.

## Web Service Deployment

The Weather App is deployed and accessible online at [https://weather-data-lx4x.onrender.com](https://weather-data-lx4x.onrender.com).

## Running the Code Locally

To run the Weather App locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/paulinebalmores/weather_data.git
   cd weather-app
   
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Set up your OpenWeatherMap API key:
Create an account on OpenWeatherMap to obtain an API key.
Replace "YOUR_OPENWEATHERMAP_API_KEY" in the app.py file with your actual API key.
Run the Flask application:
```bash
python app.py
```
The application will be accessible at http://localhost:5000 in your web browser.
