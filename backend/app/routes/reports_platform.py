from flask import Blueprint, Response, render_template
from ..services.reports.platform.reports_platform import platform_insights
from ..services.reports.csv.csv_generator import generate_csv_insights
from ..utils.get_platform_value import get_platform_value_by_name

reports_platform_bp = Blueprint('reports_platform', __name__)

@reports_platform_bp.route('/<platform_name>', methods=['GET'])
def get_platform_data(platform_name):
    try:
        data = platform_insights(platform_name)
        return render_template('table_insights.html', data=data)
    except ValueError as e:
        return render_template('error.html', error=str(e)), 404
    
@reports_platform_bp.route('/<platform_name>/download_csv', methods=['GET'])
def download_platform_insights_data(platform_name):
    print('platform_name =>', platform_name)
    try:
        platform_value = get_platform_value_by_name(platform_name)

        data = platform_insights(platform_value)
        
        csv_output = generate_csv_insights(data)
        
        return Response(
            csv_output,
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment;filename={platform_name}_insights.csv"}
        )
    except ValueError as e:
        return render_template('error.html', error=str(e)), 404
