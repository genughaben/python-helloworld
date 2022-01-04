import logging
from datetime import datetime

from flask import Flask
from flask import json
from enums.ResponseType import ResponseType
from enums.Endpoints import Endpoints

app = Flask(__name__)
app.log = logging.getLogger(__name__)


def _get_timestamp():
    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())


@app.route("/")
def hello():
    app.log.info(f"{_get_timestamp()} -  {Endpoints.HELLO.value}, endpoint was reached")
    return "Hello World!"


@app.route("/status")
def health():
    app.log.info(f"{_get_timestamp()} -  {Endpoints.HEALTH.value}, endpoint was reached")
    return app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )


@app.route("/metrics")
def metrics():
    app.log.info(f"{_get_timestamp()} -  {Endpoints.METRICS.value}, endpoint was reached")
    return app.response_class(
        response=json.dumps({
            "status": ResponseType.SUCCESS.value,
            "code":0,
            "data": {"UserCount": 140, "UserCountActive": 23}
        }),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host='0.0.0.0')
