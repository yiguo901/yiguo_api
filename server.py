from apps import app
from views import home_view, cart_view
from flask_cors import CORS
APP_CONFIG={
    'host': '0.0.0.0',
    'port': 8003,
    'debug': True
}
if __name__ == '__main__':
    CORS().init_app(app)
    app.register_blueprint(home_view.blue_home)
    app.register_blueprint(cart_view.blue_cart)
    app.run(**APP_CONFIG)