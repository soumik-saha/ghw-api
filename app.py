from flask import Flask, request
import fcntl

app = Flask(__name__)

weather = {
    "Kolkata" : {
        "coord": {
            "lon": 88.3697,
            "lat": 22.5697
        },
        "weather": [
            {
                "id": 721,
                "main": "Haze",
                "description": "haze",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 33.97,
            "feels_like": 37.05,
            "temp_min": 33.97,
            "temp_max": 33.97,
            "pressure": 1013,
            "humidity": 46
        },
        "visibility": 3200,
        "wind": {
            "speed": 3.09,
            "deg": 260
        },
        "clouds": {
            "all": 2
        },
        "dt": 1680843867,
        "sys": {
            "type": 1,
            "id": 9114,
            "country": "IN",
            "sunrise": 1680825236,
            "sunset": 1680870199
        },
        "timezone": 19800,
        "id": 1275004,
        "name": "Kolkata",
        "cod": 200
    },
    "London" : {
        "coord": {
            "lon": -0.1257,
            "lat": 51.5085
        },
        "weather": [
            {
                "id": 803,
                "main": "Clouds",
                "description": "broken clouds",
                "icon": "04n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 4.84,
            "feels_like": 3.12,
            "temp_min": 1.7,
            "temp_max": 6.86,
            "pressure": 1018,
            "humidity": 88
        },
        "visibility": 10000,
        "wind": {
            "speed": 2.06,
            "deg": 310
        },
        "clouds": {
            "all": 75
        },
        "dt": 1680843603,
        "sys": {
            "type": 2,
            "id": 2075535,
            "country": "GB",
            "sunrise": 1680844983,
            "sunset": 1680892922
        },
        "timezone": 3600,
        "id": 2643743,
        "name": "London",
        "cod": 200
    },
    "Seattle": {
        "coord": {
            "lon": -122.3321,
            "lat": 47.6062
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 9.62,
            "feels_like": 7.48,
            "temp_min": 8.53,
            "temp_max": 10.66,
            "pressure": 1007,
            "humidity": 91
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.12,
            "deg": 110
        },
        "rain": {
            "1h": 0.75
        },
        "clouds": {
            "all": 100
        },
        "dt": 1680843734,
        "sys": {
            "type": 2,
            "id": 2041694,
            "country": "US",
            "sunrise": 1680788282,
            "sunset": 1680835505
        },
        "timezone": -25200,
        "id": 5809844,
        "name": "Seattle",
        "cod": 200
    }
}

@app.route("/")
def hello_ghw():
    return "<p>Hello, API Week Hackers!</p>"

@app.route("/weather", methods=['GET','POST'])
def getWeather():
    if request.method == 'POST':
        weather["New Hackathon"] = request.json
        return weather
    else:
        return weather

if __name__ == "__main__":
    app.run(debug = True)