from ...utils.api_requests import make_api_request

def get_accounts_data(params):
    return make_api_request('accounts', params)

def get_fields_data(params):
    return make_api_request('fields', params)

def get_insights_data(platform, params):
    params['platform'] = platform

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
