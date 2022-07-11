import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

data = {
    "nama":"muh ali bakhtiar"
}

@REQUEST_API.route('/request', methods=['GET'])
def get_records():
    """Return all book requests
    @return: 200: an array of all known BOOK_REQUESTS as a \
    flask/response object with application/json mimetype.
    """
    return jsonify(data)
