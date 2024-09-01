from flask import Blueprint, render_template, redirect, url_for, request, session
from app.model.product import Product
from app.model.cart import Cart
import pickle

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

@cart_bp.route('/')
def view_cart():
    cart = session.get('cart', Cart())
    if isinstance(cart, bytes):
        cart = pickle.loads(cart)
    return render_template('cart.html', cart=cart)

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in Product.all_products if p.id == product_id), None)
    if not product:
        return "Product not found", 404
    cart = session.get('cart', Cart())
    if isinstance(cart, bytes):
        cart = pickle.loads(cart)
    quantity = int(request.form.get('quantity', 1))
    cart.add_item(product, quantity)
    session['cart'] = pickle.dumps(cart)
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', Cart())
    if isinstance(cart, bytes):
        cart = pickle.loads(cart)
    cart.remove_item(product_id)
    session['cart'] = pickle.dumps(cart)
    return redirect(url_for('cart.view_cart'))
