import requests
import datetime
import os
import os.path
from datetime import datetime
import hmac
import hashlib


def current_time():
    today = int(datetime.now().timestamp())*1000
    return today


def string_to_date(date_str):
    datee = datetime.strptime(date_str, "%Y-%m-%d")

    return datee

def get_current_year(date_str):

    datee = datetime.strptime(date_str, "%Y-%m-%d")

    return datee.year


def get_current_month(date_str):

    datee = datetime.strptime(date_str, "%Y-%m-%d")

    return datee.month


def prepare_header(api_key):

    headers = {
        'X-MBX-APIKEY': f'{api_key}'
    }

    return headers


def post_query(service_endpoint, data, headers=None, params=None):

    base_url = os.environ.get("BASE_URL")

    response = requests.post(f'{base_url}{service_endpoint}', data=data, headers=headers, params=params)

    return response

def get_query(service_endpoint, headers=None, params=None):

    base_url = os.environ.get("BASE_URL")

    response = requests.get(f'{base_url}{service_endpoint}', headers=headers, params=params)

    return response


def get_bearer_token(client_id=None, client_secret=None):

    if (client_id is None) & (client_secret is None):
        client_id = os.environ.get("API_KEY")
        client_secret=os.environ.get("API_SECRET_KEY")

    auth_url = os.environ.get("URL_AUTH")

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_headers = prepare_header(client_id, client_secret)

    auth_resp = post_query(auth_url, auth_data, auth_headers)

    return auth_resp


def sign_request(params):
    secret_key = os.environ.get("APP_SECRET_KEY").encode()
    signature = hmac.new(secret_key, params, hashlib.sha256).hexdigest()
    print(f'signature = {signature}')
    return signature
