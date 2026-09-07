from flask import Flask

app=Flask(__name__)

@app.route("/books/1")
def ger_books():
    return{
        "id": 1,
        "title":"Python Programming"
    }

if __name__=="__main__":
    app.run(port=5050)