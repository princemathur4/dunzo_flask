from flask import Blueprint, request, jsonify, current_app
from modules.entities.store.controller import StoreController
from modules.exceptions import InvalidRequestPayload

store_bp = Blueprint('store', __name__)


@store_bp.route('/store', methods=['GET'])
def get_nearby_shops():
    user_id = request.args.get("user_id")
    if not user_id or not user_id.isnumeric():
        raise InvalidRequestPayload(internal_err_message="Invalid value for payload key: 'user_id'")
    user_id = int(user_id)
    nearby_shops = StoreController().get_nearby_shops(user_id=user_id)
    return jsonify({"status": True, "data": nearby_shops}), 200


@store_bp.route('/store/<int:store_id>/menu', methods=['GET'])
def get_store_menu_items(store_id):
    store_menu = StoreController().get_store_menu(store_id=store_id)
    return jsonify({"status": True, "data": store_menu}), 200
