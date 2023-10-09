from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        location = request.form.get('location')
        weather = get_weather(location)
    return render_template('index.html', weather=weather)

def get_weather(location):
    api_url = f"http://api.weatherapi.com/v1/current.json?key=18ff27d5db9c4f5e8c384211230910&q={location}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    app.run(debug=True)
