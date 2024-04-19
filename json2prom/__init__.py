import logging
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "JSON2Prom",
        "description": "Post values in JSON you want to expose as Prometheus metrics!",
        "version": "1.0"
    }
}
swagger = Swagger(app, template=swagger_template)

from json2prom import health, ingest, expose_metrics, expose_json