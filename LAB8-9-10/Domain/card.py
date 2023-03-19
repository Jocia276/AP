from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Card(Entity):
    nume: str
    prenume: str
    cnp: str
    data_nasterii: str
    data_inregistrarii: str
