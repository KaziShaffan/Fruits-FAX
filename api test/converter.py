from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/api/ALL")
def allfruits():
    try:
        response = requests.get("https://www.fruityvice.com/api/fruit/all")
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        fruits = response.json()
        return jsonify({"data": fruits})
    except Exception as error:
        print("COULD NOT FEACH API", error)
        return jsonify({"ERROR INTERNET PROBLEMS"}), 500


@app.route("/api/<fruitname>")
def specificfruit(fruitname):
    try:
        response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruitname}")
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        fruit = response.json()

        formatted_fruit = {
            "name": fruit.get("name"),
            "nutritions": fruit.get("nutritions", {}),
        }

        return jsonify(formatted_fruit)
    except Exception as error:
        print("COULD NOT FEACH API", error)
        return jsonify({"ERROR INTERNET PROBLEMS"}), 500


if __name__ == "__main__":
    app.run(port=6969)
