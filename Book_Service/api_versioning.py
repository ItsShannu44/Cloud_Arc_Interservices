from flask import Flask

app = Flask(__name__)
@app.route("/api/v1/books/1")
def book_v1():
    return{
        "id":1,
        "name":"ANSI C"
    }

@app.route("/api/v2/books/1")
def book_v2():
    return{
        "id":1,
        "title": "Progressive Web Apps",
        "author": "John"
    }

app.run(port=5002)