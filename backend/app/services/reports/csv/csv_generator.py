import csv
import io
from flask import Response
from ....utils.get_platform_value import get_platform_value_by_name
from ...reports.platform.platform_reports_insights import platform_insights, collapsed_platform_insights
from ...reports.general.general_reports_insights import get_all_platforms_insights

def generate_csv_insights(platform_name):
    platform_value = get_platform_value_by_name(platform_name)

    data = platform_insights(platform_value)

    output = io.StringIO()
    writer = csv.writer(output)
    
    headers = ['Account Owner', 'Platform'] + list(data[0]['insights'][0].keys())
    writer.writerow(headers)
    
    for account in data:
        for insight in account['insights']:
            row = [account['account_name'], account['platform']] + list(insight.values())
            writer.writerow(row)
    
    csv_bytes = output.getvalue().encode('utf-8')

    return Response(
        csv_bytes,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment;filename={platform_value}_insights.csv"}
    )

def generate_insights_summary_csv(platform_name):    
    platform_value = get_platform_value_by_name(platform_name)

    data = collapsed_platform_insights(platform_value)
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    if data:
        headers = ['Account Owner', 'Platform'] + list(data[0]['insights'].keys())
        writer.writerow(headers)
        
        for account in data:
            row = [account['account_name'], account['platform']] + list(account['insights'].values())
            writer.writerow(row)
    
    csv_bytes = output.getvalue().encode('utf-8')

    return Response(
        csv_bytes,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment;filename={platform_value}_summary_insights.csv"}
    )

def generate_all_insights_csv():
    data = get_all_platforms_insights()

    all_columns = set()
    for account in data:
        for insight in account['insights']:
            all_columns.update(insight.keys())
    
    all_columns = sorted(all_columns)
    
    headers = ['Account Owner', 'Platform'] + all_columns

    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(headers)

    for account in data:
        for insight in account['insights']:
            row = [account['account_name'], account['platform']]
            for column in all_columns:
                row.append(insight.get(column, ""))
            writer.writerow(row)
    
    csv_bytes = output.getvalue().encode('utf-8')

    return Response(
        csv_bytes,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=all_platforms_insights.csv"}
    )