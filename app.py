from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/weather", methods=["GET"])
def weather():
    """
    Get Weather Information
    ---
    parameters:
      - name: location
        in: query
        type: string
        required: true
        description: City name
        example: New Delhi

    responses:
      200:
        description: Weather information
    """

    location = request.args.get("location")

    return {
        "location": location,
        "temperature": 32,
        "condition": "Sunny"
    }


if __name__ == "__main__":
    app.run(port=5006, debug=True)