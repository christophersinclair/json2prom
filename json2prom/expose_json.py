import logging

from flask import jsonify, make_response

from metric import Metric

from json2prom import app


@app.route("/json", methods=["GET"])
def expose_json():
    """
    Expose metrics for Prometheus in JSON format
    ---
    responses:
      200:
        description: All metrics contained inside response
    """
    m = Metric.getInstance()
    response = make_response(jsonify(m.metrics), 200)
    response.mimetype = "application/json"
    return response
