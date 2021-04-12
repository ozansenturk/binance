import os

from ema import create_app
from ema.rest import api

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

