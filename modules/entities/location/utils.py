import haversine as hs


class LocationUtils:
    @staticmethod
    def get_distance_between_locations(location1, location2):
        # To calculate distance in meters
        distance = hs.haversine(location1, location2, unit=hs.Unit.KILOMETERS)
        return distance
