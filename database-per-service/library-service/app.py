from flask import Flask
import requests
import sqlite3

app = Flask(__name__)

DB = "library.db"
STUDENT_SERVICE = "http://localhost:5010"
BOOK_SERVICE = "http://localhost:5002"


def init_db():
    conn = sqlite3.connect(DB)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS borrowings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            book_id INTEGER
        )
    """)

    conn.commit()
    conn.close()


@app.route("/borrow/<int:student_id>/<int:book_id>")
def borrow_book(student_id, book_id):

    # Check student
    student_response = requests.get(
        f"{STUDENT_SERVICE}/students/{student_id}"
    )

    if student_response.status_code != 200:
        return {"error": "Student not found"}, 404

    # Check book
    book_response = requests.get(
        f"{BOOK_SERVICE}/books/{book_id}"
    )

    if book_response.status_code != 200:
        return {"error": "Book not found"}, 404

    student = student_response.json()
    book = book_response.json()

    # Store borrowing
    conn = sqlite3.connect(DB)

    cursor = conn.execute(
        "INSERT INTO borrowings(student_id, book_id) VALUES (?, ?)",
        (student_id, book_id)
    )

    borrowing_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return {
        "message": "Book borrowed successfully",
        "borrowing_id": borrowing_id,
        "student": student,
        "book": book
    }, 201


if __name__ == "__main__":
    init_db()
    app.run(port=5003)