from flask import Flask, render_template
from urllib import request
import json
app = Flask(__name__)

@app.route("/")
def index():
    popLink = "https://www.toontownrewritten.com/api/population"
    resp = request.urlopen(popLink)
    population = resp.read().decode()
    population = json.loads(population)
    sortedDistricts = {dis: pop for dis, pop in sorted(population["populationByDistrict"].items())}

    return render_template('index.html', total_pop = population, popByDistrict = sortedDistricts)

if __name__ == '__main__':
    app.run(debug=True)