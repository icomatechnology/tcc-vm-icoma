from app.repositories.city_repository import CityRepository
from app.models.city import City

class CityService:
    def __init__(self):
        self.city_repo = CityRepository()

    def get_all_cities(self):
        return self.city_repo.get_all_cities()

    def get_city(self, city_id: str):
        return self.city_repo.get_city(city_id)

    def create_city(self, data: dict):
        city = City(
            id=None,
            name=data.get('name'),
            state=data.get('state'),
            initials=data.get('initials'),
            country=data.get('country'),
            country_initials=data.get('country_initials'),
            timezone=data.get('timezone'),
            health_cust=float(data.get('health_cust', 0.0)),
            airport=data.get('airport')
        )
        return self.city_repo.add_city(city)

    def update_city(self, city_id: str, data: dict):
        city = City(
            id=city_id,
            name=data.get('name'),
            state=data.get('state'),
            initials=data.get('initials'),
            country=data.get('country'),
            country_initials=data.get('country_initials'),
            timezone=data.get('timezone'),
            health_cust=float(data.get('health_cust', 0.0)),
            airport=data.get('airport')
        )
        return self.city_repo.update_city(city_id, city)
