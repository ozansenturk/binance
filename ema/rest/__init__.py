from flask_restx import Api
from .bnc import bnc_ns

api = Api(title="Binance Wrapper App", version="1.0", description="The binance wrapper API")
api.add_namespace(bnc_ns)