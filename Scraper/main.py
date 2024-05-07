from flask import Flask, request, jsonify
from test import WebDriver

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

@app.route("/rating", methods=["POST"])
def rating():
    data = request.get_json()
    data2 = list(data.keys())
    ratings = WebDriver.findPoiRating(WebDriver, data2)
    return jsonify(ratings), 200


if __name__ == '__main__':
    app.run(debug=True)