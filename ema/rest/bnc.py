import os
import http.client
import logging
import json

from flask_restx import Namespace, Resource, fields
from ema.rest import utils

logging.basicConfig(level=logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(
                 '%(asctime)s %(levelname)s: %(message)s '
                 '[in %(pathname)s:%(lineno)d]'))

bnc_ns = Namespace('api', description='Binance APIs')
bnc_ns.logger.addHandler(stream_handler)

price_symbol_response = bnc_ns.model('price_symbol_response', {
    'symbol': fields.String(description='symbol key'),
    'price': fields.String(description='symbol price')
})

order_response = bnc_ns.model('order_response', {
    'symbol': fields.String(description='symbol key'),
    'origClientOrderId': fields.String(description='some key'),
    'orderId': fields.Integer(description='order id'),
    'orderListId': fields.Integer(description='order list id'),
    'clientOrderId': fields.String(description='client order id'),
    'price': fields.String(description='price'),
    'origQty': fields.String(description='origin quantity'),
    'status': fields.String(description='status'),
    'timeInForce': fields.String(description='time in force'),
    'type': fields.String(description='type'),
    'side': fields.String(description='side')
})


def ping_bnc():

    ping_url = os.environ.get('PING_GET')

    get_resp = utils.get_query(ping_url)

    return get_resp


def price_ticker(timestamp):

    price_ticker_url = os.environ.get('PRICE_TICKER_GET')

    response = utils.get_query(f'{price_ticker_url}{timestamp}')
    bnc_ns.logger.debug('response {response.text}')
    response_dict = json.loads(response.text)

    return response_dict


def get_order(timestamp, signature):

    price_ticker_url = f'{os.environ.get("OPEN_ORDERS_GET")}{timestamp}&signature={signature}'
    header = utils.prepare_header(os.environ.get('APP_API_KEY'))
    response = utils.get_query(price_ticker_url,headers=header)

    bnc_ns.logger.debug(f'response {response.text}')
    response_dict = json.loads(response.text)

    return response_dict


@bnc_ns.route('/ping')
class Ping(Resource):

    @bnc_ns.doc('ping the binance')
    @bnc_ns.marshal_with({}, envelope='data', code=http.client.OK)
    def get(self):
        """ping the binance API"""
        response = ping_bnc()
        bnc_ns.logger.debug("response {}".format(response))

        return response


@bnc_ns.route('/openOrders')
class Order(Resource):

    @bnc_ns.doc('get orders by date')
    @bnc_ns.marshal_with(order_response,
                         envelope='data',
                         code=http.client.OK)
    def get(self):
        """get all your open orders"""

        timestamp = utils.current_time()
        signature = utils.sign_request(f'recvWindow=60000&timestamp={timestamp}'.encode())
        response = get_order(timestamp, signature)

        return response


@bnc_ns.route('/price/symbol=<string:symbol>')
class PriceTicker(Resource):

    @bnc_ns.doc('get the price by the symbol')
    @bnc_ns.marshal_with(price_symbol_response,
                         code=http.client.OK)
    def get(self, symbol):
        """get the price by the symbol"""

        response = price_ticker(symbol)

        return response