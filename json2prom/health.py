from flask import jsonify

from json2prom import app


@app.route("/", methods=["GET"])
def index():
    """
    The index endpoint of json2prom
    ---
    responses:
      200:
        description: A greeting message for the json2prom API is returned
    """
    return jsonify("JSON2Prom - Convert JSON to Prometheus Metrics!")


@app.route("/health", methods=["GET"])
def health():
    """
    A simple healthcheck endpoint
    ---
    responses:
      200:
        description: A simple healthcheck endpoint for the json2prom API
    """
    response = jsonify(success=True)
    response.status_code = 200
    return response