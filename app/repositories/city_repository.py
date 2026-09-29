import firebase_admin
from firebase_admin import firestore
from app.models.city import City

class CityRepository:
    def get_all_cities(self) -> list[City]:
        db = firestore.client()
        docs = db.collection('cities').stream()
        cities = []
        for doc in docs:
            data = doc.to_dict()
            cities.append(City(id=doc.id,
                                name=data.get('name'),
                                state=data.get('state'),
                                initials=data.get('initials'),
                                country=data.get('country'), 
                                country_initials=data.get('country_initials'),
                                timezone=data.get('timezone'),
                                health_cust=data.get('health_cust'),
                                airport=data.get('airport')))
        return cities

    def get_city(self, city_id: str) -> City:
        db = firestore.client()
        doc = db.collection('cities').document(city_id).get()
        if doc.exists:
            data = doc.to_dict()
            return City(id=doc.id, 
                        name=data.get('name'),
                        state=data.get('state'), 
                        initials=data.get('initials'),
                        country=data.get('country'), 
                        country_initials=data.get('country_initials'),
                        timezone=data.get('timezone'),
                        health_cust=data.get('health_cust'),
                        airport=data.get('airport'))
        return None

    def add_city(self, city: City) -> str:
        db = firestore.client()
        doc = db.collection('cities').add({
            'name': city.name,
            'state': city.state,
            'initials': city.initials,
            'country': city.country, 
            'country_initials': city.country_initials,
            'timezone': city.timezone,
            'health_cust': city.health_cust,
            'airport': city.airport
        })
        return doc[1].id

    def update_city(self, city_id: str, city: City) -> bool:
        db = firestore.client()
        db.collection('cities').document(city_id).update({
            'name': city.name,
            'state': city.state,
            'initials': city.initials,
            'country': city.country, 
            'country_initials': city.country_initials,
            'timezone': city.timezone,
            'health_cust': city.health_cust,
            'airport': city.airport
        })
        return True