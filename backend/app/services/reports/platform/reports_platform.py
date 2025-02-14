import uuid
import logging
from ....services.API.api_stract import get_accounts_data, get_fields_data, get_insights_data
from ....utils.api_requests import get_platforms_data

def platform_insights(platform_name):
    print('platform_name on platform_insights(platform_name) =>', platform_name)
    platforms = get_platforms_data()

    platform = next((p for p in platforms if p['value'] == platform_name), None)
    if not platform:
        raise ValueError(f"Platform '{platform_name}' not found.")

    platform_value = platform['value']
    
    formatted_data = []

    fields_data = get_fields_data({'platform': platform_value})

    fields = fields_data.get('fields', [])

    field_values = ','.join([field['value'] for field in fields])

    accounts_data = get_accounts_data({'platform': platform_value})
    accounts = accounts_data.get('accounts', [])

    for account in accounts:
        account_id = account['id']
        account_token = account['token']

        try:
            insights_data = get_insights_data(platform_value, {
                'account': account_id,
                'token': account_token,
                'fields': field_values
            })
            insights = insights_data.get('insights', [])

            account_insights = []

            for insight in insights:
                insight_dict = {}

                for field in fields:
                    field_text = field['text']
                    field_value = field['value']

                    if field_value in insight:
                        insight_dict[field_text] = insight[field_value]

                account_insights.append(insight_dict)

            formatted_data.append({
                'uuid': str(uuid.uuid4()),
                'account_id': account_id,
                'account_name': account['name'],
                'platform': platform['text'],
                'insights': account_insights
            })

        except ValueError as e:
            logging.error(f"Error fetching insights for account {account_id}: {str(e)}")
            continue

    return formatted_data
