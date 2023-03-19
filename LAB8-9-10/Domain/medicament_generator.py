import string
from random import randint, choices, uniform, choice


class MedicamentGenerator:

    def generare_id(self) -> str:
        return str(randint(1, 300))

    def generare_nume(self) -> str:
        return ''.join(
                choices(string.ascii_lowercase + string.digits, k=20))

    def generare_producator(self) -> str:
        return ''.join(
            choices(string.ascii_lowercase + string.digits, k=20))

    def generare_pret(self) -> float:
        return uniform(2.5, 30.0)

    def generare_reteta(self) -> str:
        reteta = ['da', 'nu']
        return choice(reteta)
