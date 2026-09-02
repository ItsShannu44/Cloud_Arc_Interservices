from flask import Flask

app = Flask(__name__)
@app.route("/v1/food/1")
def food_v1():
    return{
        "food_name":"Paneer Chilly",
        "price": 480
    }

@app.route("/v2/food/1")
def food_v2():
    return{
        "food_name":"Paneer Chilly",
        "Restaurant":"Swathi Veg",
        "price":480,
        "Category": "Veg"
    }

app.run(port=5002)