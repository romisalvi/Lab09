
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flight:
    id:int
    airline_id: int
    flight_number:int
    tail_number:str
    origin_airport_id:int
    destination_airport_id:int
    scheduled_departure_date:datetime
    departure_delay:int
    elapsed_time:int
    distance:int
    arrival_date:datetime
    arrival_delay:int
    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return (f" Flight id: {self.id}, OG airport: {self.origin_airport_id}, ArrAirport: {self.destination_airport_id}, distance: {self.distance} ")

