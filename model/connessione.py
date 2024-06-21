from dataclasses import dataclass


@dataclass
class Connessione:
    Location: str
    Latitude: float
    Longitude: float

    def __hash__(self):
        return hash(self.Location)
