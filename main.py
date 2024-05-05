import requests
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
        data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=b21a2633ddaac750a77524f91fe104e7')
        data = data.json()

        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]
        img = data["weather"][0]["icon"]
        return render_template('weather.html', img=img, temp=temp, pressure=pressure, humidity=humidity, wind=wind, city_name=city_name)
    
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)

