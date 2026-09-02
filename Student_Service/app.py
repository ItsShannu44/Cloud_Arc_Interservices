from flask import Flask
import requests

app = Flask(__name__)
@app.route("/student-book")
def student_book():
    response= requests.get("http://localhost:5001/books")
    return response.json()

if __name__=="__main__":
    app.run(port =5002, debug=True)