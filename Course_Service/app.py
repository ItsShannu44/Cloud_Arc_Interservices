from flask import Flask

app = Flask(__name__)
@app.route("/api/v1/course/1")
def book_v1():
    return{
        "course_code":"MCA101",
        "course_name":"Java Enterprise Application Dev"
    }

@app.route("/api/v2/course/1")
def book_v2():
    return{
        "course_name":"Web App Development",
        "faculty":"John Doe",
        "avl_seats":25
    }

app.run(port=5002)