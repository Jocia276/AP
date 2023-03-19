from Domain.medicament import Medicament


class MedicamentValidationError(Exception):
    pass


class MedicamentValidator:

    def validate(self, medicament: Medicament):
        errors = []
        valori_necesita_reteta = ['da', 'nu']
        if medicament.necesita_reteta not in valori_necesita_reteta:
            errors.append(f"Valoarea pentru necesita_reteta"
                          f" trebuie sa fie una dintre"
                          f" {valori_necesita_reteta}")
        pret = float(medicament.pret)
        if pret < 0 or pret == 0:
            errors.append('Pretul trebuie sa fie pozitiv!')
        if errors:
            raise MedicamentValidationError(errors)
