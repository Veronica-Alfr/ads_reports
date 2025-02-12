from flask import Blueprint, jsonify, request
from ..services.api import get_fields_data

fields_bp = Blueprint('fields', __name__)

@fields_bp.route('/fields', methods=['GET'])
def get_fields():
    platform = request.args.get('platform')

    if not platform:
        return jsonify({'error': 'Platform is required'}), 400

    try:
        data = get_fields_data(platform)
        return jsonify(data), 200
    except ValueError as value:
        return jsonify({'error': str(value)}), 400
    except Exception as error:
        return jsonify({'error': str(error)}), 500
