from flask import Blueprint, jsonify, request
from ..utils.api_requests import get_platforms_data
from ..services.API.api_stract import get_accounts_data, get_fields_data, get_insights_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/<endpoint>', methods=['GET'])
def get_data(endpoint):
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
        elif endpoint == 'insights':
            platform = params['platform']
            data = get_insights_data(platform, params)
        else:
            return jsonify({'error': f'Unknown endpoint: {endpoint}'}), 404

        return jsonify(data), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
