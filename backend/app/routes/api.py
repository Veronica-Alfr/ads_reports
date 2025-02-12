from flask import Blueprint, jsonify, request
from ..services.api import get_platforms_data, get_accounts_data, get_fields_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/<endpoint>', methods=['GET'])
def get_data(endpoint):
    """
    Endpoint genérico para fazer requisições com parâmetros dinâmicos.
    """
    params = request.args.to_dict()

    if 'platform' not in params and endpoint != 'platforms':
        return jsonify({'error': 'Platform is required'}), 400

    try:
        if endpoint == 'platforms':
            data = get_platforms_data()
        elif endpoint == 'accounts':
            data = get_accounts_data(params)
        elif endpoint == 'fields':
            data = get_fields_data(params)
        else:
            return jsonify({'error': f'Unknown endpoint: {endpoint}'}), 404

        return jsonify(data), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
