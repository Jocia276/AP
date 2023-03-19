from typing import List
from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.medicament import Medicament
from Domain.medicament_generator import MedicamentGenerator
from Domain.medicament_validator import MedicamentValidator
from Domain.multiple_update_operation import MultipleUpdateOperation
from Domain.update_operation import UpdateOperation
from Repository.repository import Repository
from Service.exceptions_service import NoMedError, ServiceValidationError
from Service.undo_redo_service import UndoRedoService


class MedicamentService:
    def __init__(self,
                 medicament_repository: Repository,
                 medicament_validator: MedicamentValidator,
                 medicament_generator: MedicamentGenerator,
                 undo_redo_service: UndoRedoService):
        self.medicament_repository = medicament_repository
        self.medicament_validator = medicament_validator
        self.medicament_generator = medicament_generator
        self.undo_redo_service = undo_redo_service

    def add_med(self,
                id_medicament: str,
                nume: str,
                producator: str,
                pret: float,
                necesita_reteta: str):
        medicament = Medicament(id_medicament, nume,
                                producator, pret, necesita_reteta)

        self.medicament_validator.validate(medicament)
        self.medicament_repository.create(medicament)

        self.undo_redo_service.add_to_undo(AddOperation(
            self.medicament_repository, medicament))

    def update_med(self,
                   id_medicament: str,
                   nume: str,
                   producator: str,
                   pret: float,
                   necesita_reteta: str):
        old_med = self.medicament_repository.read(id_medicament)
        medicament = Medicament(id_medicament, nume,
                                producator, pret, necesita_reteta)

        self.medicament_validator.validate(medicament)
        self.medicament_repository.update(medicament)

        self.undo_redo_service.add_to_undo(
            UpdateOperation(self.medicament_repository,
                            old_med,
                            medicament))

    def delete_med(self, id_medicament: str):
        medicament = self.medicament_repository.read(id_medicament)

        self.medicament_repository.delete(id_medicament)

        self.undo_redo_service.add_to_undo(
            DeleteOperation(self.medicament_repository, medicament))

    def get_all_med(self) -> List[Medicament]:
        return self.medicament_repository.read()

    def scumpire_medicament(self,
                            procent: int,
                            pret_dat: float):
        """
        Scumpirea unui medicament cu un procent dat daca acesta are pretul mai
        mic decat un pret dat
        :param procent: procentul dat de la tastatura
        :param pret_dat: pretul dat de la tastatura
        :return: mesaj
        """
        medicamente = self.medicament_repository.read()
        old_med_list = list(filter(lambda x: x.pret < pret_dat, medicamente))

        if self.medicament_repository.read() is None:
            raise NoMedError('Nu exista medicamente!')
        if pret_dat < 0:
            raise ServiceValidationError("Pretul trebuie sa fie pozitiv!")
        if procent <= 0:
            raise ServiceValidationError('Procentul trebuie sa fie pozitiv!')

        new_med_list = []
        for medicament in self.medicament_repository.read():
            if medicament.pret < pret_dat:
                medicament.pret = medicament.pret + \
                                  0.01 * procent * medicament.pret
                self.medicament_repository.update(medicament)
            new_med_list.append(self.medicament_repository.read(
                    medicament.id_entity))
            self.undo_redo_service.add_to_undo(
                MultipleUpdateOperation(self.medicament_repository,
                                        old_med_list,
                                        new_med_list))
        return " "

    def get_full_text(self, string_search) -> List:
        """
        :param string_search: stringul citit de la tastatura
        :return: toate medicamentele care contin stringul citit
        """

        medicamente = self.medicament_repository.read()

        def find(text, string):
            if len(text) <= 0:
                return None
            elif text[0:len(string)] == string:
                return string
            else:
                return find(text[1:], string)
        lst = []
        for medicament in medicamente:
            if find(str(medicament).lower(), string_search.lower()):
                lst.append(medicament)
        return lst
