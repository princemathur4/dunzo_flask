from modules.common.db_init import db
from modules.entities.cart.models import Cart, CartItem
from modules.entities.location.models import Location, UserLocation
from modules.exceptions import NoRecordsFound


class CartService:

    @staticmethod
    def get_user_cart(user_id):
        result = db.session.query(
            CartItem, Cart
        ).join(
            Cart,
            CartItem.cart_id == Cart.id
        ).filter(
            Cart.user_id == user_id
        ).first()

        if not result:
            raise NoRecordsFound(internal_err_message="No user location found for this user")
        return {
            "cart_id": result[1].id, "menu_item_id": result[0].menu_item_id, "quantity": result[0].quantity,
            "store_id": result[1].store_id
        }

    @staticmethod
    def create_user_cart(user_id, store_id):
        cart_obj = Cart.new(user_id=user_id, store_id=store_id)
        db.session.flush()
        return cart_obj

    @staticmethod
    def add_item_to_cart(cart_id, menu_item_id, quantity=1, discount_percentage=0):
        cart_item_obj = db.session.query(
            CartItem
        ).filter(
            CartItem.cart_id == cart_id
        ).first()
        if cart_item_obj:
            cart_item_obj.quantity += quantity
        else:
            cart_item_obj = CartItem.new(
                cart_id=cart_id, menu_item_id=menu_item_id, quantity=quantity,
                discount_percentage=discount_percentage
            )
        db.session.flush()
        return cart_item_obj
