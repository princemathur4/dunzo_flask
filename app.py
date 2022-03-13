import os
from flask import Flask

from modules.common.db_init import db
from modules.exceptions import InvalidInputParamter


PROD = "PROD"
DEV = "DEV"
LOCAL = "LOCAL"
STAGING = "STAGING"
ENV = [PROD, DEV, STAGING, LOCAL]


def load_config(app, env):
    app.config["ENVIRONMENT"] = env
    global_config_path = os.path.join(app.root_path, "config/default.py")
    app.config.from_pyfile(global_config_path)

    env_config_path = os.path.join(app.root_path, f"config/{env.lower()}.py")
    app.config.from_pyfile(env_config_path)


def create_app(env: str):
    if env not in ENV:
        raise InvalidInputParamter(f"Invalid value for env={env}")

    app = Flask(__name__)
    load_config(app, env)

    db.init_app(app=app)

    # from modules.entities.users.models import User, UserRole, Role
    # from modules.entities.location.models import Location, UserLocation
    # from modules.entities.store.models import Store, Item, MenuItem
    # from modules.entities.cart.models import Cart, CartItem
    # from modules.entities.order.models import Order, OrderItem
    # db.create_all(app=app)
    register_blueprints(app)

    print("#" * 50, f"{' ' * 10} * Environment: {env}", "#" * 50, sep='\n')

    return app


def register_blueprints(app):
    from modules.entities.store.views import store_bp
    app.register_blueprint(store_bp)
    from modules.entities.cart.views import cart_bp
    app.register_blueprint(cart_bp)
    from modules.common.base_blueprint import base_bp
    app.register_blueprint(base_bp)


if __name__ == "__main__":
    app = create_app(LOCAL)
    app.run(port=5000, debug=True)
