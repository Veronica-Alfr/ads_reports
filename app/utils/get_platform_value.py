from .api_requests import get_platforms_data

def get_platform_value_by_name(platform_name):
    platforms = get_platforms_data()

    platform = next((p for p in platforms if p['text'] == platform_name), None)
    if platform:
        return platform['value']
    else:
        raise ValueError(f"Platform '{platform_name}' not found.")
