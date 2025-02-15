import requests
from ..config import Config

def get_platforms_data():
    if not hasattr(get_platforms_data, "platform_cache"):
        headers = {
            'Authorization': f'{Config.STRACT_API_TOKEN}',
        }

        response = requests.get(f"{Config.BASE_URL}/platforms", headers=headers)
        response.raise_for_status()

        get_platforms_data.platform_cache = response.json().get('platforms', [])

    return get_platforms_data.platform_cache

def make_api_request(endpoint, params):
    platforms = get_platforms_data()

    platform_param = params['platform']

    if not platform_param:
        raise ValueError("Platform is required in query parameters.")
    
    valid_platforms = [p['value'] for p in platforms]
    if platform_param not in valid_platforms:
        raise ValueError(f"Invalid Platform: {platform_param}.")

    headers = {
        'Authorization': f'{Config.STRACT_API_TOKEN}',
    }

    url = f"{Config.BASE_URL}/{endpoint}"
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()
