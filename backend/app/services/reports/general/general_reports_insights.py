import logging
from ....utils.api_requests import get_platforms_data
from ..platform.platform_reports_insights import platform_insights

def get_all_platforms_insights():
    platforms = get_platforms_data()
    all_insights = []

    for platform in platforms:
        platform_key_value = platform['value']
        try:
            platform_data = platform_insights(platform_key_value)
            all_insights.extend(platform_data)
        except ValueError as e:
            logging.error(f"Error fetching insights for platform {platform_key_value}: {str(e)}")
            continue
        
    print('all_insights =>', all_insights)

    return all_insights