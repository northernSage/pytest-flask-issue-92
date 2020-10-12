import os
from flask import Flask, request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/security', methods=["POST", "GET"])
    def security():
        if request.method == "POST":
            return "post request received"
        return "get request received"

    return app