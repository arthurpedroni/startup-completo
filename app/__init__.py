from flask import Flask
from app.controller.home_controller import home_bp
from app.controller.cart_controller import cart_bp
from app.controller.product_controller import product_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Change to a random secret key for production
    app.register_blueprint(home_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    return app
