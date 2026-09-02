from flask import Flask 
import requests

app=Flask(__name__)
@app.route("/api/v1/students/1")
def student_v1():
    response=requests.get("http://localhost:5002/api/v1/course/1")
    return response.json()

@app.route("/api/v2/students/1")
def student_v2():
    response = requests.get("http://localhost:5002/api/v2/course/1")
    return response.json()

if __name__=="__main__":
    app.run(port=5001)