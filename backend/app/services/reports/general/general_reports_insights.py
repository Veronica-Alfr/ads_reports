import logging
from ....utils.api_requests import get_platforms_data
from ..platform.platform_reports_insights import platform_insights

def get_all_platforms_insights():
    """
    Obtém os insights de todas as plataformas e consolida em uma única lista.
    Retorna uma lista de dicionários contendo os dados consolidados.
    """
    print("entrei aquiiiii!!!")
    platforms = get_platforms_data()
    print('platforms AQUI =>', platforms)
    all_insights = []

    for platform in platforms:
        platform_key_value = platform['value']
        try:
            platform_data = platform_insights(platform_key_value)
            print('platform_data AQUI =>', platform_data)
            all_insights.extend(platform_data)
            print('all_insights AQUI =>', all_insights)
        except ValueError as e:
            print(f"Error fetching insights for platform {platform_key_value}: {str(e)}")
            logging.error(f"Error fetching insights for platform {platform_key_value}: {str(e)}")
            continue

    return all_insights