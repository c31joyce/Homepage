from flask import *
import json

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/mechanical")
def mechanical():
	json_mechanical_data = open("data/mechanical.json")
	mechanical_data = json.load(json_mechanical_data)
	json_mechanical_data.close()
	return render_template("mechanical.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/portfolio")
def portfolio():
	return render_template("portfolio.html")

@app.route("/climbing")
def climbing():
	return render_template("climbing.html")

if __name__ == "__main__":
	app.run()