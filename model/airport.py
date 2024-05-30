from dataclasses import dataclass
from datetime import datetime
@dataclass
class Airport:
    id:int
    iata_code:str
    airport:str
    city:str
    state:str
    country:str
    latitude:int
    longitude:int
    timezone_offset:int

    def __hash__(self):
        return hash(id)
    def __str__(self):
        return(f"Airport id: {self.id}, Airport name: {self.airport}, Airport city: {self.city}")