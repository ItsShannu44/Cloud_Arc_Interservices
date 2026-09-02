from flask import Flask 
import requests

app=Flask(__name__)
@app.route("/v1/food_del/1")
def student_v1():
    response=requests.get("http://localhost:5002/v1/food/1")
    return response.json()

@app.route("/v2/food_del/1")
def student_v2():
    response = requests.get("http://localhost:5002/v2/food/1")
    return response.json()

if __name__=="__main__":
    app.run(port=5001)