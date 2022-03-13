from flask import current_app

from modules.entities.location.service import LocationService
from modules.entities.location.utils import LocationUtils
from modules.entities.store.service import StoreService


class StoreController:

    def get_nearby_shops(self, user_id):
        user_location_result = LocationService.get_user_location(user_id=user_id)
        user_location = [user_location_result["latitude"], user_location_result["longitude"]]
        all_stores = StoreService.get_all_stores(city=user_location_result["city"])
        all_nearby_stores = []
        for store_dict in all_stores:
            distance = LocationUtils.get_distance_between_locations(
                location1=user_location,
                location2=[store_dict["latitude"], store_dict["longitude"]]
            )
            if distance <= current_app.config["NEARBY_DISTANCE"]:
                all_nearby_stores.append(store_dict)
        return all_nearby_stores

    def get_store_menu(self, store_id):
        menu_items = StoreService.get_store_menu_items(store_id=store_id)
        return menu_items
