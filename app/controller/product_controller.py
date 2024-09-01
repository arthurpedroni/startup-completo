from flask import Blueprint, render_template
from app.model.product import Product

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/<int:category_id>')
def list_products_by_category(category_id):
    products = [product for product in Product.all_products if product.category_id == category_id]
    return render_template('product.html', products=products)

@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in Product.all_products if p.id == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Produto não encontrado", 404
