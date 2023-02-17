from flask import Flask
import status

app = Flask(__name__)

COUNTERS = {}


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Creates a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS

    if name in COUNTERS:
        return {"message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Updates a counter"""
    app.logger.info(f"Request to update the counter: {name}")
    global COUNTERS

    if name in COUNTERS:
        COUNTERS[name] += 1
    else:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND
    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route("/counters/<name>", methods=["GET"])
def get_counter(name):
    """Returns the value of the counter"""
    app.logger.info(f"Request to fetch the counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK
    else:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    app.logger.info(f"Request to delete the counter {name}")
    global COUNTERS
    if name in COUNTERS:
        del COUNTERS[name]
        return '', status.HTTP_204_NO_CONTENT
    else:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND
