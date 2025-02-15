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
            
            for account in platform_data:
                for insight in account['insights']:
                    if 'Cost Per Click' not in insight:
                        clicks = insight.get('Clicks', 0)
                        spend = insight.get('Spend', 0)
                        
                        if clicks and spend:
                            insight['Cost Per Click'] = round(spend / clicks, 2)
                        else:
                            insight['Cost Per Click'] = ""
                
                all_insights.append(account)
                
        except ValueError as e:
            logging.error(f"Error fetching insights for platform {platform_key_value}: {str(e)}")
            continue

    return all_insights

def get_collapsed_platforms_insights():
    all_insights = get_all_platforms_insights()

    all_columns = set()
    for account in all_insights:
        for insight in account['insights']:
            all_columns.update(insight.keys())
    
    all_columns = sorted(all_columns)

    collapsed_data = {}

    for account in all_insights:
        platform_name = account['platform']

        if platform_name not in collapsed_data:
            collapsed_data[platform_name] = {
                'platform': platform_name,
                'insights': {col: "" for col in all_columns}
            }

        for insight in account['insights']:
            for key, value in insight.items():
                if isinstance(value, (int, float)):
                    if collapsed_data[platform_name]['insights'][key] == "":
                        collapsed_data[platform_name]['insights'][key] = 0
                    collapsed_data[platform_name]['insights'][key] += value
                elif isinstance(value, str) and value != "":
                    if key == 'platform':
                        collapsed_data[platform_name]['insights'][key] = platform_name
                    else:
                        collapsed_data[platform_name]['insights'][key] = ""

    return list(collapsed_data.values())
