from flask import Blueprint, render_template
from ..services.reports.platform.reports_platform import platform_insights

reports_platform_bp = Blueprint('reports_platform', __name__)

@reports_platform_bp.route('/<platform_name>', methods=['GET'])
def get_platform_data(platform_name):
    try:
        data = platform_insights(platform_name)
        return render_template('table_insights.html', data=data)
    except ValueError as e:
        return render_template('error.html', error=str(e)), 404
