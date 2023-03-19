from typing import List
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class CascadeDeleteOperation(UndoRedoOperation):
    def __init__(self, 
                 repository: Repository,
                 tranzactie_repository: Repository,
                 cascada_list: List):
        self.repository = repository
        self.tranzactie_repository = tranzactie_repository
        self.cascada_list = cascada_list

    def undo(self):
        for i in range(len(self.cascada_list) - 1):
            self.tranzactie_repository.read(self.cascada_list[i])
        self.repository.create(
            self.cascada_list[len(self.cascada_list) - 1])

    def redo(self):
        for i in range(len(self.cascada_list) - 1):
            self.tranzactie_repository.delete(
                self.cascada_list[0].id_entitate
            )
        self.repository.delete(
            self.cascada_list[len(self.cascada_list) - 1].id_entitate)
