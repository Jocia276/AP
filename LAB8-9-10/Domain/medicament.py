from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Medicament(Entity):
    nume: str
    producator: str
    pret: float
    necesita_reteta: str
