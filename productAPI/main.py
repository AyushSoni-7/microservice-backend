from flask import Flask
import os
from routes import ROUTES
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    port = os.environ.get("port", default=5001)
    for route in ROUTES:
        app.register_blueprint(route)
    app.run(host="0.0.0.0", port=port)
