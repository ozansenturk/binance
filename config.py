import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    APP_API_KEY=os.environ.get('APP_API_KEY')
    APP_SECRET_KEY=os.environ.get('APP_SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG=True


config = {
    'dev': DevConfig,
    'default': DevConfig
}
