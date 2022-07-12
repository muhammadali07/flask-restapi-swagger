"""A Python Flask REST API (CRUD)"""

import argparse
import logging
import os
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from api import (
    product
)
from db import engine, Base

app = Flask(__name__)

# engine = create_engine('mysql+mysqldb://scott:tiger@localhost/db')
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://scott:tiger@localhost/db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Restfull API"
    }
)

db = SQLAlchemy(app)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


app.register_blueprint(product.get_blueprint())


async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        db.create_all()


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Flask Restfull API")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(app)
        startup()
        app.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        app.run(host='0.0.0.0', port=PORT, debug=False)