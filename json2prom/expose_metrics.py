import logging

from flask import jsonify, make_response

from metric import Metric

from json2prom import app


def get_metrics():
    m = Metric.getInstance()
    prom = ""

    for metric in m.metrics:
        prom += f"{metric['name']}"
        prom += "{"
        for label in metric['labels']:
            for key, value in label.items():
                prom += f'{key}="{value}"'
        prom = prom[:-1]
        prom += "}"
        prom += f"{metric['value']}"
        prom += "\n"

    return prom


@app.route("/metrics", methods=["GET"])
def expose_metrics():
    """
    Expose metrics for Prometheus in PromQL format
    ---
    responses:
      200:
        description: All metrics contained inside response
    """
    response = make_response(get_metrics(), 200)
    response.mimetype = "text/plain"
    return response