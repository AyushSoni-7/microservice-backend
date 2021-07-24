from flask import Flask
import os
from flask_cors import CORS
from flask_restful import Api
from resources import ROUTES_MAP


def create_app():
    flask_app = Flask(__name__)
    cors = CORS(flask_app)
    flask_app.config['CORS_HEADERS'] = 'Content-Type'
    api = Api(flask_app)
    for route in ROUTES_MAP:
        api.add_resource(route["resource"], route["route"])
    return flask_app


if __name__ == "__main__":
    port = os.environ.get("port")
    app = create_app()
    app.run(host="0.0.0.0", port=port)
