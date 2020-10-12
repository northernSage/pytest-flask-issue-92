import os
from flask import Flask, request, jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/', methods=["POST", "GET"])
    def auth():
        json_data = request.get_json()
        print(json_data)
        username = json_data['username']
        password = json_data['password']
        return jsonify(token=f"t-{username}@{password}")

    return app