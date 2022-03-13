from modules.entities.cart.service import CartService
from modules.exceptions import NoRecordsFound, AddToCartError


class CartController:
    def add_to_cart(self, user_id, store_id, menu_item_id, quantity):
        cart_id = None
        try:
            cart_dict = CartService.get_user_cart(user_id=user_id)
            if cart_dict["store_id"] != store_id:
                raise AddToCartError(internal_err_message="Items already exists for other cart")
            cart_id = cart_dict["cart_id"]
        except NoRecordsFound:
            cartobj = CartService.create_user_cart(user_id=user_id, store_id=store_id)
            cart_id = cartobj.id
        CartService.add_item_to_cart(cart_id=cart_id, menu_item_id=menu_item_id, quantity=quantity)
