from modules.common.db_init import db
from modules.entities.location.models import Location, UserLocation
from modules.entities.store.models import Store, MenuItem, Item
from modules.exceptions import NoRecordsFound


class StoreService:
    @staticmethod
    def get_all_stores(city):
        results = db.session.query(
            Store, Location
        ).join(
            Location,
            Location.id == Store.location_id
        ).filter(
            Location.city == city
        ).all()
        if not results:
            raise NoRecordsFound(internal_err_message="No stores found in this city")
        return [{
            "store_name": result[0].name,
            "latitude": result[1].latitude,
            "longitude": result[1].longitude,
            "address_line": result[1].address_line,
            "city": result[1].city,
            "state": result[1].state,
            "pincode": result[1].pincode,
        } for result in results]

    @staticmethod
    def get_store_menu_items(store_id):
        results = db.session.query(
            MenuItem, Item
        ).join(
            Item,
            Item.id == MenuItem.item_id
        ).filter(
            MenuItem.store_id == store_id
        ).all()
        if not results:
            raise NoRecordsFound(internal_err_message="No menu found for this store")
        return [
            {
                "item_name": result[1].item_name,
                "item_price": result[0].item_price,
                "available_quantity": result[0].available_quantity,
                "mrp": result[1].mrp,
            } for result in results
        ]
