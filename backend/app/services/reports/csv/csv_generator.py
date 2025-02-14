import csv
import io

def generate_csv_insights(data):
    """
    Gera um arquivo CSV a partir dos dados passados de determinada plataforma.
    
    :param data: Lista de dicionários contendo os dados a serem convertidos para CSV.
    :return: Um buffer de memória (StringIO) contendo o CSV.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    
    headers = ['Account Owner', 'Platform'] + list(data[0]['insights'][0].keys())
    writer.writerow(headers)
    
    for account in data:
        for insight in account['insights']:
            row = [account['account_name'], account['platform']] + list(insight.values())
            writer.writerow(row)
    
    output.seek(0)
    return output