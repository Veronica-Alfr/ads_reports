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

def get_accounts_data(params):
    """Faz a requisição para o endpoint /accounts?platform={{platform}}"""
    return make_api_request('accounts', params)

def get_fields_data(params):
    """Faz a requisição para o endpoint /fields?platform={{platform}}"""
    return make_api_request('fields', params)

def get_insights_data(platform, params):
    """
    Faz a requisição para o endpoint /insights usando os valores de 'id', 'token' das contas
    e o 'value' dos campos de dados, além de 'platform'
    """

    platform_data = {'platform': platform}

    accounts_data = get_accounts_data(platform_data)
    if not accounts_data.get('accounts'):
        raise ValueError("No accounts found for the given platform.")

    account_id = params.get('account')
    token_param = params.get('token')

    if not account_id:
        raise ValueError("Account id is required.")
    
    if not token_param:
        raise ValueError("Account token is required.")
    
    account = next((acc for acc in accounts_data['accounts'] if acc['id'] == account_id), None)
    if not account:
        raise ValueError(f"Account with id {account_id} not found.")

    token = account['token']
    
    if token != params.get('token'):
        raise ValueError("Account token does not match.")

    fields_data = get_fields_data(platform_data)
    if not fields_data.get('fields'):
        raise ValueError("No fields found for the given platform.")

    fields_requested = params.get('fields', '').split(',')
    if fields_requested:
        fields_data['fields'] = [field for field in fields_data['fields'] if field['value'] in fields_requested]
    
    insights_data = make_api_request('insights', params)

    return insights_data
