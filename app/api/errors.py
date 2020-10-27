from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from app.exceptions import ValidationError
from . import api_errors

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_response(400, message)


def unauthorized(message):
    return error_response(401, message)


def forbidden(message):
    return error_response(403, message)


def page_not_found(message):
    return error_response(404, message)


def internal_server_error(message):
    return error_response(500, message)


@api_errors.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
