import os
import requests
from dotenv import load_dotenv

load_dotenv()

def convert(amount, rate):
    return round(amount*rate, 2)

def get_rate(data, currency):
    key = f'USD{currency}'
    if key in data['quotes']:
        return data['quotes'][key]
    else:
        return None
    
def get_liveData():
    api_key = os.getenv('CURRENCY_API_KEY')
    url = f"http://api.currencylayer.com/live?access_key={api_key}"
    response = requests.get(url)
    return response.json()

def convert_curr(amount, from_currency, to_currency, data):
    if from_currency == 'USD':
        from_rate = 1.0
    else:
        from_rate = get_rate(data, from_currency)

    if to_currency == 'USD':
        to_rate = 1.0
    else:
        to_rate = get_rate(data, to_currency)

    if from_rate is None or to_rate is None:
        return None

    amount_in_usd = amount / from_rate
    result = round(amount_in_usd * to_rate, 2)
    return result
