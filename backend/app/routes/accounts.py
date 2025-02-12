from flask import Blueprint, jsonify, request
from ..services.api import get_accounts_data

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts', methods=['GET'])
def get_accounts():
    platform = request.args.get('platform')
    if not platform:
        return jsonify({'error': 'Platform is required'}), 400

    try:
        data = get_accounts_data(platform)
        return jsonify(data), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
