from flask import Flask
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import config
from models import db
from routes.customer_routes import customer_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

cache = Cache(app)
limiter = Limiter(key_func=get_remote_address, app=app)

app.register_blueprint(customer_bp)

if __name__ == '__main__':
    app.run(debug=True)
