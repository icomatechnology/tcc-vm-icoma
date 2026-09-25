from dataclasses import dataclass

@dataclass
class City:
    id: str
    name: str
    state: str
    initials: str
    country: str
    country_initials: str
    timezone: str
    health_cust: float
    airport: str