from flask import Blueprint, jsonify
from ..services.api import get_platforms_data

platforms_bp = Blueprint('platforms', __name__)

@platforms_bp.route('/platforms', methods=['GET'])
def get_platforms():
    try:
        data = get_platforms_data()
        return jsonify(data), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500
