from flask_restx import Api
from .bnc import bnc_ns

api = Api(title="Binance Wrapper App", version="1.0",
          description="Ozan Senturk ozan.senturk@gmail.com",
          contact="ozan.senturk@gmail.com")
api.add_namespace(bnc_ns)