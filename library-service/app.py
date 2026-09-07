from flask import Flask
import requests
import time

app = Flask(__name__)

BOOK_SERVICE = "http://localhost:5050"

failure_count = 0
failure_threshold = 3

circuit_state = "CLOSED"
open_time = None
timeout = 15


def call_book_service():
    global failure_count
    global circuit_state
    global open_time

    if circuit_state == "OPEN":

        if time.time() - open_time < timeout:
            return {
                "error": "Circuit is OPEN. Book Service is unavailable.",
                "circuit_state": "OPEN"
            }, 503

        else:
            circuit_state = "HALF-OPEN"
            print("Circuit changed to HALF-OPEN")
            return {
                "message": "Circuit is HALF-OPEN",
                "circuit_state": "HALF-OPEN"
            }, 200  


    try:
        response = requests.get(
            f"{BOOK_SERVICE}/books/1",
            timeout=2
        )

        if response.status_code == 200:

            failure_count = 0
            circuit_state = "CLOSED"
            open_time = None

            return response.json(), 200

        else:
            raise Exception("Service Failure")


    except Exception:

        if circuit_state == "HALF-OPEN":

            circuit_state = "OPEN"
            open_time = time.time()

            return {
                "error": "Book Service still unavailable.",
                "circuit_state": "OPEN"
            }, 503


        failure_count += 1

        if failure_count >= failure_threshold:

            circuit_state = "OPEN"
            open_time = time.time()

        return {
            "error": "Book Service Failed",
            "circuit_state": circuit_state,
            "failure_count": failure_count
        }, 503


@app.route("/borrow")
def borrow():

    book, status = call_book_service()

    return {
        "book": book,
        "circuit_state": circuit_state
    }, status


app.run(port=5051)