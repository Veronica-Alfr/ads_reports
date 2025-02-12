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

def make_api_request(endpoint, params):
    """Função genérica para fazer requisições GET para qualquer endpoint"""

    platforms = get_platforms_data()

    platform = params.get('platform')
    if not platform:
        raise ValueError("Platform is required in query parameters.")
    
    valid_platforms = [p['value'] for p in platforms]
    if platform not in valid_platforms:
        raise ValueError(f"Invalid Platform: {platform}")

    headers = {
        'Authorization': f'{Config.STRACT_API_TOKEN}',
    }

    url = f"{Config.BASE_URL}/{endpoint}"
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

def get_accounts_data(params):
    """Faz a requisição para o endpoint /accounts?platform={{platform}}"""
    return make_api_request('accounts', params)

def get_fields_data(params):
    """Faz a requisição para o endpoint /fields?platform={{platform}}"""
    return make_api_request('fields', params)
