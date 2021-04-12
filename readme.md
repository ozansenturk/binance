#Binance Wrapper - Binance 101

####Installation
place an env. file into the root directory within the content below

```
Envrionment variables
```.env
APP_API_KEY='YOUR API KEY'
APP_SECRET_KEY='YOUR SECRET KEY'

BASE_URL='https://api.binance.com'
PING_GET='/api/v3/ping'
PRICE_TICKER_GET='/api/v3/ticker/price?symbol='
OPEN_ORDERS_GET='/api/v3/openOrders?recvWindow=60000&timestamp='
```

Installation
```python
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python wsgi.py


