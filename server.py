from apps import app

from flask_cors import CORS
APP_CONFIG={
    'host': '0.0.0.0',
    'port': 8003,
    'debug': True
}
if __name__ == '__main__':
    CORS().init_app(app)

    from views import home_view, cart_view, user_view, order_view, mine_view, address_view, es_view

    app.register_blueprint(user_view.blue)
    app.register_blueprint(home_view.blue_home)
    app.register_blueprint(cart_view.blue_cart)
    app.register_blueprint(order_view.blue_order)
    app.register_blueprint(mine_view.mine_blue)
    app.register_blueprint(address_view.blue_addr)
    app.register_blueprint(es_view.blue_es)

    app.run(**APP_CONFIG)