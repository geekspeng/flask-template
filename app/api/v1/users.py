from werkzeug.exceptions import BadRequest
from app.api.v1 import api_v1


@api_v1.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    raise BadRequest('valid value')
