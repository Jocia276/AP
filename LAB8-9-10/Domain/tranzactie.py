from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Tranzactie(Entity):
    id_medicament: str
    id_card: str
    nr_bucati: int
    data: str
    ora: str
    pret_platit: float
    valoare_reduceri: float
