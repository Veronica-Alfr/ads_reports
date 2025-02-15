from flask import Blueprint, render_template
from ..services.reports.csv.csv_generator import generate_all_insights_csv
from ..services.reports.general.general_reports_insights import get_all_platforms_insights, get_collapsed_platforms_insights

general_reports_bp = Blueprint('general_reports', __name__)

@general_reports_bp.route('/', methods=['GET'])
def get_general_platform_data():
    
    try:
        data = get_all_platforms_insights()
        return render_template('insights/table_general_insights.html', data=data)
    except Exception as e:
        return render_template('errors/error404.html', error=str(e)), 404

@general_reports_bp.route('/download_general_insights_csv', methods=['GET'])
def download_general_insights_data():
    try:
        return generate_all_insights_csv()
    except Exception as e:
        return render_template('errors/error404.html', error=str(e)), 404
    
@general_reports_bp.route('/resumo', methods=['GET'])
def get_general_summary():
    try:
        data = get_collapsed_platforms_insights()
        return render_template('insights/table_general_summary.html', data=data)
    except Exception as e:
        print('ERROR =>', e)
        return render_template('errors/error404.html', error=str(e)), 404
