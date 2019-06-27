from apps import app
from views import home_view, cart_view
from flask_cors import CORS
APP_CONFIG={
    'host': 'localhost',
    'port': 5000,
    'debug': True
}
if __name__ == '__main__':
    CORS().init_app(app)
    app.register_blueprint(home_view.blue_home)
    app.register_blueprint(cart_view.blue_cart)
    app.run(**APP_CONFIG)