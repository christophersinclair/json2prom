import logging

from flask import request, jsonify, abort
from flasgger import swag_from

from metric import Metric

from json2prom import app


@app.route("/ingest", methods=["POST"])
@swag_from(
    {
        "parameters": [
            {
                "in": "body",
                "name": "body",
                "type": "object",
                "required": True,
                "properties": {
                    "metrics": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "metric": {
                                    "type": "object",
                                    "properties": {
                                        "metric_name": {"type": "string"},
                                        "metric_value": {"type": "string"},
                                        "metric_labels": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "foo": {"type": "string"}
                                                },
                                            },
                                        },
                                    },
                                }
                            },
                        },
                    }
                },
            }
        ]
    }
)
def ingest():
    """
    Ingest metrics from a JSON POST request
    ---
    responses:
      201:
        description: The metrics were ingested successfully
      400:
        description: The request could not be parsed
    """
    data = request.json
    metrics_ingested = data.get("metrics", [])

    m = Metric.getInstance()

    for metric in metrics_ingested:
        ingest_name = metric.get("metric", {}).get("metric_name")
        ingest_value = metric.get("metric", {}).get("metric_value")
        ingest_labels = metric.get("metric", {}).get("metric_labels")

        if ingest_name is None or ingest_value is None or ingest_labels is None:
            abort(400)

        replacement = False
        for met in m.metrics:
            # Overwrite the value already there for the same metric (for continuous updates)
            if met["name"] == ingest_name:
                replacement = True

                met["value"] = ingest_value
                met["labels"] = ingest_labels

                break

        if not replacement:
            m.metrics.append(
                {"name": ingest_name, "value": ingest_value, "labels": ingest_labels}
            )

    response = jsonify(success=True)
    response.status_code = 201
    return response
