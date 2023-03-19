from typing import List
from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.multiple_delete_operation import MultipleDeleteOperation
from Domain.tranzactie import Tranzactie
from Domain.update_operation import UpdateOperation
from Repository.exceptions import NoSuchIdError
from Repository.repository import Repository
from Service.exceptions_service import NoCardError,\
    NoMedError, NoTranzError, ServiceValidationError
from Service.undo_redo_service import UndoRedoService
from ViewModels.carduri_dupa_reduceri import CarduriDupaReduceri
from ViewModels.medicamente_dupa_vanzari import MedicamenteDupaVanzari
from utile import my_sort


class TranzactieService:
    def __init__(self,
                 medicament_repository: Repository,
                 card_repository: Repository,
                 tranzactie_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.tranzactie_repository = tranzactie_repository
        self.medicament_repository = medicament_repository
        self.card_repository = card_repository
        self.undo_redo_service = undo_redo_service

    def add_tranzactie(self,
                       id_tranzactie: str,
                       id_medicament: str,
                       id_card: str,
                       nr_bucati: int,
                       data: str,
                       ora: str):
        if self.medicament_repository.read(id_medicament) is None:
            raise NoSuchIdError(f'Nu exista niciun medicament '
                                f'cu id-ul {id_medicament}')
        if self.card_repository.read(id_card) is None:
            raise NoSuchIdError(f'Nu exista niciun card cu id-ul {id_card}')

        cardul = []
        pret_platit = 0
        valoare_reduceri = 0

        tranzactie = Tranzactie(id_tranzactie, id_medicament,
                                id_card, nr_bucati, data, ora,
                                pret_platit, valoare_reduceri)

        med = self.medicament_repository.read(str(id_medicament))

        if tranzactie.id_card:
            cardul.append(self.card_repository.read(str(id_card)))

        if len(cardul) == 1:
            if med.necesita_reteta == 'nu':
                total = float(float(med.pret) * nr_bucati)
                valori_reduceri = 0.1 * total
                tranzactie.pret_platit = total - valori_reduceri
                tranzactie.valoare_reduceri = valori_reduceri
            elif med.necesita_reteta == 'da':
                total = float(float(med.pret) * nr_bucati)
                valori_reduceri = 0.15 * total
                tranzactie.pret_platit = total - valori_reduceri
                tranzactie.valoare_reduceri = valori_reduceri
        else:
            tranzactie.pret_platit = float(float(med.pret) * nr_bucati)

        self.tranzactie_repository.create(tranzactie)

        self.undo_redo_service.add_to_undo(AddOperation(
            self.tranzactie_repository, tranzactie))

    def update_tranzactie(self,
                          id_tranzactie: str,
                          id_medicament: str,
                          id_card: str,
                          nr_bucati: int,
                          data: str,
                          ora: str
                          ):

        old_tranz = self.tranzactie_repository.read(id_tranzactie)

        if self.medicament_repository.read(id_medicament) is None:
            raise NoSuchIdError(f'Nu exista niciun medicament'
                                f' cu id-ul {id_medicament}')
        if self.card_repository.read(id_card) is None:
            raise NoSuchIdError(f'Nu exista niciun card cu id-ul {id_card}')

        cardul = []
        pret_platit = 0
        valoare_reduceri = 0

        tranzactie = Tranzactie(id_tranzactie, id_medicament,
                                id_card, nr_bucati, data, ora,
                                pret_platit, valoare_reduceri)

        med = self.medicament_repository.read(str(id_medicament))

        if tranzactie.id_card:
            cardul.append(self.card_repository.read(str(id_card)))

        if len(cardul) == 1:
            if med.necesita_reteta == 'nu':
                total = float(float(med.pret) * nr_bucati)
                valori_reduceri = 0.1 * total
                tranzactie.pret_platit = total - valori_reduceri
                tranzactie.valoare_reduceri = valori_reduceri
            elif med.necesita_reteta == 'da':
                total = float(float(med.pret) * nr_bucati)
                valori_reduceri = 0.15 * total
                tranzactie.pret_platit = total - valori_reduceri
                tranzactie.valoare_reduceri = valori_reduceri
        else:
            tranzactie.pret_platit = float(float(med.pret) * nr_bucati)

        self.tranzactie_repository.update(tranzactie)
        self.undo_redo_service.add_to_undo(
            UpdateOperation(self.tranzactie_repository,
                            old_tranz,
                            tranzactie))

    def delete_tranzactie(self, id_tranzactie: str):
        tranzactie = self.tranzactie_repository.read(id_tranzactie)
        self.tranzactie_repository.delete(id_tranzactie)
        self.undo_redo_service.add_to_undo(
            DeleteOperation(self.tranzactie_repository, tranzactie))

    def get_all_tranzactie(self) -> List[Tranzactie]:
        return self.tranzactie_repository.read()

    def afisare_tranzactii_dupa_data(self,
                                     data_initiala: str,
                                     data_finala: str):
        """
        Afiseaza toate tranzactiile intr-un interval de zile dat.
        :param data_initiala: data de la care se incepe afisarea tranzactiilor
        :param data_finala: data pana la care se afiseaza tranzactiile
        :return: toate tranzactiile intr-un interval de zile dat
        """
        tranzactii = self.tranzactie_repository.read()

        if self.tranzactie_repository.read() is None:
            raise NoTranzError('Nu exista tranzactii! ')
        if str(data_initiala) > str(data_finala):
            raise ServiceValidationError('Data initiala trebuie '
                                         'sa fie mai mica decat cea '
                                         'finala!')

        lst = []
        for tranzactie in tranzactii:
            if str(data_initiala) <= str(tranzactie.data) <= str(data_finala):
                lst.append(tranzactie)
        return lst

    def sterge_tranzactii_dupa_data(self,
                                    data_initiala: str,
                                    data_finala: str):
        """
        Sterge tranzactiile dintre doua date introduse de utilizator.
        :param data_initiala: prima data introdusa de utilizator
        :param data_finala: a doua data introdusa de utilizator
        :return: Tranzactiile fara cele care se sterg.
        """
        tranzactii = self.tranzactie_repository.read()
        lista_tranzactii_sterse = list(filter(
            lambda x: data_initiala <= x.data <= data_finala, tranzactii))

        if self.tranzactie_repository.read() is None:
            raise NoTranzError('Nu exista tranzactii! ')
        if str(data_initiala) > str(data_finala):
            raise ServiceValidationError('Data initiala trebuie '
                                         'sa fie mai mica decat'
                                         ' cea finala!')

        for tranzactie in tranzactii:
            if str(data_initiala) < str(tranzactie.data) < str(data_finala):
                self.tranzactie_repository.delete(tranzactie.id_entity)

        self.undo_redo_service.add_to_undo(
            MultipleDeleteOperation(self.tranzactie_repository,
                                    lista_tranzactii_sterse))
        return "Stergerea a fost efectuata cu succes!"

    def medicamente_ordonate_dupa_nr_vanzari(self) -> \
            List[MedicamenteDupaVanzari]:
        """
        :return: o lista cu medicamente ordonate
        descrescator in functie de numarul de vanzari
        """
        if self.medicament_repository.read() is None:
            raise NoMedError('Nu exista medicamente! ')
        if self.get_all_tranzactie() is None:
            raise NoTranzError('Nu exista tranzactii! ')
        result = []
        for medicament in self.medicament_repository.read():
            vanzari_pentru_medicament = filter(
                lambda vanzare:
                vanzare.id_medicament == medicament.id_entity,
                self.get_all_tranzactie())
            for tranzactie in vanzari_pentru_medicament:
                vanzari = tranzactie.nr_bucati
                result.append(MedicamenteDupaVanzari(medicament.nume, vanzari))
        return my_sort(result, key=lambda x: x.nr_bucati, reverse=True)

    def carduri_ordonate_desc_dupa_valoare_reduceri(self)\
            -> List[CarduriDupaReduceri]:
        """
        :return: o lista cu carduri ordonate descrescator
        in functie de valoarea reducerilor
        """
        if self.card_repository.read() is None:
            raise NoCardError("Nu exista carduri! ")
        if self.medicament_repository.read() is None:
            raise NoMedError("Nu exista medicamente! ")
        if self.get_all_tranzactie() is None:
            raise NoTranzError('Nu exista tranzactii! ')

        result = []
        for card in self.card_repository.read():
            reduceri_pentru_card = filter(
                lambda reducere: reducere.id_card == card.id_entity,
                self.get_all_tranzactie())
            for tranzactie in reduceri_pentru_card:
                reduceri = tranzactie.valoare_reduceri
                result.append(CarduriDupaReduceri(card.id_entity,
                                                  card.nume,
                                                  card.prenume,
                                                  reduceri))
        return my_sort(result, key=lambda x: x.reduceri, reverse=True)

    def get_full_text(self, string_search) -> List:
        """
        :param string_search: stringul citit de la tastatura
        :return: toate tranzactiile care contin stringul citit
        """
        tranzactii = self.tranzactie_repository.read()

        def find(text, string):
            if len(text) <= 0:
                return None
            elif text[0:len(string)] == string:
                return string
            else:
                return find(text[1:], string)

        lst = []
        for tranzactie in tranzactii:
            if find(str(tranzactie).lower(), string_search.lower()):
                lst.append(tranzactie)
        return lst

    def delete_cascada(self, id) -> None:
        lista = self.tranzactie_repository.read()
        for tranzactie in lista:
            if tranzactie.id_medicament == id:
                id_tranzactie = tranzactie.id_entity
                self.tranzactie_repository.delete(id_tranzactie)
        self.medicament_repository.delete(id)
