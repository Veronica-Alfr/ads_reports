from flask import Blueprint, jsonify, abort
from ..services.reports.platform.reports_platform import platform_insights

reports_platform_bp = Blueprint('reports_platform', __name__)

@reports_platform_bp.route('/<platform_name>', methods=['GET'])
def get_platform_data(platform_name):
    try:
        data = platform_insights(platform_name)
        return jsonify(data)
    except ValueError as e:
        abort(404, description=str(e))
