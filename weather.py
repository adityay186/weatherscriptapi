from flask import json
import urllib

#class for Weather Data Object
class Weather():
    #initializing fields
    def __init__(self,qcity): #api key goes here(get it from openweathermap.org)
        self.apikey=None
        self.qcity=qcity
        self.city = None
        self.country = None
        self.description = None
        self.curr_temp = None
        self.feels_like = None
        self.max_temp = None
        self.min_temp = None
        self.humidity = None
        self.pressure = None
        self.visibility = None
        self.wind_speed = None
        self.wind_direction=None

    #method to convert kelvin(temperature unit) to celsius(temperature unit)
    def kelvinToCelsius(self,kelvin):

        return round((kelvin-273.15),1) # °C = K - 273.15
    
    #method to convert meters(length unit) to kilometers(length unit)
    def metersToKilometers(self,meters):

        return round((meters/1000),1)

    #method to convert mps(meters/second - speed unit) to kmph(kilometers/hour - speed unit)
    def mpsToKmph(self,mps):

        return round((mps*3.6),1)

    #method to get direction of wind from degrees
    def degreesToDirection(self,degrees):
        if degrees in range(0,90):
            if degrees == 0:
                return "W"
            elif degrees == 90:
                return "N"
            else:
                return "NE"
        elif degrees in range(90,180):
            if degrees == 90:
                return "N"
            elif degrees == 180:
                return "W"
            else:
                return "NW"
        elif degrees in range(180,270):
            if degrees == 180:
                return "W"
            elif degrees == 270:
                return "S"
            else:
                return "SW"
        elif degrees >= 270:
            if degrees == 270:
                return "S"
            elif degrees > 270:
                return "SE"
            else:
                return "E"

    # A set method to set initialized variables for the weather data object
    def setWeather(self):
        f = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+self.qcity+"&appid="+self.apikey)
        result = json.loads(f.read())
        self.city=result['name']
        self.country=result['sys']['country']
        self.description=result['weather'][0]['description']
        self.curr_temp=self.kelvinToCelsius(result['main']['temp'])
        self.feels_like=self.kelvinToCelsius(result['main']['feels_like'])
        self.max_temp=self.kelvinToCelsius(result['main']['temp_max'])
        self.min_temp=self.kelvinToCelsius(result['main']['temp_min'])
        self.humidity=result['main']['humidity']
        self.pressure=result['main']['pressure']
        self.visibility=self.metersToKilometers(result['visibility'])
        self.wind_speed=self.mpsToKmph(result['wind']['speed'])
        self.wind_direction=self.degreesToDirection(result['wind']['deg'])

    #A get method to finally get the actual values of the weather object
    def getWeather(self):
        self.setWeather()

        #returning dictionary containing key and value pairs derived from weather object
        return {
            "city" : self.city,
            "country" : self.country,
            "description" : self.description,
            "curr_temperature" : self.curr_temp,
            "feels_like" : self.feels_like,
            "max_temp" : self.max_temp,
            "min_temp" : self.min_temp,
            "humidity" : self.humidity,
            "pressure" : self.pressure,
            "visibility" : self.visibility,
            "wind_speed" : self.wind_speed,
            "wind_direction":self.wind_direction
        }