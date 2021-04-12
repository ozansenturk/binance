from config import config
from flask import Flask


def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])
    config[config_name].init_app(application)

    application.config['RESTX_MASK_SWAGGER'] = False

    return application
