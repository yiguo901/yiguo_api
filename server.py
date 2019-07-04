from apps import app

from flask_cors import CORS
APP_CONFIG={
    'host': '0.0.0.0',
    'port': 8003,
    'debug': True
}
if __name__ == '__main__':
    CORS().init_app(app)
<<<<<<< HEAD
    from views import home_view, cart_view, user_view, order_view, mine_view, address_view
=======
    from views import home_view, cart_view, user_view, order_view, mine_view, es_view
>>>>>>> bf8bb083743f9b1f42a4d0b2ca94965036d3dbeb

    app.register_blueprint(user_view.blue)
    app.register_blueprint(home_view.blue_home)
    app.register_blueprint(cart_view.blue_cart)
    app.register_blueprint(order_view.blue_order)
    app.register_blueprint(mine_view.mine_blue)
<<<<<<< HEAD
    app.register_blueprint(address_view.blue_addr)
=======
    app.register_blueprint(es_view.blue_es)
>>>>>>> bf8bb083743f9b1f42a4d0b2ca94965036d3dbeb
    app.run(**APP_CONFIG)