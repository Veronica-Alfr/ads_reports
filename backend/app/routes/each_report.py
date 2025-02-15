from flask import Blueprint, render_template
from ..services.reports.platform.platform_reports_insights import platform_insights, collapsed_platform_insights
from ..services.reports.csv.csv_generator import generate_insights_summary_csv, generate_csv_insights

reports_platform_bp = Blueprint('reports_platform', __name__)

@reports_platform_bp.route('/<platform_name>', methods=['GET'])
def get_platform_data(platform_name):
    try:
        data = platform_insights(platform_name)
        return render_template('insights/table_insights.html', data=data)
    except ValueError as e:
        return render_template('errors/error404.html', error=str(e)), 404
    
@reports_platform_bp.route('/<platform_name>/download_csv', methods=['GET'])
def download_platform_insights_data(platform_name):
    try:
        return generate_csv_insights(platform_name)
    except ValueError as e:
        return render_template('errors/error404.html', error=str(e)), 404
    
@reports_platform_bp.route('/<platform_name>/resumo', methods=['GET'])
def get_collapsed_platform_data(platform_name):
    try:
        data = collapsed_platform_insights(platform_name)
        return render_template('insights/table_collapsed_insights.html', data=data)
    except ValueError as e:
        return render_template('errors/error404.html', error=str(e)), 404

@reports_platform_bp.route('/<platform_name>/resumo/download_csv', methods=['GET'])
def download_collapsed_platform_data(platform_name):
    try:
        return generate_insights_summary_csv(platform_name)
    except ValueError as e:
        return render_template('errors/error404.html', error=str(e)), 404
