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


def sign_request(params):
    secret_key = os.environ.get("APP_SECRET_KEY").encode()
    signature = hmac.new(secret_key, params, hashlib.sha256).hexdigest()
    print(f'signature = {signature}')
    return signature
