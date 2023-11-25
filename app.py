from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_weather(city, unit, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'units': unit,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
        return weather
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    unit = request.form['unit']
    api_key = request.form['api_key']

    weather_data = get_weather(city, unit, api_key)

    if weather_data:
        return render_template('weather.html', weather=weather_data)
    else:
        error_message = f"Couldn't retrieve weather data for {city}. Please check your input and try again."
        return render_template('error.html', error=error_message)


if __name__ == "__main__":
    app.run(debug=True)
