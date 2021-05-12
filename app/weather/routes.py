from flask import jsonify
from app.weather import bp
from app.weather.controller import WeatherController

from flask import jsonify


@bp.route('/fetch', methods=['GET'])
def insertWeatherData():
    c = WeatherController()
    c.insertWeather()

    return "Weather data inserted"

@bp.route('', methods=['GET'])
def getWeather():
    c = WeatherController()
    result = c.getWeather()

    return jsonify(result)
