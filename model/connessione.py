from dataclasses import dataclass


@dataclass
class Connessione:
    l1: str
    l2: str
    lat1: float
    lon1: float
    lat2: float
    lon2: float

    def __hash__(self):
        return hash(self.l1)
