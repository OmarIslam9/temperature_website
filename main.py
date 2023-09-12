from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '5c8aa7b09e0f3b8333ad07670274b44e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()

    if response['cod'] == '404':
        error_message = "City not found. Please try again."
        return render_template('index.html', error=error_message)

    weather_data = {
        'city': response['name'],
        'temperature': round(response['main']['temp'] - 273.15, 1),  # Convert temperature to Celsius
        'humidity': response['main']['humidity'],
        'description': response['weather'][0]['description'],
    }

    return render_template('weather.html', weather=weather_data)


if __name__ == '__main__':
    app.run(debug=True)