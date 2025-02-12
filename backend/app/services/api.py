import requests
from ..config import Config

def get_platforms_data():
    """Faz a requisição para o endpoint /platforms e armazena as plataformas"""
    if not hasattr(get_platforms_data, "platform_cache"):
        headers = {
            'Authorization': f'{Config.STRACT_API_TOKEN}',
        }

        response = requests.get(f"{Config.BASE_URL}/platforms", headers=headers)
        response.raise_for_status()

        get_platforms_data.platform_cache = response.json().get('platforms', [])
    
    return get_platforms_data.platform_cache

def get_accounts_data(platform):
    """Faz a requisição para o endpoint /accounts?platform={{platform}}"""
    platforms = get_platforms_data()

    valid_platforms = [p['value'] for p in platforms]

    if platform not in valid_platforms:
        raise ValueError(f"Invalid Platform: {platform}")

    headers = {
        'Authorization': f'{Config.STRACT_API_TOKEN}',
    }

    url = f"{Config.BASE_URL}/accounts?platform={platform}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_fields_data(platform):
    """Faz a requisição para o endpoint /fields?platform={{platform}}"""

    platforms = get_platforms_data()

    valid_platforms = [p['value'] for p in platforms]
    
    if platform not in valid_platforms:
        raise ValueError(f"Invalid Platform: {platform}")
    
    headers = {
        'Authorization': f'{Config.STRACT_API_TOKEN}',
    }

    url = f"{Config.BASE_URL}/fields?platform={platform}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()
