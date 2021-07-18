from flask import Flask
import os
from flask_cors import CORS
from routes import ROUTES


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    port = os.environ.get("port")
    for route in ROUTES:
        app.register_blueprint(route)
    app.run(host="0.0.0.0", port=port)
