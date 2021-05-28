from flask import Flask, render_template
import requests as r
import json
app = Flask(__name__)

url = r.get(
    "https://raw.githubusercontent.com/muhiqsimui/PyTraining/main/json/rs.json")
rsud = url.json()


@ app.route("/")
def web():
    return render_template("index.php", rsud=rsud)


@ app.route("/web")
def website():
    return "posible"


if __name__ == "__main__":
    app.run(debug=True)
