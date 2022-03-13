from app import create_app
from modules.common.db_init import db
from modules.entities.location.models import UserLocation
from modules.entities.store.models import Item, Store, MenuItem
from modules.entities.users.models import User

app = create_app("LOCAL")
with app.app_context():
    user_obj = User.new(
        user_type="CUSTOMER",
        name="Prince Mathur"
    )
    db.session.flush()
    UserLocation.new(
        location_id=1,
        user_id=user_obj.id
    )
    db.session.flush()

    item1 = Item.new(
        item_name="Item 1",
        mrp=120.1
    )
    db.session.flush()
    item2 = Item.new(
        item_name="Item 2",
        mrp=220.1
    )
    db.session.flush()
    for i in range(1, 6):
        store = Store.new(
            name=f"Store {i}",
            location_id=i+1
        )
        db.session.flush()
        menu_item_1 = MenuItem.new(
            store_id=store.id,
            item_id=item1.id,
            item_price=110,
            available_quantity=4
        )
        db.session.flush()
        menu_item_2 = MenuItem.new(
            store_id=store.id,
            item_id=item2.id,
            item_price=220,
            available_quantity=10
        )
        db.session.flush()
    db.session.commit()