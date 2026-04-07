from flask import *

app = Flask(__name__)

PLANET_GRAVITY = {
    'Mercury': 0.38,
    'Venus': 0.91,
    'Earth':1.00,
    'Mars': 0.38,
    'Jupiter': 2.34,
    'Saturn': 0.93,
    'Uranus': 0.92,
    'Neptune': 1.12,
}

@app.route('/')
def home():
    return render_template('website.html')

@app.route('/planets')
def planets():
    weight = request.args.get('weight', '')
    return render_template('planets.html', weight=weight)

@app.route('/result')
def result():
    weight = float(request.args.get('weight', '0'))
    planet = request.args.get('planet', 'Earth')
    gravity = PLANET_GRAVITY.get(planet, 1.0)
    planet_weight = round(weight * gravity, 2)
    return render_template('result.html', weight=weight, planet=planet, planet_weight=planet_weight)


if __name__ == '__main__':
    app.run(debug=True, port = 5001)