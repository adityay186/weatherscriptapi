from flask import Flask, jsonify
from weather import Weather
import os
from os import environ

'''
    This Program uses OpenWeatherMapAPI.
    The program returns JSON Object of Weather Data received.
    Features an easy, fast and dynamic way of handling requests using OOPs (Object-Oriented-Programming).
'''

#initializing Flask Object
app=Flask(__name__)

apikey=environ['apikey']

#routing web server with end points
@app.route('/api/<query_city>')
def api(query_city,apikey):
    k=Weather(query_city,apikey).getWeather()
    return jsonify(k)

app.run(debug=True)