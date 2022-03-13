from flask import Blueprint, request, jsonify, current_app

from modules.common.db_init import db
from modules.entities.cart.controller import CartController
from modules.entities.store.controller import StoreController
from modules.exceptions import InvalidRequestPayload

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/cart/store/<int:store_id>/menu_item/<int:menu_item_id>', methods=['POST'])
def add_to_cart(store_id, menu_item_id):
    user_id = request.json.get("user_id")
    if user_id is None or not isinstance(user_id, int):
        raise InvalidRequestPayload(internal_err_message="Invalid value for payload key: 'user_id'")

    quantity = request.json.get("quantity")
    if quantity is None or not isinstance(quantity, int):
        raise InvalidRequestPayload(internal_err_message="Invalid value for payload key: 'quantity'")

    CartController().add_to_cart(user_id=user_id, store_id=store_id, menu_item_id=menu_item_id, quantity=quantity)
    db.session.commit()
    return jsonify({"status": True, "message": "Added to cart successfully"}), 200

