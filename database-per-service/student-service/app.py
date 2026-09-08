from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB = "student.db"


def init_db():
    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    conn.execute("INSERT OR IGNORE INTO students VALUES(101, 'John')")
    conn.execute("INSERT OR IGNORE INTO students VALUES(102, 'Max')")

    conn.commit()
    conn.close()


@app.route("/students/<int:student_id>")
def get_student(student_id):
    conn = sqlite3.connect(DB)
    cursor = conn.execute(
        "SELECT id, name FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "id": student[0],
        "name": student[1]
    })


if __name__ == "__main__":
    init_db()
    app.run(port=5010)