from .api_requests import get_platforms_data

def get_platform_value_by_name(platform_name):
    """
    Retorna o valor 'value' de uma plataforma com base no nome 'text'.
    
    :param platform_name: Nome da plataforma ('text').
    :return: O valor 'value' correspondente ou levanta um ValueError se não encontrado.
    """
    platforms = get_platforms_data()

    platform = next((p for p in platforms if p['text'] == platform_name), None)
    if platform:
        return platform['value']
    else:
        raise ValueError(f"Platform '{platform_name}' not found.")
