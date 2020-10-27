from flask import Flask, request, current_app
from flask import jsonify
from flask_babel import Babel

from config import config

babel = Babel()


def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors."""
    payload = {'error': error.name}
    if error.description:
        payload['message'] = error.description
    response = jsonify(payload)
    response.status_code = error.code
    return response


def create_app(config_name='default'):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    babel.init_app(app)


    from werkzeug.exceptions import HTTPException
    app.register_error_handler(HTTPException, handle_exception)

    from app.api.v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
