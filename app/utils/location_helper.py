from geopy.geocoders import Nominatim


async def get_location_from_coordinates(
    latitude: float,
    longitude: float
):

    geolocator = Nominatim(
        user_agent="news_app"
    )

    location = geolocator.reverse(
        f"{latitude}, {longitude}",
        language="en"
    )

    if not location:
        return None

    address = location.raw.get(
        "address",
        {}
    )

    return {
        "country": address.get("country"),
        "state": address.get("state"),
        "district": (
            address.get("state_district")
            or address.get("county")
            or address.get("district")
        ),
        "city": (
            address.get("city")
            or address.get("town")
            or address.get("village")
        )
    }