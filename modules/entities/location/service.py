from modules.common.db_init import db
from modules.entities.location.models import Location, UserLocation
from modules.exceptions import NoRecordsFound


class LocationService:

    @staticmethod
    def get_user_location(user_id):
        result = db.session.query(
            Location.latitude, Location.longitude, Location.city
        ).join(
            UserLocation, UserLocation.location_id == Location.id
        ).filter(
            UserLocation.user_id == user_id
        ).first()
        if not result:
            raise NoRecordsFound(internal_err_message="No user location found for this user")
        return {"latitude": result.latitude, "longitude": result.longitude, "city": result.city}
