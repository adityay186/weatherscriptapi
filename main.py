from flask import Flask, jsonify
from weather import Weather

'''
    This Program uses OpenWeatherMapAPI.
    The program returns JSON Object of Weather Data received.
    Features an easy, fast and dynamic way of handling requests using OOPs (Object-Oriented-Programming).
'''

#initializing Flask Object
app=Flask(__name__)

#routing web server with end points
@app.route('/api/<query_city>')
def api(query_city):
    k=Weather(query_city).getWeather()
    return jsonify(k)

def main():
    app.run(debug=True)

main()